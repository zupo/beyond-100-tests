def colorize(text, color):
    if color == "red":
        color = "1;31"
    elif color == "blue":
        color = "1;34"

    return f"\033[{color}m{text}\033[0m"


if __name__ == "__main__":  # pragma: no cover
    print(f"roses are {colorize('red', 'red')}")
    print(f"this is a {colorize('hack', 'black')}")


# -- HERE BE TESTS -- #


def test_red():
    assert colorize("foo", "red") == "\033[1;31mfoo\033[0m"


def test_blue():
    assert colorize("foo", "blue") == "\033[1;34mfoo\033[0m"


""" Scenario:
$ pytest --cov=run --cov-report html run.py
$ open htmlcov/index.html
$ python run.py
"""
