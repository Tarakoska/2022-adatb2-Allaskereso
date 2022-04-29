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

INSERT_ONEL = "INSERT INTO Oneletrajzok (formatum) VALUES (:formatum)"
INSERT_HIRD = "INSERT INTO Hirdetesek (nev, leiras) VALUES (:nev, :leiras)"
INSERT_FELH = "INSERT INTO Felhasznalo (veznev, kernev, felhnev, jelszo, email, varos, utca, hazszam, telefon, isadmin) VALUES (:veznev, :kernev, :felhnev, :jelszo, :email, :varos, :utca, :hazszam, :telefon, :isadmin)"
INSERT_MUNK = "INSERT INTO Munkaado (beosztas, ertekeles, feid) VALUES (:beosztas, :ertekeles, :feid)"
INSERT_HIFE = "INSERT INTO HirdetesFeladas (muid) VALUES (:muid)"
INSERT_ALLA = "INSERT INTO Allaskereso (szulido, onid, feid) VALUES (TO_DATE(:szulido), :onid, :feid)"
INSERT_BIRT = "INSERT INTO Birtokol (szakid, allid) VALUES (:szakid, :allid)"
INSERT_JELE = "INSERT INTO Jelentkezes (allid, hiid) VALUES (:allid, :hiid)"
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