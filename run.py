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

import responses


@responses.activate
def test_YEN_last_month():

    responses.add(
        responses.GET,
        "http://data.fixer.io/2018-10-01?symbols=JPY&access_key=SECRET",
        json={"rates": {"JPY": 1.1}},
    )

    responses.add(
        responses.GET,
        "http://data.fixer.io/2018-10-31?symbols=JPY&access_key=SECRET",
        json={"rates": {"JPY": 1.2}},
    )

    assert YEN_last_month() == (1.1, 1.2)


""" Scenario:
$ pytest run.py
$ open https://pypi.org/project/responses/
"""
