def number():
    return 2


# -- HERE BE TESTS -- #
def test_equal():
    assert number() == 1


def test_not_equal():
    assert number() != 1


def test_less_than():
    assert number() < 2


def test_greater_than():
    assert number() > 0


def test_contained():
    assert number() in [1, 0]


def test_instance():
    assert isinstance(number(), int)


""" Scenario:
$ pytest run.py
$ flake8 run.py
$ open https://pypi.org/project/flake8-assertive/
"""
