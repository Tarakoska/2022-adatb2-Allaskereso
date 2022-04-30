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
    EZERMESTEREK = "Ezermesterek"

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
        "type":["text","text","text"]
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
    }
}

colnames = {
    Tabla.ONELETRAJZ: [],
    Tabla.HIRDETESEK: [],
    Tabla.FELHASZNALO: [],
    Tabla.MUNKAADO: [],
    Tabla.HIRDETESFELAD: [],
    Tabla.ALLASKERESO: [],
    Tabla.BIRTOKOL: [],
    Tabla.JELENTKEZES: [],
    Tabla.SZAKMAK: [],
    Tabla.EZERMESTEREK: ["Teljes név"]
}

COL_NAME_SQL = "select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)= :table_name"

INSERT_ONEL = "INSERT INTO Oneletrajzok (filenev,formatum) VALUES (:filenev,:formatum)"
INSERT_HIRD = "INSERT INTO Hirdetesek (nev, leiras) VALUES (:nev, :leiras)"
INSERT_FELH = "INSERT INTO Felhasznalo (veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin) VALUES (:veznev, :kernev, :felhnev, :jelszo, :email, :varos, :utca, :hazszam, :telefon, :isadmin)"
INSERT_MUNK = "INSERT INTO Munkaado (beosztas, ertekeles, feid) VALUES (:beosztas, :ertekeles, :feid)"
INSERT_HIFE = "INSERT INTO HirdetesFeladas (muid) VALUES (:muid)"
INSERT_ALLA = "INSERT INTO Allaskereso (szulido, onid, feid) VALUES (TO_DATE(:szulido,'RR-MON-DD'), :onid, :feid)"
INSERT_BIRT = "INSERT INTO Birtokol (szakid, allid) VALUES (:szakid, :allid)"
INSERT_JELE = "INSERT INTO Jelentkezes (mikor, allid, hiid) VALUES (SYSDATE,:allid, :hiid)"
INSERT_SZAK = "INSERT INTO Szakmak (nev, leiras) VALUES (:nev, :leiras)"


UPDATE_ONEL = "UPDATE Oneletrajzok SET formatum=:formatum where id= :id_input"
UPDATE_HIRD = "UPDATE hirdetesek SET nev=:nev_input, leiras=:leiras_input where id= :id_input"
UPDATE_FELH = "UPDATE Felhasznalo SET veznev= :veznev, kernev=:kernev, felhnev=:felhnev, jelszo=:jelszo, email=:email, varos=:varos, utca=:utca, hazszam=:hazszam, telefon=:telefon, isadmin=:isadmin where id= :id_input"
UPDATE_MUNK = "UPDATE Munkaado SET beosztas= :beosztas, ertekeles=:ertekeles, feid=:feid where id= :id_input"
UPDATE_HIFE = "UPDATE HirdetesFeladas SET muid=:muid where id= :id_input"
UPDATE_ALLA = "UPDATE Allaskereso SET szulido=TO_DATE(:szulido) , onid=:onid, feid=:feid where id= :id_input"
UPDATE_BIRT = "UPDATE Birtokol SET szakid=:szakid , allid=:allid where id= :id_input"
UPDATE_JELE = "UPDATE Jelentkezes SET allid=:allid , hiid=:hiid where id= :id_input"
UPDATE_SZAK = "UPDATE Szakmak SET nev=:nev , leiras=:leiras where id= :id_input"

DELETE_ONE = "delete from {usertable} where id=:id_input"
SELECT_ONE = "select * from {usertable} where id=:id_input"
SELECT_ALL = "select * from {usertable}"

EZERMESTEREK_SQL = "SELECT NEV FROM (SELECT (F.VEZNEV || ' ' || F.KERNEV) as NEV, COUNT(B.ALLID) as darab FROM ((ALLASKERESO A INNER JOIN FELHASZNALO F on F.ID = A.FEID) LEFT JOIN BIRTOKOL B on B.ALLID = A.ID) GROUP BY VEZNEV, KERNEV) WHERE darab > 0"