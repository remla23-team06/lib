from importlib import metadata


class VersionUtil:
    @classmethod
    def get_version(cls):
        try:
            return metadata.version('version_util')
        except metadata.PackageNotFoundError:
            return 'Package not found'
