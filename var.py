from enum import Enum


class Tabla(Enum):
    ONELETRAJZ = "oneletrajzok"
    HIRDETESEK = "hirdetesek"
    FELHASZNALO = "felhasznalo"
    MUNKAADO = "munkaado"
    HIRDETESFELAD = "hirdetesfeladas"
    ALLASKERESO = "allaskereso"
    BIRTOKOL = "birtokol"
    JELENTKEZES = "jelentkezes"
    SZAKMAK = "szakmak"
    FRISS_JELENTKEZESEK = "Friss Jelentkezések"
    LEGTOBB_LEHETOSEG = "Legtöbb lehetőséget kínáló munkaadó"
    EZERMESTEREK = "Ezermesterek"
    LEGNEPSZERUBB_SZAKMAK = "Legnépszerűbb szakmák"
    MEGFELELO_ALLASOK = "Megfeleő Állások"
    LEGKIVANTABB_ALLAS = "Legtöbben megpályázott állások"
    LEGFIATALABB = "Legfiatalabb munkakeresőnk"
    SQL_8 = "sql8"
    SQL_9 = "sql9"
    LOGIN = "Bejelentkezés"

inputs = {
    Tabla.ONELETRAJZ: {
        "label": ["Fájl"],
        "type":["file"]
    },
    Tabla.HIRDETESEK: {
        "label": ["Név", "Leírás"],
        "type": ["text", "text"]
    },
    Tabla.FELHASZNALO: {
        "label": ["Vezetéknév", "Keresztnév","Felhasználónév","Jelszó","Jelszó újra","Email cím","Település","Utca","Házszám","Telefon szám","Admin"],
        "type": ["text", "text","text","password","password","text","text","text","text","text","checkbox"]
    },
    Tabla.MUNKAADO: {
        "label": ["Beosztás","Értékelés","Felhasználó id"],
        "type": ["text","text","text"]
    },
    Tabla.HIRDETESFELAD: {
        "label": [],
        "type": []
    },
    Tabla.ALLASKERESO: {
        "label": ["Születési idő","Önéletrajz id","Felhasználó id"],
        "type":["date","text","text"]
    },
    Tabla.BIRTOKOL: {
        "label": ["Szakma id","Álláskereső id"],
        "type":["text","text"]
    },
    Tabla.JELENTKEZES: {
        "label": ["Álláskereső id", "Hirdetés id"],
        "type":["text","text"]
    },
    Tabla.SZAKMAK: {
        "label": ["Név","Leírás"],
        "type":["text","text"]
    },
    Tabla.FRISS_JELENTKEZESEK: {
        "label": [],
        "type": []
    },
    Tabla.LEGTOBB_LEHETOSEG: {
        "label": [],
        "type": []
    },
    Tabla.EZERMESTEREK: {
        "label": [],
        "type": []
    },
    Tabla.LEGNEPSZERUBB_SZAKMAK: {
        "label": [],
        "type": []
    },
    Tabla.MEGFELELO_ALLASOK: {
        "label": [],
        "type": []
    },
    Tabla.LEGKIVANTABB_ALLAS: {
        "label": [],
        "type": []
    },
    Tabla.LEGFIATALABB: {
        "label": [],
        "type": []
    },
    Tabla.SQL_8: {
        "label": [],
        "type": []
    },
    Tabla.SQL_9: {
        "label": [],
        "type": []
    },
    Tabla.LOGIN: {
        "label": ["Felhasználónév", "Jelszó"],
        "type": ["text", "password"]
    }
}
colnames = {
    Tabla.ONELETRAJZ: ["Id","Fájlnév","Kiterjesztés"],
    Tabla.HIRDETESEK: ["Id","Hirdetés cím","Leírása"],
    Tabla.FELHASZNALO: ["Id","Vezetéknév", "Keresztnév","Felhasználónév","Jelszó","Email cím","Település","Utca","Házszám","Telefon szám","Admin-e"],
    Tabla.MUNKAADO: ["Id","Beosztása","Értékelése","Felhasználói azonosító"],
    Tabla.HIRDETESFELAD: ["Id","Hirdetés feladás ideje","Munka adó azonosító"],
    Tabla.ALLASKERESO: ["Id","Születési idő","Önéletrajz Id","Felhasználói azonosító"],
    Tabla.BIRTOKOL: ["Szakma azonosító","Álláskereső azonosító"],
    Tabla.JELENTKEZES: ["Id","Jelentkezés ideje","Álláskereső azonosító","Hirdetés azonosító"],
    Tabla.SZAKMAK: ["Id","Szakam neve","Leírása"],
    Tabla.FRISS_JELENTKEZESEK: ["Teljes név"],
    Tabla.LEGTOBB_LEHETOSEG: ["Felhasználónév"],
    Tabla.EZERMESTEREK: ["Teljes név"],
    Tabla.LEGNEPSZERUBB_SZAKMAK: ["Szakma","Darabszám"],
    Tabla.MEGFELELO_ALLASOK: ["Hirdetés azonosító","Hirdetés Cím"],
    Tabla.LEGKIVANTABB_ALLAS: ["Hirdetés cím","Leírás","Jelentkezők száma"],
    Tabla.LEGFIATALABB: ["Vezetéknév", "Keresztnév","Felhasználónév","Email cím","Település","Utca","Házszám","Telefon szám","Születési idő"],
    Tabla.SQL_8: [],
    Tabla.SQL_9: []
}


