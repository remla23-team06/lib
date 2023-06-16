import pytest

from src.remlaverlib import Preprocessor


@pytest.fixture
def preprocessor():
    """
    Loads the preprocessor class instance
    :return: Preprocessor
    """
    pre_proc = Preprocessor()
    return pre_proc
