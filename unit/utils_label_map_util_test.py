import pytest
from utils import label_map_util

class TestUtilsLabelMap:
    def value_error(self):
        with pytest.raises(ValueError):
            label_map_util._validate_label_map(0.5)
    def category_index_test(self):
        assert (list(label_map_util.create_category_index([{"id":"lol"}])) == {'lol': {'id': 'lol'}})
    def type_error_create_category_index(self):
        with pytest.raises(TypeError):
            label_map_util.create_category_index("test")
            label_map_util.create_category_index(1)
            label_map_util.create_category_index(0.1)
