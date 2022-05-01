import cx_Oracle
from var import *

DB_URL = "SYSTEM/admin@localhost/Allasborze"


def getCursor():
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        return con, cursor
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:" + str(err))



def destroyCursor(con, cursor):
    cursor.close()
    con.close()


def selectAll(sql):
    con, cursor = getCursor()
    print(sql)
    cursor.execute(sql)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def selectAllColName(table_name):
    con, cursor = getCursor()
    cursor.execute(COL_NAME_SQL, table_name=table_name)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def insert(sql, values):
    con, cursor = getCursor()
    cursor.execute(sql, values)
    con.commit()
    destroyCursor(con, cursor)


def update(sql, values):
    con, cursor = getCursor()
    cursor.execute(sql, values)
    con.commit()
    destroyCursor(con, cursor)


def selectOne(tab_name, id):
    sql = SELECT_ONE.format(usertable=tab_name.value)
    con, cursor = getCursor()
    cursor.execute(sql, id_input=id)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def querryOne(sql, data):
    con, cursor = getCursor()
    cursor.execute(sql, data)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def querryWithData(sql, data):
    con, cursor = getCursor()
    cursor.execute(sql, data)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def delete(tab_name, id):
    sql = DELETE_ONE.format(usertable=tab_name.value)
    con, cursor = getCursor()
    cursor.execute(sql, id_input=id)
    con.commit()
    destroyCursor(con, cursor)


def querry(tab_name):
    query = SELECT_ALL.format(usertable=tab_name.value)
    return colnames[tab_name], selectAll(query)


def querrySpec(tab_name, data=None):
    if data is None:
        data = []
    match tab_name:
        case Tabla.FRISS_JELENTKEZESEK:
            query = FRISS_JELENTKEZESEK_SQL
        case Tabla.LEGTOBB_LEHETOSEG:
            query = LEGTOBB_LEHETOSEG_SQL
        case Tabla.EZERMESTEREK:
            query = EZERMESTEREK_SQL
        case Tabla.LEGNEPSZERUBB_SZAKMAK:
            query = LEGNEPSZERUBB_SZAKMAK_SQL
        case Tabla.MEGFELELO_ALLASOK:
            query = MEGFELELO_SZAKMAK_SQL
        case Tabla.LEGKIVANTABB_ALLAS:
            query = LEGKIVANTABB_ALLAS_SQL
        case Tabla.LEGFIATALABB:
            query = LEGFIATALABB_SQL
        case Tabla.SQL_8:
            query = SQL_8_SQL
        case Tabla.SQL_9:
            query = SQL_8_SQL

    return colnames[tab_name], querryWithData(query, data)