COL_NAME_SQL = "select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)= :table_name"

INSERT_ONEL = "INSERT INTO Oneletrajzok (filenev,formatum) VALUES (:filenev,:formatum)"
INSERT_HIRD = "INSERT INTO Hirdetesek (nev, leiras) VALUES (:nev, :leiras)"
INSERT_FELH = "INSERT INTO Felhasznalo (veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin) VALUES (:veznev, :kernev, :felhnev, :jelszo, :email, :varos, :utca, :hazszam, :telefon, :isadmin)"
INSERT_MUNK = "INSERT INTO Munkaado (beosztas, ertekeles, feid) VALUES (:beosztas, :ertekeles, :feid)"
INSERT_HIFE = "INSERT INTO HirdetesFeladas (muid) VALUES (:muid)"
INSERT_ALLA = "INSERT INTO Allaskereso (szulido, onid, feid) VALUES (TO_DATE(:szulido,'YYYY-MM-DD'), :onid, :feid)"
INSERT_BIRT = "INSERT INTO Birtokol (szakid, allid) VALUES (:szakid, :allid)"
INSERT_JELE = "INSERT INTO Jelentkezes (mikor, allid, hiid) VALUES (SYSDATE,:allid, :hiid)"
INSERT_SZAK = "INSERT INTO Szakmak (nev, leiras) VALUES (:nev, :leiras)"


UPDATE_ONEL = "UPDATE Oneletrajzok SET formatum=:formatum where id= :id_input"
UPDATE_HIRD = "UPDATE hirdetesek SET nev=:nev_input, leiras=:leiras_input where id= :id_input"
UPDATE_FELH = "UPDATE Felhasznalo SET veznev= :veznev, kernev=:kernev, felhnev=:felhnev, jelszo=:jelszo, email=:email, varos=:varos, utca=:utca, hazszam=:hazszam, telefon=:telefon, isadmin=:isadmin where id= :id_input"
UPDATE_MUNK = "UPDATE Munkaado SET beosztas= :beosztas, ertekeles=:ertekeles, feid=:feid where id= :id_input"
UPDATE_HIFE = "UPDATE HirdetesFeladas SET muid=:muid where id= :id_input"
UPDATE_ALLA = "UPDATE Allaskereso SET onid=:onid where id= :id_input"
UPDATE_BIRT = "UPDATE Birtokol SET szakid=:szakid , allid=:allid where id= :id_input"
UPDATE_JELE = "UPDATE Jelentkezes SET hiid=:hiid where id= :id_input"
UPDATE_SZAK = "UPDATE Szakmak SET nev=:nev , leiras=:leiras where id= :id_input"

