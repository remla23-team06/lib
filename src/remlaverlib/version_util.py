from importlib import metadata


class VersionUtil:
    """
    This class returns the current version of REMLA ver(sion) lib(rary)
    """
    @classmethod
    def get_version(cls) -> str:
        """
        Returns the current version of remlaverlib
        :return: a string with the version number like MAJOR.MINOR.PATCH
        """
        try:
            return metadata.version("remlaverlib")
        except metadata.PackageNotFoundError:
            return "Package not found"
