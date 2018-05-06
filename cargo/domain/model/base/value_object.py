
class ValueObject(object):

    def __setattr__(self, key, value):
        if not self.__dict__.has_key(key):
            self.__dict__[key] = value
        else:
            raise AttributeError()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

