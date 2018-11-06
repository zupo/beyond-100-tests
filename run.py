def increment(n):
    return ++n


def append_to(element, to=[]):
    to.append(element)
    return to


# -- HERE BE TESTS -- #


def test_increment():

    assert increment(1) == 2


def test_append_to():
    my_list = append_to(12)
    assert my_list == [12]

    my_other_list = append_to(42)
    assert my_other_list == [42]


""" Scenario:
$ pytest run.py
$ flake8 run.py
$ open https://pypi.org/project/flake8-bugbear/
"""
