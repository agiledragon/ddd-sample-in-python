from domain.model.cargo_factory import CargoFactory
from domain.model.cargo_repo import get_cargo_repo
from domain.model.cargo_provider import get_cargo_provider


class CargoService(object):

    def __init__(self):
        self._cargo_repo = get_cargo_repo()
        self._cargo_provider = get_cargo_provider()

    def create(self, cargo_id, days):
        cargo = CargoFactory().create(cargo_id, days)
        self._cargo_repo.add(cargo_id, cargo)
        self._cargo_provider.confirm(cargo)

    def delay(self, cargo_id, days):
        cargo = self._cargo_repo.get(cargo_id)
        if cargo is not None:
            cargo.delay(days)
            self._cargo_repo.update(cargo_id, cargo)
            self._cargo_provider.confirm(cargo)

    def get_after_days(self, cargo_id):
        cargo = self._cargo_repo.get(cargo_id)
        if cargo is not None:
            return cargo.after_days

    def destroy(self, cargo_id):
        self._cargo_repo.remove(cargo_id)
