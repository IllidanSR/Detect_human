import sqlite3
import numpy as np
import io
import time
import os

# compressor = 'bz2'  # zlib, bz2

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    # zlib uses similar disk size that Matlab v5 .mat files
    # bz2 compress 4 times zlib, but storing process is 20 times slower.
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read().encode())  # zlib, bz2

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    out = io.BytesIO(out.read().encode())
    return np.load(out)

sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("array", convert_array)


dbname = 'example.db'
def save_sqlite_arrays(Name,arr):
    "Load MNIST database (70000 samples) and store in a compressed SQLite db"
    os.path.exists(dbname) and os.unlink(dbname)
    con = sqlite3.connect(dbname, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute("create table test (idx text primary key, Enc array);")
    cur.execute("insert into test (idx, Enc) values (?,?)",(Name, arr))
    con.commit()
    con.close()

def load_sqlite_arrays():
    "Query MNIST SQLite database and load some samples"
    con = sqlite3.connect(dbname, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute('select Enc from test')
    data = cur.fetchall()
    return data


if __name__ == '__main__':
    pass
    #
    load_sqlite_arrays()