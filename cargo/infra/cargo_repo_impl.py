from domain.model.base.repo import Repo


class CargoRepoImpl(Repo):

    def add(self, id, obj):
        print 'add cargo'
        return False

    def remove(self, id):
        print 'remove cargo'

    def update(self, id, obj):
        print 'update cargo'
        return False

    def get(self, id):
        print 'get cargo by id'
        return None



