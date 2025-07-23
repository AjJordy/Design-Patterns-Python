from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List,Dict
from time import sleep

class IUser(ABC):
    """ Subject interface """
    first_name: str
    last_name: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    """ Real Subject """
    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2) # simulate a request
        self.first_name = first_name
        self.last_name = last_name


    def get_addresses(self) -> List[Dict]:
        sleep(2) # simulate a request
        return [
            {"rua":"Av. Brasil", "numero": 500}
        ]


    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {
            "cpf": "111.111.111-11",
            "rg": "AB111222333",
        }


class UserProxy(IUser):
    """ Proxy Subject """
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        # Not exist yet
        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict


    def get_real_user(self) -> None:
        """ Lazy instantiation """
        if not hasattr(self, "_real_user"):
            self._real_user = RealUser(self.first_name, self.last_name)


    def get_addresses(self):
        self.get_real_user()
        if not hasattr(self, "_cached_addresses"):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses


    def get_all_user_data(self):
        self.get_real_user()
        if not hasattr(self, "_all_user_data"):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == "__main__":
    user_proxy = UserProxy("Jordy", "Araujo")
    print(user_proxy.first_name)
    print(user_proxy.last_name)

    # 6 seconds
    print(user_proxy.get_all_user_data())
    print(user_proxy.get_addresses())

    # Cached data
    for i in range(50):
        user_proxy.get_addresses()
