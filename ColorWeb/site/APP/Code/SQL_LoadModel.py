import sqlite3



def SaveLoadModelSql():
    conn = sqlite3.connect('DB/Data.db')
    conn.execute('''
                 CREATE TABLE LoadModel 
         (ID INTEGER PRIMARY KEY,
         name           TEXT    NOT NULL
         );''')
    

def AddLoadModelSql(name):
    try: 
        conn = sqlite3.connect('DB/Data.db')
        conn.execute(f"INSERT INTO  LoadModel (name) VALUES ('{name}' )")
    except:
        SaveLoadModelSql()
        conn = sqlite3.connect('DB/Data.db')
        conn.execute(
            f"INSERT INTO   LoadModel (name) VALUES ('{name}' )")
    conn.commit()
    conn.close()
    

def ShowLoadModel():
    conn = sqlite3.connect('DB/Data.db')
    cursor_obj = conn.cursor()

    cursor_obj.execute(
        f"SELECT * FROM LoadModel ORDER BY ID DESC")
    output = cursor_obj.fetchall()
    # for row in output:
    #     print(row)
    conn.commit()
    conn.close()
    return output[0]

