def number():
    return 2


# -- HERE BE TESTS -- #
import unittest


class TestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(number(), 1)

    def test_not_equal(self):
        self.assertNotEqual(number(), 2)

    def test_less_than(self):
        self.assertLess(number(), 2)

    def test_greater_than(self):
        self.assertGreater(number(), 0)

    def test_contained(self):
        self.assertIn(number(), [0, 1])

    def test_instance(self):
        self.assertIsInstance(number(), int)


""" Scenario:
$ pytest run.py
$ flake8 run.py
$ open https://pypi.org/project/flake8-assertive/
"""
