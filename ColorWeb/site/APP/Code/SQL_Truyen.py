import sqlite3



def SaveTruyenSql():
    conn = sqlite3.connect('DB/Data.db')
    conn.execute('''
                 CREATE TABLE Truyen 
         (ID INTEGER PRIMARY KEY,
         TenTruyen           TEXT    NOT NULL,
         NoiDung           TEXT    NOT NULL
         );''')
    

def AddTruyenSql(TenTruyen, NoiDung):
    try: 
        conn = sqlite3.connect('DB/Data.db')
        conn.execute(
            f"INSERT INTO Truyen (TenTruyen, NoiDung) VALUES ('{TenTruyen}', '{NoiDung}' )")
    except:
        SaveTruyenSql()
        conn = sqlite3.connect('DB/Data.db')
        conn.execute(
            f"INSERT INTO Truyen (TenTruyen, NoiDung) VALUES ('{TenTruyen}', '{NoiDung}' )")
    conn.commit()
    conn.close()
    

def ShowTruyen():
    conn = sqlite3.connect('DB/Data.db')
    cursor_obj = conn.cursor()

    cursor_obj.execute(
        f"SELECT * FROM Truyen ORDER BY ID DESC")
    output = cursor_obj.fetchall()
    # for row in output:
    #     print(row)
    conn.commit()
    conn.close()
    return output

