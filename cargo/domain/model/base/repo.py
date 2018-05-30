
class Repo(object):

    def __init__(self):
        self._repo = {}

    def add(self, id, obj):
        if self._repo.has_key(id):
            return False
        self._repo[id] = obj
        return True

    def remove(self, id):
        if self._repo.has_key(id):
            del self._repo[id]

    def update(self, id, obj):
        if self._repo.has_key(id):
            self._repo[id] = obj
            return True
        return False

    def get(self, id):
        return self._repo[id]

