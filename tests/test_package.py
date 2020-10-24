from masonite.testing import TestCase
from masonite.routes import Get


class TestPackage(TestCase):
    sqlite = False

    def setUp(self):
        super().setUp()
        self.routes(only=[Get("/", "WelcomeController@show")])

    def test_can_get_home_route(self):
        self.assertTrue(self.get("/").contains("Hello Package World"))
