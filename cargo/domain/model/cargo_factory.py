from domain.model.base.factory import Factory
from domain.model.delivery import Delivery
from domain.model.cargo import Cargo


class CargoFactory(Factory):

    def create(self, cargo_id, days):
        delivery = Delivery(days)
        return Cargo(cargo_id, delivery)


if __name__ == '__main__':
    cargo = CargoFactory().create(1, 10)
    print cargo.id
    print cargo.after_days

