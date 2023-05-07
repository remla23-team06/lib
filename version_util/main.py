from importlib import metadata


class VersionUtil:
    @classmethod
    def get_version(cls):
        try:
            return metadata.version('your_package_name')
        except metadata.PackageNotFoundError:
            return 'Package not found'
