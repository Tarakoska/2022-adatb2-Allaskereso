import tkinter as tk
import dao

labels = []


def showResult(result):
    for label in labels:
        label.destroy()

    coln_i = 0
    for col_name in result[0]:
        tmp = tk.Label(root, text=col_name)
        tmp.grid(row=1, column=0 + coln_i)
        labels.append(tmp)
        coln_i += 1

    row_i = 0
    for row in result[1]:
        col_i=0
        for col in row:
            tmp = tk.Label(root, text=col)
            tmp.grid(row=2 + row_i, column=0+col_i)
            labels.append(tmp)
            col_i+=1
        row_i += 1


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
root.geometry("1050x600")
root.text = tk.Label()

root.btn = tk.Button(text="Oneletrajzok", command=oneletrajzokShow)
root.btn.grid(row=0, column=0)

root.btn = tk.Button(text="Hirdetesek", command=hirdetesekShow)
root.btn.grid(row=0, column=1)

root.btn = tk.Button(text="Felhasznalo", command=felhasznaloShow)
root.btn.grid(row=0, column=2)

root.btn = tk.Button(text="Munkaadó", command=munkaAdoShow)
root.btn.grid(row=0, column=3)

root.btn = tk.Button(text="HirdetesFeladas", command=hirdetesFeladasShow)
root.btn.grid(row=0, column=4)

root.btn = tk.Button(text="Allaskereso", command=allaskeresoShow)
root.btn.grid(row=0, column=5)

root.btn = tk.Button(text="Birtokol", command=birtokolShow)
root.btn.grid(row=0, column=6)

root.btn = tk.Button(text="Jelentkezes", command=jelentkezesShow)
root.btn.grid(row=0, column=7)
root.mainloop()
