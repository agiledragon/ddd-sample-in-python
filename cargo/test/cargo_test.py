import unittest

from app.service.cargo_api import *
from domain.model.cargo_provider import *
from domain.model.base.provider import Provider


class SpyCargoProvider(Provider):

    def __init__(self):
        self._cargo_id = 0
        self._after_days = 0

    def confirm(self, cargo):
        self._cargo_id = cargo.id
        self._after_days = cargo.after_days

    @property
    def cargo_id(self):
        return self._cargo_id

    @property
    def after_days(self):
        return self._after_days


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
        destroy_cargo(self._cargo_id)

    def test_delay_cargo(self):
        create_cargo(self._cargo_id, self._after_days)
        delay_cargo(self._cargo_id, 5)
        provider = get_cargo_provider()
        after_days = get_cargo_after_days(self._cargo_id)
        self.assertEqual(self._cargo_id, provider.cargo_id)
        self.assertEqual(self._after_days + 5, provider.after_days)
        self.assertEqual(self._after_days + 5, after_days)
        destroy_cargo(self._cargo_id)


if __name__ == '__main__':
    unittest.main()

