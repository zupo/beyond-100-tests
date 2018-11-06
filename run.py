import logging

logger = logging.getLogger(__name__)


def process_data():
    logger.info("Processing started.")
    pass  # hardcore processing action
    logger.info("Processing finished.")


# -- HERE BE TESTS -- #
from unittest import mock


@mock.patch("run.logger")
def test_process_data(mocked_logger):
    assert process_data() is None

    assert len(mocked_logger.info.mock_calls) == 2
    assert mocked_logger.info.mock_calls[0] == mock.call("Processing started.")
    assert mocked_logger.info.mock_calls[1] == mock.call("Processing finished.")


""" Scenario:
$ pytest run.py
"""
