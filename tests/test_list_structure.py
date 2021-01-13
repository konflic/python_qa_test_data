import pytest


class TestListStructure:
    list_for_test = [1, 2, 3, 4]
    standart_list = list(list_for_test)

    @pytest.mark.parametrize("value", [1, 2, 3, 4, 5])
    def test_append(self, value):
        model = [1, 2, 3, 4, value]
        self.list_for_test = list(self.standart_list)
        self.list_for_test.append(value)
        assert model == self.list_for_test

    def test_pop(self):
        self.list_for_test = list(self.standart_list)
        self.list_for_test.pop(0)
        assert len(self.list_for_test) == len(self.standart_list) - 1

    def test_pop_value(self):
        self.list_for_test = list(self.standart_list)
        value = self.list_for_test.pop(2)
        assert value == 3

    def test_clear(self):
        self.list_for_test.clear()
        assert len(self.list_for_test) == 0

    def test_count(self):
        self.list_for_test = list(self.standart_list)
        count3 = self.list_for_test.count(3)
        assert count3 == 1
