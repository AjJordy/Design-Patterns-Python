"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
# from __future__ import annotations
from typing import List
from copy import deepcopy


class Address:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    luiz = Person('Luiz', 'Miranda')
    endereco = Address('Av. Brazil', '250A')
    luiz.add_address(endereco)

    # esposa_luiz = deepcopy(luiz)
    # esposa_luiz.firstname = 'Leticia'
    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Leticia'
