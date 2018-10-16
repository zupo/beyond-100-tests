import enum


class Color(enum.Enum):
    red = "1;31"
    blue = "1;34"


def colorize(text, color: Color):
    return f"\033[{color.value}m{text}\033[0m"


if __name__ == "__main__":  # pragma: no cover
    print(f"roses are {colorize('red', Color.red)}")
    print(f"this is a {colorize('hack', Color.black)}")


# -- HERE BE TESTS -- #


def test_red():
    assert colorize("foo", Color.red) == "\033[1;31mfoo\033[0m"


""" Scenario:
$ pytest --cov=run --cov-report html run.py --cov-branch
$ open htmlcov/index.html
$ mypy run.py
$ python run.py
"""
