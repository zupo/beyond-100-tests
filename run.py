import datetime


def get_yesterdays_microsecond():
    return datetime.datetime.now().microsecond - datetime.timedelta(day=1)


def get_current_microsecond():
    return datetime.datetime.now().microsecond


# -- HERE BE TESTS -- #
from freezegun import freeze_time


@freeze_time("2018-01-01 11:22:33.9999999")
def test_get_current_microsecond():
    assert get_current_microsecond() == 999999


""" Scenario:
$ pytest run.py
$ open https://pypi.org/project/freezegun/
"""
