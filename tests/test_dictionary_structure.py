import pytest


class TestDictionaryStructure:
    dict_for_test = {'key1': 1, 'key2': 2, 'key3': 3}
    standart_dict = dict_for_test.copy()

    @pytest.mark.parametrize("key, value", [("key4", 4), ("key5", 5)])
    def test_add(self, key, value):
        model = {'key1': 1, 'key2': 2, 'key3': 3, key: value}
        self.dict_for_test = self.standart_dict.copy()
        self.dict_for_test[key] = value
        assert model == self.dict_for_test

    def test_keys(self):
        model = ['key1', 'key2', 'key3']
        dict_keys = list(self.dict_for_test.keys())
        assert model == dict_keys

    def test_pop(self):
        self.dict_for_test = self.standart_dict.copy()
        self.dict_for_test.pop('key1')
        assert len(self.dict_for_test) == len(self.standart_dict) - 1

    def test_value(self):
        model = [1, 2, 3]
        self.dict_for_test = self.standart_dict.copy()
        dict_values = list(self.dict_for_test.values())
        assert dict_values == model

    def test_clear(self):
        self.dict_for_test.clear()
        assert len(self.dict_for_test) == 0
