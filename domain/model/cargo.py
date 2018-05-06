from domain.model.base.entity import Entity
from domain.model.delivery import Delivery


class Cargo(Entity):
    def __init__(self, cargo_id, delivery):
        Entity.__init__(self, cargo_id)
        self._delivery = delivery

    def delay(self, days):
        after = self._delivery.after_days
        self._delivery = Delivery(after + days)

    @property
    def after_days(self):
        return self._delivery.after_days


if __name__ == '__main__':
    delivery = Delivery(10)
    cargo = Cargo(1, delivery)
    cargo.delay(5)
    print cargo.after_days
    print cargo.id

