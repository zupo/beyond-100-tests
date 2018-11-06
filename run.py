from collections import namedtuple

Car = namedtuple("Car", ["wheels", "doors"])


def describe_car(car: Car):
    return f"This car has {car.wheels} wheels and {car.doors} doors."


if __name__ == "__main__":  # pragma: no cover
    corsa = {"wheels": 4, "doors": 5}
    print(describe_car("corsa"))


# -- HERE BE TESTS -- #


def test_describe_car():
    corsa = Car(wheels=4, doors=5)
    assert describe_car(corsa) == "This car has 4 wheels and 5 doors."


""" Scenario:
$ pytest --cov=run --cov-report html --cov-branch run.py
$ open htmlcov/index.html
$ mypy run.py
$ python run.py
"""
