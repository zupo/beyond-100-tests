import logging

logger = logging.getLogger(__name__)


def process_data():
    logger.warn("Processing started.")
    pass  # hardcore processing action
    logger.warn("Processing finished.")


# -- HERE BE TESTS -- #
from testfixtures import LogCapture


def test_process_data():

    with LogCapture() as log:
        assert process_data() is None

    log.check(
        ("run", "WARNING", "Processing started."),
        ("run", "WARNING", "Processing finished."),
    )


""" Scenario:
$ pytest run.py
$ open https://pypi.org/project/testfixtures/
"""
