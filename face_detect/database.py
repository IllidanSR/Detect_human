import sqlite3
import face_recognition
import json
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        # self.cur = self.conn.execute("CREATE TABLE HUMAN(id CHAR, array ENCODER)")

    def write_2_db(self,image):
        my_face = face_recognition.load_image_file(image)
        my_face_encoding = face_recognition.face_encodings(my_face)[0]
        self.cur.execute("INSERT INTO HUMAN VALUES (?,?)", ("Sergei", json.dumps(my_face_encoding.tolist())))
        self.conn.commit()
        # data = self.cur.execute("SELECT * FROM HUMAN")
        # data = self.cur.fetchall()
        # print(my_list)
        # print(type(my_face_encoding))
    def write(self, image):
        my_face = face_recognition.load_image_file(image)
        my_face_encoding = face_recognition.face_encodings(my_face)[0]
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO HUMAN VALUES (?,?)",(17081993,my_face_encoding))
        conn.commit()
        conn.close()
    def read(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM  HUMAN")
        result = c.fetchall()
        conn.close()
        print(result)
    def find_in_db(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("")
if __name__ == "__main__":
    db = DB()
    # db.write_2_db("Sergei.jpg")
    db.read()
