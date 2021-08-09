# from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Dict


class Observer(ABC):
    @abstractmethod
    def update(self, subject: str, data: any) -> None:
        pass


class Publisher:
    _observers: Dict[str, List[Observer]] = {}
    
    def attach(self, subject: str, observer: Observer) -> None:
        if subject not in self._observers:
            self._observers[subject] = []
        self._observers[subject].append(observer)

    def detach(self, observer: Observer, subject: str) -> None:
        self._observers[subject].remove(observer)

    def notify(self, subject: str, data: any = None) -> None:
       for observer in self._observers[subject]:
           observer.update(subject, data)