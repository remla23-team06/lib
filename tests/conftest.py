import pytest

from src.remlaverlib import Preprocessor
from src.remlaverlib import VersionUtil

@pytest.fixture
def version_util() -> VersionUtil:
    """
    Loads an instance of the VersionUtil class
    :return: VersionUtil
    """
    return VersionUtil()

@pytest.fixture
def preprocessor():
    """
    Loads the preprocessor class instance
    :return: Preprocessor
    """
    pre_proc = Preprocessor()
    return pre_proc
