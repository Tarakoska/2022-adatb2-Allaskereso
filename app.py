import tkinter as tk
import dao

def showResult(result):
    root.text.destroy()
    i=0
    for r in result:
        root.text = tk.Label()
        root.text["text"] = r
        root.text.grid(row=1+i, column=0)
        i+=1

def oneletrajzokShow():
    showResult(dao.oneletrajzokQuerry())

def hirdetesekShow():
    showResult(dao.hirdetesekQuerry())

def felhasznaloShow():
    showResult(dao.felhasznaloQuerry())

def munkaAdoShow():
    showResult(dao.munkaAdoQuerry())

def hirdetesFeladasShow():
    showResult(dao.hirdetesFeladasQuerry())

def allaskeresoShow():
    showResult(dao.allaskeresoQuerry())

def birtokolShow():
    showResult(dao.birtokolQuerry())

def jelentkezesShow():
    showResult(dao.jelentkezesQuerry())

root = tk.Tk()
root.title("Állásbörze")
root.geometry("800x500")
root.text = tk.Label()


root.btn = tk.Button(text="Oneletrajzok", command=oneletrajzokShow)
root.btn.grid(row=0,column=0)

root.btn = tk.Button(text="Hirdetesek", command=hirdetesekShow)
root.btn.grid(row=0,column=1)

root.btn = tk.Button(text="Felhasznalo", command=felhasznaloShow)
root.btn.grid(row=0,column=2)

root.btn = tk.Button(text="Munkaadó", command=munkaAdoShow)
root.btn.grid(row=0,column=3)

root.btn = tk.Button(text="HirdetesFeladas", command=hirdetesFeladasShow)
root.btn.grid(row=0,column=4)

root.btn = tk.Button(text="Allaskereso", command=allaskeresoShow)
root.btn.grid(row=0,column=5)

root.btn = tk.Button(text="Birtokol", command=birtokolShow)
root.btn.grid(row=0,column=6)

root.btn = tk.Button(text="Jelentkezes", command=jelentkezesShow)
root.btn.grid(row=0,column=7)
root.mainloop()