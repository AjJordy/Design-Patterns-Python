"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod


class User:
    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):

    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone_number(self, phone_number): pass

    @abstractmethod
    def add_addresses(self, addresses): pass


class UserBuilder(IUserBuilder):

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone_number(self, phone_number):
        self._result.phone_numbers.append(phone_number)
        return self

    def add_addresses(self, addresses):
        self._result.addresses.append(addresses)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        # self._builder.add_firstname(firstname)
        # self._builder.add_lastname(lastname)
        # self._builder.add_age(age)
        self._builder.add_firstname(firstname)\
                     .add_lastname(lastname)\
                     .add_age(age)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Luiz', 'Otavio', 30)