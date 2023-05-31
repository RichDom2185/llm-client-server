from __future__ import annotations

from abc import ABC, abstractmethod

# Adapted from https://refactoring.guru/design-patterns/observer/python/example


class Observable(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Observable) -> None:
        pass
