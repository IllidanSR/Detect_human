import pytest
from detect_human import main_func

class TestDetectHuman:
    def test_type_error(self):
        with pytest.raises(TypeError):
            list(main_func("lol"))

