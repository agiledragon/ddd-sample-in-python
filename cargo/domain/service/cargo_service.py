from domain.model.cargo_factory import CargoFactory


class CargoService(object):

    def __init__(self, cargo_repo, cargo_provider):
        self._cargo_repo = cargo_repo
        self._cargo_provider = cargo_provider

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
