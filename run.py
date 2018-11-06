# fmt: off
class ModelFeatureFactoryToolkitFeelsLikeJava(object):

    with_a_very_long_parameter = "that is one long text, really"
    and_another_one = "and a bit shorter text, maybe",

    def some_very_complex_method_here(argument_foo, argument_bar):
        return (
            argument_foo ** argument_bar + with_a_very_long_parameter  # noqa
        ) / and_another_one  # noqa
# fmt: on


def test_parameters_are_of_equal_length():
    obj = ModelFeatureFactoryToolkitFeelsLikeJava
    assert len(obj.with_a_very_long_parameter) == len(obj.and_another_one)


""" Scenario:
$ pytest run.py
$ flake8 run.py
$ open https://pypi.org/project/flake8_tuple/
"""
