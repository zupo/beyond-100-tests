def describe_car(car):
    if not "wheels" in car.keys():
        raise Exception("wheels is a required key")
    if not "doors" in car.keys():
        raise Exception("doors is a required key")
    return f"This car has {car['wheels']} wheels and {car['doors']} doors."


if __name__ == "__main__":  # pragma: no cover
    corsa = {"wheels": 4, "doors": 5}
    print(describe_car("corsa"))


# -- HERE BE TESTS -- #
import pytest


def test_describe_car():
    corsa = {"wheels": 4, "doors": 5}
    assert describe_car(corsa) == "This car has 4 wheels and 5 doors."


def test_bad_parameters():

    with pytest.raises(Exception) as exc:
        describe_car({})

    assert str(exc.value) == "wheels is a required key"

    with pytest.raises(Exception) as exc:
        describe_car({"wheels": 4})

    assert str(exc.value) == "doors is a required key"


""" Scenario:
$ pytest --cov=run --cov-report html --cov-branch run.py
$ open htmlcov/index.html
$ python run.py
"""
