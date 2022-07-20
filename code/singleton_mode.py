#! -*- utf-8 -*-

class _Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(_Singleton('SingletonMeta', (object, ), {})):
    pass

class Logger(Singleton):
    pass

def singleton(cls, *args, **kwargs):
    instances = {}
    def get_instance(*args, **kwargs):
        # nonlocal instances
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Myclass(object):
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)

if __name__ == '__main__':
    a = Myclass('Michael', 'Ma')
    b = Myclass(1, 2)

    print(a)
    print(b)

    c = Logger()
    d = Logger()

    print(c)
    print(d)