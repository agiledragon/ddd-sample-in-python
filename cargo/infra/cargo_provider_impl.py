from domain.model.cargo_provider import CargoProvider


class CargoProviderImpl(CargoProvider):

    def confirm(self, cargo):
        print 'confirm cargo'


