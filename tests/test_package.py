from masonite.tests import TestCase


class TestPackage(TestCase):

    def setUp(self):
        super().setUp()

    def test_can_get_home_route(self):
        self.assertTrue(
            self.get('/').assertOk().assertContains('Masonite')
        )
