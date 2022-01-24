import pstats
from masonite.packages import PackageProvider


class PackageProvider(PackageProvider):

    def configure(self):
        self.root("package").name("package")

    def register(self):
        super().register()

    def boot(self):
        pass
