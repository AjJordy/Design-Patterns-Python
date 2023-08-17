
# class Meta(type):
#     def __call__(cls, *args, **kwds):
#         return super().__call__(*args, **kwds)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('new')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('init')
#         self.nome = nome

#     def __call__(self, *args, **kwds):
#         print('Call chamado')


# p1 = Pessoa('Luiz')
# p1()
# print(p1.nome)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    as1.nome = 'Luiz'
    print('as2.nome:', as2.nome)
