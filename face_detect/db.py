import sqlite3
import numpy as np

def incert(Name, arr):
    """ insert data into DB"""
    con = sqlite3.connect("some.db")
    cur = con.cursor()
    # cur.execute("create table test (idx int primary key, Enc varchar);")
    cur.execute("insert into test (idx, Enc) values (?,?)",(Name, arr))
    con.commit()
    con.close()
def read():
    """Read from DB"""

    if __name__ == "__main__":                      #This is module to test, if module start without
        con = sqlite3.connect("some.db")            #All programm - use 1-t dir
    else:                                           #else
        con = sqlite3.connect("face_detect/some.db")#second, with full path
    cur = con.cursor()
    cur.execute("select Enc from test")
    data = cur.fetchall()

    data = np.fromstring(data[0][0])
    con.close()
    return data
def read_name():
    if __name__ == "__main__":
        con = sqlite3.connect("some.db")
    else:
        con = sqlite3.connect("face_detect/some.db")
    cur = con.cursor()
    cur.execute("select idx from test")
    data = cur.fetchall()
    con.close()
    return data
if __name__ == "__main__":
    print(list(read_name()[0]))