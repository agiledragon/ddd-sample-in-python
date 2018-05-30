from domain.model.base.provider import Provider


class CargoProviderImpl(Provider):

    def confirm(self, cargo):
        print 'confirm cargo'


