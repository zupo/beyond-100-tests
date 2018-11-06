import requests


def YEN_last_month():
    response = requests.get(
        "http://data.fixer.io/2018-10-01?symbols=JPY&access_key=SECRET"
    )
    first_of_month = response.json()["rates"]["JPY"]
    response2 = requests.get(
        "http://data.fixer.io/2018-10-31?symbols=JPY&access_key=SECRET"
    )
    last_of_month = response.json()["rates"]["JPY"]
    return first_of_month, last_of_month


# -- HERE BE TESTS -- #

from unittest import mock


@mock.patch("run.requests")
def test_YEN_last_month(mocked_requests):
    mocked_requests.get.return_value.json.return_value = {"rates": {"JPY": 1.1}}
    assert YEN_last_month() == (1.1, 1.1)  # Really Bad Test™


""" Scenario:
$ pytest run.py
"""
