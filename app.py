import tkinter as tk
from tkinter import messagebox
import dao
from var import *
from tksheet import Sheet

labels = []
entries = []

buttons_col = 0
buttons_width = 20
data_row = 3
data_col = 3

# default:
selected_menu = Tabla.FELHASZNALO
selectedRowData = ""

user = []


def megfeleloAllasok():
    global selected_menu, selectedRowData
    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    selectedRowData = ""
    selected_menu = Tabla.MEGFELELO_ALLASOK
    showResult(dao.querrySpec(selected_menu, rowDataId))
    updateLabel()


def showLogin():
    global selected_menu
    clean()
    selected_menu = Tabla.LOGIN
    updateLabel()
    showInputs()
    root.login_btn = tk.Button(root, text="Bejelentkezés", width=buttons_width, command=login)
    root.login_btn.grid(row=4 + len(entries), column=1)


def login():
    global user
    felhnev = entries[0].get()
    passwd = entries[1].get()
    values = [felhnev, passwd]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    testuser = dao.querryWithData(SELECT_ONE_login, [felhnev])
    print(testuser)
    if len(testuser) == 0:
        errorPopup("Nincs ilyen felhasználó!")
        return
    if passwd != testuser[0][4]:
        errorPopup("Jelszó nem helyes!")
        return
    print("User logged in:" + str(testuser))
    user = testuser[0]
    root.loginLabel['text'] = user[3]


def showInputs():
    for e in range(len(inputs[selected_menu]["type"])):
        tmpLabel = tk.Label(root, width=buttons_width, text=inputs[selected_menu]["label"][e] + ":")
        tmpLabel.grid(row=data_row + len(entries), column=0)
        labels.append(tmpLabel)
        match inputs[selected_menu]["type"][e]:
            case "text":
                input = tk.Entry(root, width=buttons_width)
                input.grid(row=data_row + len(entries), column=1)
                entries.append(input)
            case "password":
                input = tk.Entry(root, width=buttons_width, show="*")
                input.grid(row=data_row + len(entries), column=1)
                entries.append(input)
            case "file":
                input = tk.Entry(root, width=buttons_width)
                input.grid(row=data_row + len(entries), column=1)
                entries.append(input)
            case "checkbox":
                input = tk.Checkbutton(root, onvalue=1, offvalue=0, variable=root.chkboxvar)
                input.grid(row=data_row + len(entries), column=1)
                entries.append(input)
            case "date":
                ev = tk.Spinbox(root, from_=1900, to=2004, wrap=True)
                ev.grid(row=data_row + len(entries), column=1)
                tmpLabel = tk.Label(root, width=buttons_width, text="Születési év:")
                tmpLabel.grid(row=data_row + len(entries), column=0)
                labels.append(tmpLabel)
                entries.append(ev)

                honap = tk.Spinbox(root, from_=1, to=12, wrap=True)
                honap.grid(row=data_row + len(entries), column=1)
                tmpLabel = tk.Label(root, width=buttons_width, text="Születési hónap:")
                tmpLabel.grid(row=data_row + len(entries), column=0)
                labels.append(tmpLabel)
                entries.append(honap)

                nap = tk.Spinbox(root, from_=1, to=31, wrap=True)
                nap.grid(row=data_row + len(entries), column=1)
                tmpLabel = tk.Label(root, width=buttons_width, text="Születési nap:")
                tmpLabel.grid(row=data_row + len(entries), column=0)
                labels.append(tmpLabel)
                entries.append(nap)


def showResult(result):
    global entries, labels, selected_menu

    # input mezők
    showInputs()

    # Beszur gomb
    root.beszur_btn = tk.Button(root, text="Beszúr", width=buttons_width, command=insert)
    root.beszur_btn.grid(row=4 + len(entries), column=1)
    root.update_btn = tk.Button(text="Update", width=buttons_width, command=lambda: update())
    root.update_btn.grid(row=4 + len(entries) + 1, column=1)
    root.delete_btn = tk.Button(text="Törlés", width=buttons_width, command=lambda: delete())
    root.delete_btn.grid(row=4 + len(entries) + 2, column=1)

    if selected_menu == Tabla.FELHASZNALO:
        root.special_btn = tk.Button(text="Elérhető állások", width=buttons_width, command=lambda: megfeleloAllasok())
        root.special_btn.grid(row=4 + len(entries) + 3, column=1)

    root.sheet.headers(newheaders=result[0])

    # tablazat sorai, adatai
    root.sheet.set_sheet_data(result[1], redraw=True)
    root.sheet.set_all_cell_sizes_to_text(redraw=True)


