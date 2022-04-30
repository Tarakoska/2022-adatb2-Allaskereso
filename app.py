import tkinter as tk
from tkinter import messagebox
import dao
from var import *
from tksheet import Sheet

labels = []
entries = []

buttons_col=0
buttons_width=20
data_row=3
data_col=3

# default:
selected_menu=Tabla.FELHASZNALO
selectedRowData=""



def showResult(result):
    global beszur_btn, entries, labels, delete_btn,update_btn, selected_menu
    for label in labels:
        label.destroy()
    labels = []
    for entry in entries:
        entry.destroy()
    entries = []
    beszur_btn.destroy()
    delete_btn.destroy()
    update_btn.destroy()
    # input mezők

    for e in range(len(inputs[selected_menu]["type"])):
        tmpLabel = tk.Label(root, width=buttons_width, text=inputs[selected_menu]["label"][e] + ":")
        tmpLabel.grid(row=3 + len(entries), column=0)
        labels.append(tmpLabel)
        match inputs[selected_menu]["type"][e]:
            case "text":entry_txt = tk.Entry(root, width=buttons_width)
            case "password":entry_txt = tk.Entry(root, width=buttons_width,show="*")
            case "file":entry_txt = tk.Entry(root, width=buttons_width)
            case "checkbox":entry_txt = tk.Checkbutton(root,onvalue=1, offvalue=0,variable=chkboxvar)
        entry_txt.grid(row=3 + len(entries), column=1)
        entries.append(entry_txt)


    #Beszur gomb
    beszur_btn = tk.Button(root, text="Beszúr", width=buttons_width, command=insert)
    beszur_btn.grid(row=4+len(entries),column=1)
    update_btn = tk.Button(text="Update", width=buttons_width, command=lambda: update())
    update_btn.grid(row=4+len(entries) + 1, column=1)
    delete_btn = tk.Button(text="Törlés", width=buttons_width, command=lambda: delete())
    delete_btn.grid(row=4+len(entries) + 2, column=1)


    root.sheet.headers(newheaders=result[0])

    #tablazat sorai, adatai
    root.sheet.set_sheet_data(result[1], redraw=True)
    root.sheet.set_all_cell_sizes_to_text(redraw=True)



def show(menu):
    global selected_menu,selectedRowData
    selectedRowData=""
    selected_menu = menu
    showResult(dao.querry(menu))
    updateLabel()

def showSpec(menu):
    global selected_menu,selectedRowData
    selectedRowData=""
    selected_menu = ""
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

def delete():
    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    dao.delete(selected_menu,rowDataId)
    show(selected_menu)

def update():
    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0],0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    oldValue=dao.querryOne(selected_menu,rowDataId)[0]
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


def insertOneletrajzok():
    filename = entries[0].get()
    format = entries[1].get()
    values = [filename,format]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_ONEL,values)
    showResult(dao.querry(selected_menu))

def insertHirdetesek():
    nev = entries[0].get()
    leiras = entries[1].get()
    if nev == "" or leiras == "":
        errorPopup("Nem lehet üresen hagyott mező!")
        return
    values = [nev,leiras]
    dao.insert(INSERT_HIRD,values)
    showResult(dao.querry(selected_menu))

def insertFelhasznalo():
    veznev = entries[0].get()
    kernev = entries[1].get()
    felhnev = entries[2].get()
    jelszo = entries[3].get()
    jelszoujra = entries[4].get()
    if jelszo != jelszoujra:
        errorPopup("A két jelszó nem egyezik!")
        return
    email = entries[5].get()
    varos = entries[6].get()
    utca = entries[7].get()
    hazszam = entries[8].get()
    telefon = entries[9].get()
    isadmin = chkboxvar.get()
    values = [veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_FELH,values)
    showResult(dao.querry(selected_menu))

