"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """ Observable """
    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observer(self) -> None: pass


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class WeatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observer()

    def reset_state(self):
        self._state = {}
        self.notify_observer()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None: 
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou '
              f'de ser atualizado => {self.observable.state}')


class WeatherStationFacede:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()
        self.smartphone = Smartphone('iPhone', self.weather_station)
        self.outro_smartphone = Smartphone('Android', self.weather_station)
        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.outro_smartphone)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == '__main__':   
    weather_station = WeatherStationFacede()
    # weather_station.state = {'temperature': '30'}
    # weather_station.state = {'temperature': '32'}
    # weather_station.state = {'humidity': '90'}
    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '90'})

    # weather_station.remove_observer(outro_smartphone)    
    # weather_station.reset_state()
    weather_station.remove_smartphone()
    weather_station.reset_state()
