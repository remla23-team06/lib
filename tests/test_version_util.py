def test_get_version_is_str(version_util):
    """
    Test if the get_version method returns a type of string
    :param version_util:
    :return: str containing a version
    """
    assert isinstance(version_util.get_version(), str)
