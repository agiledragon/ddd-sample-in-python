from abc import abstractmethod


class Provider(object):

    @abstractmethod
    def confirm(self, *args):
        raise NotImplementedError