def clean():
    global selected_menu, selectedRowData, labels, entries
    if selected_menu == Tabla.LOGIN:
        root.login_btn.destroy()
    selectedRowData = ""
    for label in labels:
        label.destroy()
    labels = []
    for entry in entries:
        entry.destroy()
    entries = []
    root.beszur_btn.destroy()
    root.delete_btn.destroy()
    root.update_btn.destroy()

    if selected_menu == Tabla.FELHASZNALO:
        root.special_btn.destroy()


def show(menu):
    global selected_menu
    clean()
    selected_menu = menu
    showResult(dao.querry(menu))
    updateLabel()


def showSpec(menu):
    global selected_menu
    clean()
    selected_menu = menu
    showResult(dao.querrySpec(menu))
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


def update():
    match selected_menu:
        case Tabla.ONELETRAJZ:
            return UPDATE_ONEL
        case Tabla.HIRDETESEK:
            updateHirdetesek()
        case Tabla.FELHASZNALO:
            updateFelhasznalo()
        case Tabla.MUNKAADO:
            updateMunkaado()
        case Tabla.HIRDETESFELAD:
            return UPDATE_HIFE
        case Tabla.ALLASKERESO:
            updateAllaskereso()
        case Tabla.BIRTOKOL:
            upadteBirtokol()
        case Tabla.JELENTKEZES:
            updateJelentkezes()
        case Tabla.SZAKMAK:
            return UPDATE_SZAK


def delete():
    if loginRequired(): return
    if root.sheet.anything_selected():
        rowDataId = int(root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0))
        if type(rowDataId) != type(2):
            errorPopup("Nem törölhetsz itt!")
            return
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return

    dao.delete(selected_menu, rowDataId)
    show(selected_menu)


def insertOneletrajzok():
    filename = entries[0].get()
    format = entries[1].get()
    values = [filename, format]
    if noEmpty(values): return 
    dao.insert(INSERT_ONEL, values)
    show(selected_menu)


def insertHirdetesek():
    if loginRequired(): return
    if needMunkaadoProfile(): return 

    nev = entries[0].get()
    leiras = entries[1].get()
    values = [nev, leiras]
    if noEmpty(values): return 
    dao.insert(INSERT_HIRD, values)
    show(selected_menu)


def updateHirdetesek():
    if loginRequired(): return
    if needMunkaadoProfile(): return 

    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return

    print(rowDataId)
    oldValue = dao.selectOne(selected_menu, rowDataId)[0]
    nev = entries[0].get()
    leiras = entries[1].get()
    values = [nev, leiras]
    for v in range(len(values)):
        if values[v] == "":
            values[v] = oldValue[v + 1]
    values.append(oldValue[0])
    print(values)
    dao.insert(UPDATE_HIRD, values)
    show(selected_menu)


def updateFelhasznalo():
    if loginRequired(): return

    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    print(rowDataId)
    if sameUserRequired(rowDataId): return

    oldValue = dao.selectOne(selected_menu, rowDataId)[0]

    # ToDO: regisztráció except oracle trigger error handling
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
    isadmin = root.chkboxvar.get()
    values = [veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin]
    for v in range(len(values)):
        if values[v] == "":
            values[v] = oldValue[v + 1]

    values.append(oldValue[0])
    print(values)
    dao.update(UPDATE_FELH, values)
    show(selected_menu)


def insertFelhasznalo():
    # ToDO: regisztráció except oracle trigger error handling
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
    isadmin = root.chkboxvar.get()
    values = [veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin]
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return
    dao.insert(INSERT_FELH, values)
    show(selected_menu)


def insertMunkaado():
    global user
    if loginRequired(): return
    munkaadoprof = dao.querryWithData(SELECT_ONE_munkaado, [user[0]])
    if len(munkaadoprof) == 1:
        errorPopup("Már regisztráltál álláskeresőként")
        return
    
    beosztas = entries[0].get()
    ertekeles = entries[1].get()
    feid = user[0]

    values = [beosztas, ertekeles, feid]
    if noEmpty(values): return 
    dao.insert(INSERT_MUNK, values)
    show(selected_menu)


def updateMunkaado():
    if loginRequired(): return
    if needMunkaadoProfile(): return 

    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    print(rowDataId)
    oldValue = dao.selectOne(selected_menu, rowDataId)[0]

    beosztas = entries[0].get()
    ertekeles = entries[1].get()

    feid = entries[2].get()
    values = [beosztas, ertekeles, feid]

    for v in range(len(values)):
        if values[v] == "":
            values[v] = oldValue[v + 1]

    values.append(oldValue[0])
    print(values)
    dao.update(UPDATE_MUNK, values)
    show(selected_menu)


def insertHirdetesFeladas():
    # ToDo:
    errorPopup("Ide nem szúrhatsz be!")


