import cx_Oracle
DB_URL="SYSTEM/admin@192.168.0.17"
def querry(sql):
    try:
        con = cx_Oracle.connect(DB_URL)
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        return rows
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if con:
    #         con.close()

def oneletrajzokQuerry():
    querry('select * from Oneletrajzok')
def hirdetesekQuerry():
    querry('select * from Hirdetesek')
def felhasznaloQuerry():
    querry('select * from Felhasznalo')
def munkaAdoQuerry():
    querry('select * from Munkaado')
def hirdetesFeladasQuerry():
    querry('select * from HirdetesFeladas')
def allaskeresoQuerry():
    querry('select * from Allaskereso')
def birtokolQuerry():
    querry('select * from Birtokol')
def jelentkezesQuerry():
    querry('select * from Jelentkezes')
