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



COL_NAME_SQL = "select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)= :table_name"

SELECT_ALL_ONEL = "select * from Oneletrajzok"
SELECT_ALL_HIRD = "select * from Hirdetesek"
SELECT_ALL_FELH = "select * from Felhasznalo"
SELECT_ALL_MUNK = "select * from Munkaado"
SELECT_ALL_HIFE = "select * from HirdetesFeladas"
SELECT_ALL_ALLA = "select * from Allaskereso"
SELECT_ALL_BIRT = "select * from Birtokol"
SELECT_ALL_JELE = "select * from Jelentkezes"
SELECT_ALL_SZAK = "select * from Szakmak"

INSERT_ONEL = "INSERT INTO Oneletrajzok (formatum) VALUES (:formatum)"
INSERT_HIRD = "INSERT INTO Hirdetesek (nev, leiras) VALUES (:nev, :leiras)"
INSERT_FELH = "INSERT INTO Felhasznalo (veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin) VALUES (:veznev, :kernev, :felhnev, :jelszo, :email, :varos, :utca, :hazszam, :telefon, :isadmin)"
INSERT_MUNK = "INSERT INTO Munkaado (beosztas, ertekeles, feid) VALUES (:beosztas, :ertekeles, :feid)"
INSERT_HIFE = "INSERT INTO HirdetesFeladas (muid) VALUES (:muid)"
INSERT_ALLA = "NSERT INTO Allaskereso (szulido, onid, feid) VALUES (TO_DATE(:szulido), :onid, :feid)"
INSERT_BIRT = "INSERT INTO Birtokol (szakid, allid) VALUES (:szakid, :allid)"
INSERT_JELE = "INSERT INTO Jelentkezes (allid, hiid) VALUES (:allid, :hiid)"
INSERT_SZAK = "INSERT INTO Szakmak (nev, leiras) VALUES (:nev, :leiras)"
