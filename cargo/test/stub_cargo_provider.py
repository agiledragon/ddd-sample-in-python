from domain.model.base.provider import Provider


class StubCargoProvider(Provider):

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


    