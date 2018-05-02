import unittest

class Test_main_module(unittest.TestCase):

    def test_connection_model(self):
        if self.assertRaises(TypeError):
            print("Нет модели!")
        elif self.assertRaises(None):
            print("NONE")
        elif self.assertRaises(SystemExit):
            print("Ошибка системы, ядро упало")
        elif self.assertRaises(MemoryError):
            print("Утечка памяти")
    def test_camera_connection(self):
        if self.assertRaises(None):
            print("Камера не подключена!")

    def test_data_base_connection(self):
