import cx_Oracle
from var import *

DB_URL="SYSTEM/admin@localhost/Allasborze"


def getCursor():
    global con, cursor
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        return con, cursor
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))
    finally:
        if cursor in globals() or cursor in locals():
            cursor.close()
        if con in globals() or con in locals():
            con.close()

def destroyCursor(con, cursor):
    cursor.close()
    con.close()


def selectAll(sql):
    con, cursor = getCursor()
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


def insert(sql,values):
    con, cursor = getCursor()
    cursor.execute(sql,values)
    con.commit()
    destroyCursor(con, cursor)

def update(sql,values):
    con, cursor = getCursor()
    cursor.execute(sql,values)
    con.commit()
    destroyCursor(con, cursor)


def querryOne(tab_name,id):
    sql = SELECT_ONE.format(usertable=tab_name.value)
    con, cursor = getCursor()
    cursor.execute(sql, id_input=id)
    ret = cursor.fetchall()
    destroyCursor(con, cursor)
    return ret


def delete(tab_name,id):
    sql = DELETE_ONE.format(usertable=tab_name.value)
    con, cursor = getCursor()
    cursor.execute(sql,id_input=id)
    con.commit()
    destroyCursor(con, cursor)

def querry(tab_name):
    colnames = selectAllColName(tab_name.value)
    query = SELECT_ALL.format(usertable=tab_name.value)
    return colnames,selectAll(query)

def querrySpec(tab_name):
    match tab_name:
        case Tabla.EZERMESTEREK:query = EZERMESTEREK_SQL
    return colnames[tab_name],selectAll(query)


