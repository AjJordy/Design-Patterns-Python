"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""


from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZonaNorte(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da zona norte está buscando o cliente')


class CarroPopularZonaNorte(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular da zona norte está buscando o cliente')


class MotoZonaNorte(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto da zona norte está buscando o cliente')


class MotoLuxoZonaNorte(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo da zona norte está buscando o cliente')


class CarroLuxoZonaSul(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo da zona Sul está buscando o cliente')


class CarroPopularZonaSul(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular da zona Sul está buscando o cliente')


class MotoZonaSul(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto da zona Sul está buscando o cliente')


class MotoLuxoZonaSul(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo da zona Sul está buscando o cliente')


class VeiculoFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: 
        return CarroLuxoZonaNorte()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular: 
        return CarroPopularZonaNorte()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: 
        return MotoLuxoZonaNorte()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZonaNorte()


class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZonaSul()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZonaSul()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZonaSul()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZonaSul()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.busca_clientes()
