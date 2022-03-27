import cx_Oracle
DB_URL="username/password@localhost"

def hirdetesekQuerry():
    try:
        con = cx_Oracle.connect(DB_URL)

        cursor = con.cursor()

        cursor.execute('select * from Hirdetesek')
        rows = cursor.fetchall()
        print(rows)
        return rows

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)
    except Exception as err:
        print("Error:"+str(err))

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
