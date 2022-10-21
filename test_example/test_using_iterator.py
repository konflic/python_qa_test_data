import pytest
import requests

from csv import DictReader
from csv import reader


def request_method(method_string: str):
    """Transform string to request method"""
    return requests.get if method_string.lower() == "get" else requests.post


# Getting data from .csv file with DictReader
api_test_data = DictReader(open("test_data.csv"))


@pytest.mark.parametrize("entry", api_test_data)
def test_dict_reader(entry):
    method = entry['method']
    url = entry["url"]
    expected_status = int(entry["status"])

    assert request_method(method)(url, allow_redirects=False).status_code == expected_status


# Getting data from csv file with reader
data_reader = reader(open("test_data.csv"))
header = next(data_reader)


@pytest.mark.parametrize(header, data_reader)
def test_reader(url, method, status):
    assert request_method(method)(url, allow_redirects=False).status_code == int(status)
