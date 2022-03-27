import cx_Oracle
DB_URL="SYSTEM/admin@192.168.0.17/databasedemo"
def querry(sql):
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        cursor.execute(sql)
        return cursor
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))

def oneletrajzokQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'oneletrajzok\'')
    result = querry('select * from Oneletrajzok')
    return colnames,result
def hirdetesekQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'hirdetesek\'')
    result = querry('select * from Hirdetesek')
    return colnames, result
def felhasznaloQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'felhasznalo\'')
    result = querry('select * from Felhasznalo')
    return colnames, result
def munkaAdoQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'munkaado\'')
    result = querry('select * from Munkaado')
    return colnames,result
def hirdetesFeladasQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'hirdetesFeladas\'')
    result = querry('select * from HirdetesFeladas')
    return colnames, result
def allaskeresoQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'allaskereso\'')
    result = querry('select * from Allaskereso')
    return colnames, result
def birtokolQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'birtokol\'')
    result = querry('select * from Birtokol')
    return colnames, result
def jelentkezesQuerry():
    colnames = querry('select COLUMN_NAME FROM ALL_TAB_COLUMNS where LOWER(TABLE_NAME)=\'jelentkezes\'')
    result = querry('select * from Jelentkezes')
    return colnames, result

