import sqlite3
import numpy as np
import io
import os
import time
import sys
import mnist
import json
# Name = "Sergei"
# con = sqlite3.connect("some.db")
# cur = con.cursor()
# cur.execute("create table test_new (idx int primary key, Name varchar Enc varchar);")
# cur.execute("insert into test (idx, Enc) values (?,?)",(Name, arr))
# cur.execute("select Enc from main.test")
# data = cur.fetchall()
# print(np.fromstring(data[0][0]))
# con.commit()

def incert(Name, arr):
    con = sqlite3.connect("some.db")
    cur = con.cursor()
    cur.execute("create table test (idx int primary key, Enc varchar);")
    cur.execute("insert into test (idx, Enc) values (?,?)",(Name, arr))
    con.commit()
    con.close()
def read():
    con = sqlite3.connect("face_detect/some.db")
    cur = con.cursor()
    cur.execute("select Enc from test")
    data = cur.fetchall()
    # print(data)
    data = np.fromstring(data[0][0])
    con.close()
    return data

if __name__ == "__main__":
    print(read())