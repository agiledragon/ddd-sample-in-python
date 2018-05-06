from abc import abstractmethod


class Factory(object):

    @abstractmethod
    def create(self, *args):
        raise NotImplementedError
