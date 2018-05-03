import face_recognition
import cv2
class Face_recogn:
    def __init__(self):
        self.my_face = face_recognition.load_image_file("face_detect/Sergei.jpg")
        self.my_face_encoding = face_recognition.face_encodings(self.my_face)[0]
        self.known_face_encodings = [
            self.my_face,
        ]
        self.known_face_names = [
            "Sergei"
        ]
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