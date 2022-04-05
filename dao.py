import cx_Oracle
from var import *

DB_URL="SYSTEM/admin@localhost/databasedemo"


def selectAll(sql):
    global con, cursor
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))
    finally:
        cursor.close()
        con.close()

def selectAllColName(table_name):
    global con, cursor
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        cursor.execute(COL_NAME_SQL, table_name=table_name)
        ret = cursor.fetchall()
        return ret
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))
    finally:
        cursor.close()
        con.close()



def querry(tab_name):
    colnames = selectAllColName(tab_name.value)
    match tab_name:
        case Tabla.ONELETRAJZ:
            result = selectAll(SELECT_ALL_ONEL)
        case Tabla.HIRDETESEK:
            result = selectAll(SELECT_ALL_HIRD)
        case Tabla.FELHASZNALO:
            result = selectAll(SELECT_ALL_FELH)
        case Tabla.MUNKAADO:
            result = selectAll(SELECT_ALL_MUNK)
        case Tabla.HIRDETESFELAD:
            result = selectAll(SELECT_ALL_HIFE)
        case Tabla.ALLASKERESO:
            result = selectAll(SELECT_ALL_ALLA)
        case Tabla.BIRTOKOL:
            result = selectAll(SELECT_ALL_BIRT)
        case Tabla.JELENTKEZES:
            result = selectAll(SELECT_ALL_JELE)
        case Tabla.SZAKMAK:
            result = selectAll(SELECT_ALL_SZAK)
        case _:
            result = selectAll(SELECT_ALL_ONEL)

    return colnames, result

def insert(sql,values):
    global con, cursor
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        cursor.execute(sql,values)
        con.commit()
        return
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle: ", e)
    except Exception as err:
        print("Error:"+str(err))
    finally:
        cursor.close()
        con.close()