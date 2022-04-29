import tkinter as tk
import dao
from var import *


labels = []
entries = []

buttons_col=0
buttons_width=20
data_row=3
data_col=3

# default:
selected_menu=Tabla.ONELETRAJZ
selectedRowData=""

def showResult(result):
    global beszur_btn, entries, labels
    for label in labels:
        label.destroy()
    labels = []
    for entry in entries:
        entry.destroy()
    entries = []
    beszur_btn.destroy()
    # input mezők
    for e in range(len(result[0])-1):
        entry_txt = tk.Entry(root)
        entry_txt.grid(row=2+e, column=1)
        entries.append(entry_txt)
    coln_i = 1
    for col_name in result[0]:
        tmpLabel = tk.Label(root, text=col_name)
        tmpLabel.grid(row=coln_i, column=0)
        labels.append(tmpLabel)
        coln_i += 1

    #Beszur gomb
    beszur_btn = tk.Button(root, text="Beszúr", command=insert)
    beszur_btn.grid(row=coln_i,column=1)

    #tablazat fejlec
    coln_i = 0
    for col_name in result[0]:
        tmpLabel = tk.Label(root, text=col_name)
        tmpLabel.grid(row=data_row, column=data_col + coln_i)
        labels.append(tmpLabel)
        coln_i += 1
    #tablazat sorai, adatai
    row_i = 0
    for row in result[1]:
        col_i=0
        for col in row:
            tmpLabel = tk.Label(root, text=col)
            tmpLabel.grid(row=data_row + 1 + row_i, column=data_col + col_i)
            tmpLabel.bind("<Button-1>", lambda e, l=tmpLabel: printSelected(l.grid_info()['row']))
            labels.append(tmpLabel)
            col_i+=1
        row_i += 1


def printSelected(selectedRow):
    global root, selectedRowData, selected_menu
    id = root.grid_slaves(selectedRow,data_col)[0]['text']
    print("selected row ID: ",str(id))
    selectedRowData = dao.querryOne(selected_menu, id)[0]
    print(selectedRowData)
    updateSelectedLabel()

def showEntries():
    for entry in entries:
        entry.destroy()


def show(menu):
    global selected_menu,selectedRowData
    selectedRowData=""
    selected_menu = menu
    showResult(dao.querry(menu))
    updateLabel()
    updateSelectedLabel()

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

def getUpdateSql():
    match selected_menu:
        case Tabla.ONELETRAJZ:
            return UPDATE_ONEL
        case Tabla.HIRDETESEK:
            return UPDATE_HIRD
        case Tabla.FELHASZNALO:
            return UPDATE_FELH
        case Tabla.MUNKAADO:
            return UPDATE_MUNK
        case Tabla.HIRDETESFELAD:
            return UPDATE_HIFE
        case Tabla.ALLASKERESO:
            return UPDATE_ALLA
        case Tabla.BIRTOKOL:
            return UPDATE_BIRT
        case Tabla.JELENTKEZES:
            return UPDATE_JELE
        case Tabla.SZAKMAK:
            return UPDATE_SZAK

def update():
    oldValue=dao.querryOne(selected_menu,selectedRowData[0])[0]
    values = []
    for entryIndex in range(len(entries)):
        if entries[entryIndex].get() == "":
            values.append(oldValue[entryIndex+1])
        else:
            values.append(entries[entryIndex].get())
    # ToDo: input ellenorzes
    values.append(oldValue[0])
    dao.update(getUpdateSql(),values)
    show(selected_menu)


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

def delRow(row):
    dao.delete(selected_menu,row)
    show(selected_menu)

def updateLabel():
    root.beszurLabel['text']="Jelen Tábla: "+ selected_menu.value + ", Adatbeszúrás:"

def updateSelectedLabel():
    if selectedRowData != "":
        root.delBtn = tk.Button(text="Törlés", width=buttons_width, command=lambda: delRow(selectedRowData[0]))
        root.delBtn.grid(row=2, column=4)
        root.UpdateBtn = tk.Button(text="Update", width=buttons_width, command=lambda: update())
        root.UpdateBtn.grid(row=2, column=5)
    elif root.delBtn:
        root.delBtn.destroy()
        root.UpdateBtn.destroy()
    root.selectedLabel['text']="Kiválasztott adat: " + str(selectedRowData)


root = tk.Tk()
root.title("Állásbörze")
root.geometry("1050x600")



beszur_btn = tk.Button(root)
root.beszurLabel = tk.Label(text="Jelen Tábla: "+ selected_menu.value + ", Adatbeszúrás:")
root.beszurLabel.grid(row=0, column=data_col, columnspan=3)
root.selectedLabel = tk.Label(text="Kiválasztott adat: " + selectedRowData)
root.selectedLabel.grid(row=1, column=data_col, columnspan=3)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Oneletrajzok",    command=lambda: show(Tabla.ONELETRAJZ))
filemenu.add_command(label="Hirdetesek",      command=lambda: show(Tabla.HIRDETESEK))
filemenu.add_command(label="Felhasznalo",     command=lambda: show(Tabla.FELHASZNALO))
filemenu.add_command(label="Munkaadó",        command=lambda: show(Tabla.MUNKAADO))
filemenu.add_command(label="HirdetesFeladas", command=lambda: show(Tabla.HIRDETESFELAD))
filemenu.add_command(label="Allaskereso",     command=lambda: show(Tabla.ALLASKERESO))
filemenu.add_command(label="Birtokol",        command=lambda: show(Tabla.BIRTOKOL))
filemenu.add_command(label="Jelentkezes",     command=lambda: show(Tabla.JELENTKEZES))
filemenu.add_command(label="Szakmak",         command=lambda: show(Tabla.SZAKMAK))
menubar.add_cascade(label="Táblák", menu=filemenu)
root.config(menu=menubar)


root.mainloop()