def insertAllaskereso():
    global user
    if loginRequired(): return
    allkerprof = dao.querryWithData(SELECT_ONE_allaskereso, [user[0]])
    if len(allkerprof) == 1:
        errorPopup("Már regisztráltál álláskeresőként")
        return
    szulev = int(entries[0].get())
    szulho = int(entries[1].get())
    szulnap = int(entries[2].get())
    szulido = f"{szulev}-{szulho:02}-{szulnap:02}"
    print("Szulidő:'" + szulido + "'")
    onid = entries[3].get()
    feid = user[0]

    values = [szulido, onid, feid]
    if noEmpty(values): return 
    dao.insert(INSERT_ALLA, values)
    show(selected_menu)


def updateAllaskereso():
    if len(user)==0:
        errorPopup("Jelentkezz be először!")
        return

    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    print(rowDataId)
    oldValue = dao.selectOne(selected_menu, rowDataId)[0]

    onid = entries[3].get()

    values = [onid]
    for v in range(len(values)):
        if values[v] == "":
            values[v] = oldValue[v + 1]

    values.append(oldValue[0])
    print(values)
    dao.update(UPDATE_ALLA, values)
    show(selected_menu)


def insertBirtokol():
    global user
    if loginRequired(): return
    if needAllaskeresoProfile():
        return
    
    allkerprof = dao.querryWithData(SELECT_ONE_allaskereso, [user[0]])
    szakid = entries[0].get()
    allid = allkerprof[0][0]

    szakma = dao.querryWithData(SELECT_ONE_szakma, [szakid])
    if len(szakma) == 0:
        errorPopup("Nincs ilyen szakma")
        return

    values = [szakid, allid]
    if noEmpty(values): return
    dao.insert(INSERT_BIRT, values)
    show(selected_menu)


#     ToDO teszt
def upadteBirtokol():
    if loginRequired(): return

    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    print(rowDataId)
    oldValue = dao.selectOne(selected_menu, rowDataId)[0]

    szakid = entries[0].get()

    values = [szakid]
    if szakid == "":
        szakid = oldValue[0]

    values.append(oldValue[1])
    print(values)
    dao.update(UPDATE_ALLA, values)
    show(selected_menu)


def insertJelentkezes():
    global user
    if loginRequired(): return
    if needAllaskeresoProfile(): return 
    
    allkerprof = dao.querryWithData(SELECT_ONE_allaskereso, [user[0]])
    allid = allkerprof[0][0]
    hiid = entries[1].get()

    hirdetes = dao.querryWithData(SELECT_ONE_hirdetes, [hiid])
    if len(hirdetes)==0:
        errorPopup("Nincs ilyen hirdetés")
        return

    values = [allid, hiid]
    if noEmpty(values): return 
    dao.insert(INSERT_JELE, values)
    show(selected_menu)


def updateJelentkezes():
    if loginRequired(): return
    if needAllaskeresoProfile(): return 


    if root.sheet.anything_selected():
        rowDataId = root.sheet.get_cell_data(root.sheet.get_currently_selected()[0], 0)
        print(rowDataId)
    else:
        errorPopup("Vállasz ki egy sor elöször!")
        return
    print(rowDataId)
    oldValue = dao.selectOne(selected_menu, rowDataId)[0]

    hiid = entries[1].get()

    hirdetes = dao.querryWithData(SELECT_ONE_hirdetes, [hiid])
    if len(hirdetes) == 0:
        errorPopup("Nincs ilyen hirdetés")
        return

    values = [hiid]

    if hiid == "":
        hiid = oldValue[3]

    values.append(oldValue[0])
    print(values)
    dao.update(UPDATE_MUNK, values)
    show(selected_menu)


def insertSzakmak():
    if loginRequired(): return
    if adminRequired(): return
    nev = entries[0].get()
    leiras = entries[1].get()
    values = [nev, leiras]
    if noEmpty(values): return 
    dao.insert(INSERT_SZAK, values)
    show(selected_menu)


def upadteSzakmak():
    if loginRequired(): return
    if adminRequired(): return
    nev = entries[0].get()
    leiras = entries[1].get()
    values = [nev, leiras]
    if noEmpty(values): return 
    dao.insert(INSERT_SZAK, values)
    show(selected_menu)


def errorPopup(str):
    messagebox.showwarning("Hiba", str)


def updateLabel():
    root.beszurLabel['text'] = "Jelen Tábla: " + selected_menu.value


def noEmpty(values):
    for v in values:
        if v == "":
            errorPopup("Nem lehet üresen hagyott mező!")
            return True
    return False


def loginRequired():
    if len(user)==0:
        errorPopup("Jelentkezz be elöször!")
        return True
    return False


def needAllaskeresoProfile():
    allkerprof = dao.querryWithData(SELECT_ONE_allaskereso, [user[0]])
    if len(allkerprof) == 0 and user[10] != 1:
        errorPopup("Regisztrálj álláskeresőként először!")
        return True
    return False