def insertMunkaado():
    beosztas = entries[0].get()
    ertekeles = entries[1].get()
    feid = entries[2].get()
    # ToDo: input ellenorzes
    values = [beosztas, ertekeles, feid]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_MUNK, values)
    showResult(dao.querry(selected_menu))

def insertHirdetesFeladas():
    errorPopup("Ide nem szúrhatsz be!")

def insertAllaskereso():
    szulido = entries[0].get()
    onid = entries[1].get()
    feid = entries[2].get()
    # ToDo: input ellenorzes
    values = [szulido, onid, feid]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_ALLA, values)
    showResult(dao.querry(selected_menu))

def insertBirtokol():
    szakid = entries[0].get()
    allid = entries[1].get()
    # ToDo: input ellenorzes
    values = [szakid, allid]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_BIRT, values)
    showResult(dao.querry(selected_menu))

def insertJelentkezes():
    allid = entries[0].get()
    hiid = entries[1].get()
    # ToDo: input ellenorzes
    values = [allid, hiid]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_JELE, values)
    showResult(dao.querry(selected_menu))

def insertSzakmak():
    nev = entries[0].get()
    leiras = entries[1].get()
    # ToDo: input ellenorzes
    values = [nev, leiras]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_SZAK, values)
    showResult(dao.querry(selected_menu))

def errorPopup(str):
   messagebox.showwarning("Hiba", str)

def updateLabel():
    root.beszurLabel['text']="Jelen Tábla: "+ selected_menu.value + ", Adatbeszúrás:"




root = tk.Tk()
root.title("Állásbörze")
root.geometry("1297x722")

root.frame = tk.Frame()
root.frame.grid_columnconfigure(0,weight=1)
root.frame.grid_rowconfigure(0,weight=1)
root.sheet = Sheet(root.frame,height = 700, width= 1000 ,show_row_index = False,show_y_scrollbar=True, expand_sheet_if_paste_too_big=True)
root.sheet.enable_bindings("row_select","column_width_resize", "rc_select","single_select")
root.frame.grid(row=data_row,column=data_col,sticky = "se", rowspan=40)
root.sheet.grid(row = 0, column = 0,sticky = "nswe")
root.sheet.set_all_cell_sizes_to_text(redraw = True)


beszur_btn = tk.Button(root)
update_btn = tk.Button(root)
delete_btn = tk.Button(root)

chkboxvar = tk.IntVar()

root.beszurLabel = tk.Label(text="Jelen Tábla: "+ selected_menu.value)
root.beszurLabel.grid(row=0, column=0, columnspan=2)


menubar = tk.Menu(root)
querrymenu = tk.Menu(menubar, tearoff=0)
querrymenu.add_command(label="Oneletrajzok", command=lambda: show(Tabla.ONELETRAJZ))
querrymenu.add_command(label="Hirdetesek", command=lambda: show(Tabla.HIRDETESEK))
querrymenu.add_command(label="Felhasznalo", command=lambda: show(Tabla.FELHASZNALO))
querrymenu.add_command(label="Munkaadó", command=lambda: show(Tabla.MUNKAADO))
querrymenu.add_command(label="HirdetesFeladas", command=lambda: show(Tabla.HIRDETESFELAD))
querrymenu.add_command(label="Allaskereso", command=lambda: show(Tabla.ALLASKERESO))
querrymenu.add_command(label="Birtokol", command=lambda: show(Tabla.BIRTOKOL))
querrymenu.add_command(label="Jelentkezes", command=lambda: show(Tabla.JELENTKEZES))
querrymenu.add_command(label="Szakmak", command=lambda: show(Tabla.SZAKMAK))
menubar.add_cascade(label="Táblák", menu=querrymenu)

specialquerrymenu = tk.Menu(menubar, tearoff=0)
specialquerrymenu.add_command(label="Ezermesterek", command=lambda: showSpec(Tabla.EZERMESTEREK))
menubar.add_cascade(label="Speciális", menu=specialquerrymenu)

root.config(menu=menubar)

show(selected_menu)
root.mainloop()

