import pytest


class TestSetStructure:
    set_of_test = {'H', 'e', 'l', 'l', 'o'}
    standart_set = set(set_of_test)

    def test_pop(self):
        self.set_of_test.pop()
        assert len(self.set_of_test) == len(self.standart_set) - 1

    def test_copy(self):
        tmp_set = self.set_of_test.copy()
        assert tmp_set == self.set_of_test

    @pytest.mark.parametrize('value', ['a', 'b', 'c', 'd'])
    def test_add(self, value):
        model = {'H', 'e', 'l', 'l', 'o', value}
        self.set_of_test = self.standart_set.copy()
        self.set_of_test.add(value)
        assert model == self.set_of_test

    def test_discard(self):
        self.set_of_test = self.standart_set.copy()
        self.set_of_test.discard('e')
        assert len(self.set_of_test) == len(self.standart_set) - 1

    def test_clear(self):
        self.set_of_test.clear()
        assert len(self.set_of_test) == 0
