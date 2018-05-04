import face_recognition
import cv2
from face_detect.database import DB
import numpy as np
class Face_recogn:
    def __init__(self):
        db = DB()
        self.my_face = face_recognition.load_image_file("Sergei.jpg")
        self.my_face_encoding = db.read()
        # print(len(self.my_face_encoding))
        self.known_face_encodings = []
        self.known_face_names = []
        for i in self.my_face_encoding:
            # print(np.fromstring(i[1],dtype=float))
            self.known_face_names.append(i[0])
            self.known_face_encodings.append((i[1]))
        print(self.known_face_names,self.known_face_encodings)
    # def rec_face(self,frame):
    #     rgb_frame = frame[:, :, ::-1]
    #     face_locations = face_recognition.face_locations(rgb_frame)
    #     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    #     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    def recogn_face(self, frame):
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame

if __name__ == "__main__":
    dr = Face_recogn()