DELETE_ONE = "delete from {usertable} where id=:id_input"
SELECT_ONE = "select * from {usertable} where id=:id_input"
SELECT_ALL = "select * from {usertable}"
SELECT_ONE_login = "select * from felhasznalo where felhnev=:felhnev_input"
SELECT_ONE_allaskereso = "select * from Allaskereso where feid=:feid_input"
SELECT_ONE_munkaado = "select * from Munkaado where feid=:feid_input"
SELECT_ONE_hirdetes = "select * from hirdetesek where id=:id_input"
SELECT_ONE_szakma = "select * from Szakmak where id=:id_input"

# -- 24 órán belül jelentkezett valamilyen állásra álláskeresők neve
FRISS_JELENTKEZESEK_SQL = "SELECT (VEZNEV || ' ' || KERNEV) as NEV FROM ((ALLASKERESO A INNER JOIN FELHASZNALO F ON F.ID = A.FEID) INNER JOIN JELENTKEZES J ON J.ALLID = A.ID) WHERE J.MIKOR > CURRENT_TIMESTAMP - interval '1' day"
# -- Munkaadók felhasználóneve legalább 2 hírdetéssel
LEGTOBB_LEHETOSEG_SQL = "SELECT FELHNEV FROM (SELECT FELHNEV, COUNT(H.ID) as darab FROM ((MUNKAADO M INNER JOIN FELHASZNALO F on F.ID = M.FEID) LEFT JOIN HIRDETESFELADAS H ON H.MUID = M.ID) GROUP BY FELHNEV) WHERE darab > 1"
# -- Álláskeresők neve legalább 1 szakmával
EZERMESTEREK_SQL = "SELECT NEV FROM (SELECT (F.VEZNEV || ' ' || F.KERNEV) as NEV, COUNT(B.ALLID) as darab FROM ((ALLASKERESO A INNER JOIN FELHASZNALO F on F.ID = A.FEID) LEFT JOIN BIRTOKOL B on B.ALLID = A.ID) GROUP BY VEZNEV, KERNEV) WHERE darab > 0"
# -- Legnépszerűbb szakmák
LEGNEPSZERUBB_SZAKMAK_SQL = "SELECT NEV, COUNT(B.ALLID) as DARAB FROM SZAKMAK SZ INNER JOIN BIRTOKOL B on SZ.ID = B.SZAKID GROUP BY NEV ORDER BY DARAB DESC"
# -- Felhasználónak megfelelő szakmák. KELL BELE ID
MEGFELELO_SZAKMAK_SQL = "SELECT H.ID,H.NEV FROM HIRDETESEK H INNER JOIN SZAKMAK SZ ON LOWER(H.NEV) = LOWER(SZ.NEV) INNER JOIN BIRTOKOL B on SZ.ID = B.SZAKID INNER JOIN ALLASKERESO A on B.ALLID = A.ID WHERE A.FEID = :id"
# -- Hírdetés a legtöbb jelentkezővel
LEGKIVANTABB_ALLAS_SQL = "SELECT * FROM (SELECT NEV, LEIRAS, MAX(J.ID) as JELENTKEZOK FROM HIRDETESEK H INNER JOIN JELENTKEZES J on H.ID = J.HIID GROUP BY NEV, LEIRAS) ORDER BY JELENTKEZOK DESC"
# -- A legfiatalabb álláskereső
LEGFIATALABB_SQL = "SELECT VEZNEV, KERNEV, FELHNEV, EMAIL, VAROS, UTCA, HAZSZAM, TELEFON, MAX(A.SZULIDO) as SZULETESI_IDO FROM ALLASKERESO A INNER JOIN FELHASZNALO F on A.FEID = F.ID WHERE SZULIDO = (SELECT MAX(SZULIDO) from ALLASKERESO) GROUP BY VEZNEV, KERNEV, FELHNEV, EMAIL, VAROS, UTCA, HAZSZAM, TELEFON"

SQL_8_SQL = ""

SQL_9_SQL = ""