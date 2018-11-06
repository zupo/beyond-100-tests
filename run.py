def number():
    return 2


# -- HERE BE TESTS -- #
import unittest


class TestCase(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(number() == 1)

    def test_not_equal(self):
        self.assertTrue(number() != 2)

    def test_less_than(self):
        self.assertTrue(number() < 2)

    def test_greater_than(self):
        self.assertTrue(number() > 0)

    def test_contained(self):
        self.assertTrue(number() in [0, 1])

    def test_instance(self):
        self.assertTrue(isinstance(number(), int))


""" Scenario:
$ pytest run.py
$ flake8 run.py
"""
