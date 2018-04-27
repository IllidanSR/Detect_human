import dlib
from skimage import io
from scipy.spatial import distance


class FaceDetect:

    def __init__(self):
        self.sp = dlib.shape_predictor('FaceDetect/shape_predictor_68_face_landmarks.dat')
        self.facerec = dlib.face_recognition_model_v1('FaceDetect/dlib_face_recognition_resnet_model_v1.dat')
        self.detector = dlib.get_frontal_face_detector()

    def get_descriptor(self, img):
        win = dlib.image_window()
        win.clear_overlay()
        win.set_image(img)
        dets = self.detector(img, 1)
        shape = None

        for k, d in enumerate(dets):
            shape = self.sp(img, d)
            win.clear_overlay()
            win.add_overlay(d)
            win.add_overlay(shape)

        face_array = []
        try:
            face_descriptor = self.facerec.compute_face_descriptor(img, shape)
            for i in face_descriptor:
                face_array.append(i)
        except:
            pass
        return face_array

    def compare(self, face1, face2):
        if len(face1) == 0:
            return 1
        if len(face2) == 0:
            return 1
        return distance.euclidean(face1, face2)

    def coder(self):
        pass

    def decoder(self):
        pass