def needMunkaadoProfile():
    munkaadoprof = dao.querryWithData(SELECT_ONE_munkaado, [user[0]])
    if len(munkaadoprof) == 0 and user[10] != 1:
        errorPopup("Regisztrálj cégként először!")
        return True
    return False


def sameUserRequired(rowDataId):
    if rowDataId != user[0]:
        errorPopup("Csak a saját profilod szerkesztheted!")
        return True
    return False

def adminRequired():
    if user[10] == "0":
        errorPopup("Ezt a műveletet csak admin tudja végrehajtani!")
        return True
    return False


root = tk.Tk()
root.title("Állásbörze")
root.geometry("1297x722")

root.frame = tk.Frame()
root.frame.grid_columnconfigure(0, weight=1)
root.frame.grid_rowconfigure(0, weight=1)
root.sheet = Sheet(root.frame, height=700, width=1000, show_row_index=False, show_y_scrollbar=True,
                   expand_sheet_if_paste_too_big=True)
root.sheet.enable_bindings("row_select", "column_width_resize", "rc_select", "single_select")
root.frame.grid(row=data_row, column=data_col, sticky="se", rowspan=40)
root.sheet.grid(row=0, column=0, sticky="nswe")
root.sheet.set_all_cell_sizes_to_text(redraw=True)

root.beszur_btn = tk.Button(root)
root.update_btn = tk.Button(root)
root.delete_btn = tk.Button(root)
root.special_btn = tk.Button(root)
root.login_btn = tk.Button(root)

root.chkboxvar = tk.IntVar()

root.beszurLabel = tk.Label(text="Jelen Tábla: " + selected_menu.value)
root.beszurLabel.grid(row=0, column=data_col, columnspan=2)
bejLabel = tk.Label(text="Bejelentkezve:")
bejLabel.grid(row=0, column=0)
root.loginLabel = tk.Label(text="")
root.loginLabel.grid(row=0, column=1)

menubar = tk.Menu(root)
querrymenu = tk.Menu(menubar, tearoff=0)
querrymenu.add_command(label="Bejelentkezés", command=lambda: showLogin())
querrymenu.add_command(label="Önéletrajzok", command=lambda: show(Tabla.ONELETRAJZ))
querrymenu.add_command(label="Hirdetések", command=lambda: show(Tabla.HIRDETESEK))
querrymenu.add_command(label="Felhasználók", command=lambda: show(Tabla.FELHASZNALO))
querrymenu.add_command(label="Munkaadók", command=lambda: show(Tabla.MUNKAADO))
querrymenu.add_command(label="HirdetesFeladások", command=lambda: show(Tabla.HIRDETESFELAD))
querrymenu.add_command(label="Álláskeresők", command=lambda: show(Tabla.ALLASKERESO))
querrymenu.add_command(label="Birtokol", command=lambda: show(Tabla.BIRTOKOL))
querrymenu.add_command(label="Jelentkezések", command=lambda: show(Tabla.JELENTKEZES))
querrymenu.add_command(label="Szakmák", command=lambda: show(Tabla.SZAKMAK))
menubar.add_cascade(label="Táblák", menu=querrymenu)

specialquerrymenu = tk.Menu(menubar, tearoff=0)
specialquerrymenu.add_command(label=Tabla.FRISS_JELENTKEZESEK.value,
                              command=lambda: showSpec(Tabla.FRISS_JELENTKEZESEK))
specialquerrymenu.add_command(label=Tabla.LEGTOBB_LEHETOSEG.value, command=lambda: showSpec(Tabla.LEGTOBB_LEHETOSEG))
specialquerrymenu.add_command(label=Tabla.EZERMESTEREK.value, command=lambda: showSpec(Tabla.EZERMESTEREK))
specialquerrymenu.add_command(label=Tabla.LEGNEPSZERUBB_SZAKMAK.value,
                              command=lambda: showSpec(Tabla.LEGNEPSZERUBB_SZAKMAK))
specialquerrymenu.add_command(label=Tabla.LEGKIVANTABB_ALLAS.value, command=lambda: showSpec(Tabla.LEGKIVANTABB_ALLAS))
specialquerrymenu.add_command(label=Tabla.LEGFIATALABB.value, command=lambda: showSpec(Tabla.LEGFIATALABB))
specialquerrymenu.add_command(label=Tabla.SQL_8.value, command=lambda: showSpec(Tabla.SQL_8))
specialquerrymenu.add_command(label=Tabla.SQL_9.value, command=lambda: showSpec(Tabla.SQL_9))
menubar.add_cascade(label="Speciális", menu=specialquerrymenu)

root.config(menu=menubar)

show(selected_menu)
root.mainloop()
