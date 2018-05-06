import unittest

from app.service.cargo_api import CargoApi
from app.service.cargo_msg import CargoMsg
from domain.service.cargo_service import CargoService
from test.stub_cargo_provider import StubCargoProvider
from test.stub_cargo_repo import StubCargoRepo


class CargoTest(unittest.TestCase):

    def setUp(self):
        self._cargo_id = 1
        self._after_days = 20
        self._provider = StubCargoProvider()

    def create_api(self):
        repo = StubCargoRepo()
        service = CargoService(repo, self._provider)
        return CargoApi(service)

    def test_create_cargo(self):
        msg = CargoMsg(1, 10)
        api = self.create_api()
        api.create_cargo(msg)
        self.assertEqual(msg.cargo_id, self._provider.cargo_id)
        self.assertEqual(msg.after_days, self._provider.after_days)

    def test_delay_cargo(self):
        msg = CargoMsg(self._cargo_id, self._after_days)
        api = self.create_api()
        api.create_cargo(msg)
        api.delay(self._cargo_id, 5)
        self.assertEqual(self._cargo_id, self._provider.cargo_id)
        self.assertEqual(25, self._provider.after_days)


if __name__ == '__main__':
    unittest.main()

