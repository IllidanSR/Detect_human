import face_recognition
import cv2
from face_detect import db
class Face_recogn:
    def __init__(self):
        #Read colum from DB
        self.my_face_enc = db.read()
        #add face encode to array, for iterable
        self.known_face_encodings = [
            self.my_face_enc
        ]
        #load from 1-st colum names
        self.known_face_names = list(db.read_name()[0])

    def recogn_face(self, frame):
        #load frame
        rgb_frame = frame[:, :, ::-1]
        #look for face on frame
        face_locations = face_recognition.face_locations(rgb_frame)
        #encoding finded on frame faces
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        #for every face, on frame, find nearest from DB(Use Euclide metric)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
            # else:
            #     test.incert("someone", face_encoding)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame

if __name__ == "__main__":
    fr = Face_recogn()
    # print(database.load_sqlite_arrays())