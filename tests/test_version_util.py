def test_get_version_is_str(version_util):
    assert isinstance(version_util.get_version(), str)