import datetime


def get_yesterdays_microsecond():
    return datetime.datetime.now().microsecond - datetime.timedelta(day=1)


def get_current_microsecond():
    return datetime.datetime.now().microsecond


# -- HERE BE TESTS -- #
from unittest import mock


@mock.patch("run.datetime")
def test_get_current_microsecond(patched_dt):
    patched_dt.now.return_value.microsecond = 999
    assert get_current_microsecond() == 999


""" Scenario:
$ pytest run.py
"""
