
class CargoMsg(object):

    def __init__(self, cargo_id, after_days):
        self._cargo_id = cargo_id
        self._after_days = after_days

    @property
    def cargo_id(self):
        return self._cargo_id

    @property
    def after_days(self):
        return self._after_days