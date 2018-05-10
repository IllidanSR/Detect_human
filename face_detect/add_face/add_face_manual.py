import face_recognition
import cv2
from face_detect import db
def load_new_face_to_db(Name,image):
    load_image = face_recognition.load_image_file(image)

    load_image_face_encoding = face_recognition.face_encodings(load_image)[0]
    # print(load_image_face_encoding)
    db.incert(Name, load_image_face_encoding)

def ROI_image(image, x1,y1,x2,y2):
    img = cv2.imread(image)
    return img[x1:x2,y1:y2]

if __name__ =="__main__":
    load_new_face_to_db("Vika","vik.jpg")