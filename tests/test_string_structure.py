import pytest


class TestStringStructure:
    str_for_test = 'Hello world!'
    str1 = str_for_test[0:5]
    str2 = str_for_test[5:]

    def test_multiple(self):
        model = 'Hello world!Hello world!'
        tmp_str = self.str_for_test * 2
        assert model == tmp_str

    @pytest.mark.parametrize("char, expect", [(0, "H"), (1, "e"), (2, "l"), (3, "l"), (4, "o")])
    def test_string_consist(self, char, expect):
        assert self.str_for_test[char] == expect

    def test_concat(self):
        concat_str = self.str1 + self.str2
        assert self.str_for_test == concat_str

    def test_len(self):
        assert len(self.str_for_test) == 12

    def test_replace(self):
        model = 'Hello Peter!'
        self.str_for_test = self.str_for_test.replace('world', 'Peter')
        assert model == self.str_for_test
