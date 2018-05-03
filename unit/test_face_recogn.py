import pytest
from face_detect.Face_recognition import Face_recogn

class TestFaceRecogn:
    def file_conn_error(self):
        with pytest.raises(FileNotFoundError):
            list(Face_recogn)
    def no_frame_error(self):
        with pytest.raises(TypeError):
            fr = Face_recogn()
            fr.recogn_face(None)
