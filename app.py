import tkinter as tk
import dao
from var import *


labels = []
entries = []

buttons_col=0
buttons_width=20
data_row=3

# default:
selected_menu=Tabla.ONELETRAJZ


def showResult(result):
    global beszur_btn
    for label in labels:
        label.destroy()

    for entry in entries:
        entry.destroy()

    beszur_btn.destroy()

    for e in range(len(result[0])-1):
        entry_txt = tk.Entry(root)
        entry_txt.grid(row=1, column=2 + e)
        entries.append(entry_txt)

    coln_i = 0
    for col_name in result[0]:

        tmp = tk.Label(root, text=col_name)
        tmp.grid(row=data_row, column=1 + coln_i)
        labels.append(tmp)
        coln_i += 1

    beszur_btn = tk.Button(root, text="Beszúr", command=insert)
    beszur_btn.grid(row=1,column=1 + coln_i)

    row_i = 0
    for row in result[1]:
        col_i=0
        for col in row:
            tmp = tk.Label(root, text=col)
            tmp.grid(row=data_row + 1 + row_i, column=1 + col_i)
            labels.append(tmp)
            col_i+=1
        row_i += 1


def showEntries():
    for entry in entries:
        entry.destroy()


def show(menu):
    global selected_menu
    selected_menu = menu
    showResult(dao.querry(menu))
    updateLabel()

def insert():
    match selected_menu:
        case Tabla.ONELETRAJZ:
            insertOneletrajzok()
        case Tabla.HIRDETESEK:
            insertHirdetesek()
        case Tabla.FELHASZNALO:
            insertFelhasznalo()
        case Tabla.MUNKAADO:
            insertMunkaado()
        case Tabla.HIRDETESFELAD:
            insertHirdetesFeladas()
        case Tabla.ALLASKERESO:
            insertAllaskereso()
        case Tabla.BIRTOKOL:
            insertBirtokol()
        case Tabla.JELENTKEZES:
            insertJelentkezes()
        case Tabla.SZAKMAK:
            insertSzakmak()

def insertOneletrajzok():
    format = entries[0].get()
    # ToDo: input ellenorzes
    values = [format]
    dao.insert(INSERT_ONEL,values)
    showResult(dao.querry(selected_menu))

def insertHirdetesek():
    nev = entries[0].get()
    leiras = entries[1].get()
    # ToDo: input ellenorzes
    values = [nev,leiras]
    dao.insert(INSERT_HIRD,values)
    showResult(dao.querry(selected_menu))

def insertFelhasznalo():
    veznev = entries[0].get()
    kernev = entries[1].get()
    felhnev = entries[2].get()
    jelszo = entries[3].get()
    email = entries[4].get()
    varos = entries[5].get()
    utca = entries[6].get()
    hazszam = entries[7].get()
    telefon = entries[8].get()
    isadmin = entries[9].get()
    # ToDo: input ellenorzes
    values = [veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin]
    dao.insert(INSERT_FELH,values)
    showResult(dao.querry(selected_menu))

def insertMunkaado():
    beosztas = entries[0].get()
    ertekeles = entries[1].get()
    feid = entries[2].get()
    # ToDo: input ellenorzes
    values = [beosztas, ertekeles, feid]
    dao.insert(INSERT_MUNK, values)
    showResult(dao.querry(selected_menu))

def insertHirdetesFeladas():
    muid = entries[0].get()
    # ToDo: input ellenorzes
    values = [muid]
    dao.insert(INSERT_HIFE, values)
    showResult(dao.querry(selected_menu))

def insertAllaskereso():
    szulido = entries[0].get()
    onid = entries[1].get()
    feid = entries[2].get()
    # ToDo: input ellenorzes
    values = [szulido, onid, feid]
    dao.insert(INSERT_ALLA, values)
    showResult(dao.querry(selected_menu))

def insertBirtokol():
    szakid = entries[0].get()
    allid = entries[1].get()
    # ToDo: input ellenorzes
    values = [szakid, allid]
    dao.insert(INSERT_BIRT, values)
    showResult(dao.querry(selected_menu))

def insertJelentkezes():
    allid = entries[0].get()
    hiid = entries[1].get()
    # ToDo: input ellenorzes
    values = [allid, hiid]
    dao.insert(INSERT_JELE, values)
    showResult(dao.querry(selected_menu))

def insertSzakmak():
    nev = entries[0].get()
    leiras = entries[1].get()
    # ToDo: input ellenorzes
    values = [nev, leiras]
    dao.insert(INSERT_SZAK, values)
    showResult(dao.querry(selected_menu))

def updateLabel():
    root.beszurLabel['text']="Jelen Tábla: "+ selected_menu.value + ", Adatbeszúrás:"


root = tk.Tk()
root.title("Állásbörze")
root.geometry("1050x600")
beszur_btn = tk.Button(root)

root.beszurLabel = tk.Label(text="Jelen Tábla: "+ selected_menu.value + ", Adatbeszúrás:")
root.beszurLabel.grid(row=0,column=1,columnspan=3)

root.btn = tk.Button(text="Oneletrajzok", width=buttons_width, command=lambda: show(Tabla.ONELETRAJZ))
root.btn.grid(row=0, column=buttons_col)

root.btn = tk.Button(text="Hirdetesek",width=buttons_width, command=lambda: show(Tabla.HIRDETESEK))
root.btn.grid(row=1, column=buttons_col)

root.btn = tk.Button(text="Felhasznalo",width=buttons_width, command=lambda: show(Tabla.FELHASZNALO))
root.btn.grid(row=2, column=buttons_col)

root.btn = tk.Button(text="Munkaadó",width=buttons_width, command=lambda: show(Tabla.MUNKAADO))
root.btn.grid(row=3, column=buttons_col)

root.btn = tk.Button(text="HirdetesFeladas",width=buttons_width, command=lambda: show(Tabla.HIRDETESFELAD))
root.btn.grid(row=4, column=buttons_col)

root.btn = tk.Button(text="Allaskereso",width=buttons_width, command=lambda: show(Tabla.ALLASKERESO))
root.btn.grid(row=5, column=buttons_col)

root.btn = tk.Button(text="Birtokol",width=buttons_width, command=lambda: show(Tabla.BIRTOKOL))
root.btn.grid(row=6, column=buttons_col)

root.btn = tk.Button(text="Jelentkezes",width=buttons_width, command=lambda: show(Tabla.JELENTKEZES))
root.btn.grid(row=7, column=buttons_col)

root.btn = tk.Button(text="Szakmak",width=buttons_width, command=lambda: show(Tabla.SZAKMAK))
root.btn.grid(row=7, column=buttons_col)
root.mainloop()
