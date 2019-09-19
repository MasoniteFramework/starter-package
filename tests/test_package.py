from masonite.testing import TestCase
from masonite.routes import Get

class TestPackage(TestCase):

    def setUp(self):
        super().setUp()
        self.routes(only=[
            Get('/home', )
        ])
    
    def test_can_get_home_route(self):
        return True