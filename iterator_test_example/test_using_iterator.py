import pytest
import requests

from csv import DictReader
from csv import reader


def _method(method_string):
    """Transform string to requests method"""
    return requests.get if method_string.lower() == "get" else requests.post


# Getting data from .csv file with DictReader
data_dictreader = DictReader(open("test_data.csv"))


@pytest.mark.parametrize("entry", data_dictreader)
def test_dict_reader(entry):
    assert _method(entry['method'])(entry["url"], allow_redirects=False).status_code == int(entry["status"])


# Getting data from csv file with reader
data_reader = reader(open("test_data.csv"))
header = next(data_reader)


@pytest.mark.parametrize(header, data_reader)
def test_reader(url, method, status):
    assert _method(method)(url, allow_redirects=False).status_code == int(status)
