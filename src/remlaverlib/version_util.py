from importlib import metadata


class VersionUtil:
    @classmethod
    def get_version(cls):
        try:
            return metadata.version('remlaverlib')
        except metadata.PackageNotFoundError:
            return 'Package not found'
