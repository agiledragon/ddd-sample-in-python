import unittest

from app.service.cargo_api import *
from domain.model.cargo_provider import *
from test.spy_cargo_provider import SpyCargoProvider


class CargoTest(unittest.TestCase):

    def setUp(self):
        set_cargo_provider(SpyCargoProvider())
        self._cargo_id = 1
        self._after_days = 20

    def test_create_cargo(self):
        create_cargo(self._cargo_id, self._after_days)
        provider = get_cargo_provider()
        after_days = get_cargo_after_days(self._cargo_id)
        self.assertEqual(self._cargo_id, provider.cargo_id)
        self.assertEqual(self._after_days, provider.after_days)
        self.assertEqual(self._after_days, after_days)

    def test_delay_cargo(self):
        create_cargo(self._cargo_id, self._after_days)
        delay_cargo(self._cargo_id, 5)
        provider = get_cargo_provider()
        after_days = get_cargo_after_days(self._cargo_id)
        self.assertEqual(self._cargo_id, provider.cargo_id)
        self.assertEqual(self._after_days + 5, provider.after_days)
        self.assertEqual(self._after_days + 5, after_days)


if __name__ == '__main__':
    unittest.main()

