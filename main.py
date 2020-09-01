import time
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

start_time = time.time()


def getfactorial(n):
    sums = []
    running = 1
    for i in range(n, 1, -1):
        running *= i
    print(running)


def getfactors(n):
    factors = []
    arr = []
    for i in range(1, n + 1):
        arr.append(i)

    for i in arr:
        for j in arr:
            if i * j == n:
                factors.append(str(i))

    if len(factors) == 2:
        '''print('number is prime')'''
        pass
    return factors


def isprime(n):
    arr = getfactors(n)
    primebool = False
    if len(arr) == 2:
        '''print(str(n))'''
        primebool = True
        return primebool


def getprimes(h, l=0):
    primes = []
    for i in range(l, h):
        isprime(i)
        if isprime(i):
            primes.append(i)
    print(primes)
    print("--- %s seconds ---" % (time.time() - start_time))
    return primes


def main():
    root = Tk()
    var = StringVar
    v = ["Get Factors for Number", "Is the number prime", "Get Primes within a range"]
    cmbo = ttk.Combobox(root, textvariable=var, values=v)
    cmbo.pack()

    def getChoice():
        if cmbo.get() == "Get Factors for Number":
            fact = Tk()
            root.destroy()
            ent = ttk.Entry(fact, width=30)
            ent.pack()
            x = ent.get()

            def displayfactors(n):
                x = getfactors(n)
                out = ""
                for i in x:
                    out += i + "\n"
                factorwin = Tk()
                lblfact = ttk.Label(factorwin, text=out).pack()

                factorwin.mainloop()

            btnget = ttk.Button(fact, text='enter', command=lambda: displayfactors(int(ent.get()))).pack()
        elif cmbo.get() == "Is the number prime":
            root.destroy()
            isprimewin = Tk()
            ent = ttk.Entry(isprimewin, width=30)
            ent.pack()

            x = ent.get()

            lbl = ttk.Label(isprimewin)

            def displayres(n):
                if isprime(n) == True:
                    lbl.config(text="The Number is Prime")
                    lbl.pack()
                else:
                    lbl.config(text="The Number is not Prime")
                    lbl.pack()

            btngetres = ttk.Button(isprimewin, text='enter', command=lambda: displayres(int(ent.get()))).pack()

        else:
            root.destroy()
            getprimeswin = Tk()
            ent1 = ttk.Entry(getprimeswin, width=30)
            ent1.pack()
            ent2 = ttk.Entry(getprimeswin, width=30)
            ent2.pack()

            def displayprimes(l, h):
                g = getprimes(h, l)
                out = ""
                for i in g:
                    out += str(i) + "\n"
                print(out)

                primewin = Tk()
                text = Text(primewin, width=10, height=10, wrap='word')
                primelbl = ttk.Label(primewin)
                text.grid(row=0, column=0)
                text.insert('1.0', out)
                scrollbar = ttk.Scrollbar(primewin, orient=VERTICAL, command=text.yview)
                scrollbar.grid(row=0, column=1, sticky='ns')
                text.config(yscrollcommand=scrollbar.set)
                text.config(state=DISABLED)

                def primeplot():
                    plt.plot(g, 'bo')
                    plt.show()


                btnPlot = ttk.Button(primewin, text="Plot", command=primeplot).grid(row=1, column=0, sticky='ew')
                primewin.mainloop()

            btnget = ttk.Button(getprimeswin, text='get primes',
                                command=lambda: displayprimes((int(ent1.get())), (int(ent2.get())))).pack()

            getprimeswin.mainloop()

    btn = ttk.Button(root, text='choose', command=getChoice).pack()
    root.mainloop()


print(getprimes(45))
main()
