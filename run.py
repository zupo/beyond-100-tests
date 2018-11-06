def max_values(list, list2):
    max = list[0]
    for x in list:
        if x > 0:
            max = x

    all_values = list()
    all_values.append(max)

    max = list2[0]
    for x in list2:
        if x > 0:
            max = x
    all_values.append(max)

    return all_values


# -- HERE BE TESTS -- #


def test_max_values():
    assert max_values([3, 4, 5], [5, 6, 7]) == [5, 7]


""" Scenario:
$ pytest run.py
$ flake8 run.py
$ open https://pypi.org/project/flake8-builtins/
"""
