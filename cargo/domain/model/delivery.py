from domain.model.base.value_object import ValueObject


class Delivery(ValueObject):

    def __init__(self, after_days):
        self._after_days = after_days

    @property
    def after_days(self):
        return self._after_days


if __name__ == '__main__':
    delivery = Delivery(10)
    print delivery.after_days

