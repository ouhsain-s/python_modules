from abc import ABC, abstractmethod


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power=None) -> None:
        pass

    @abstractmethod
    def create_spell(self, name_or_power=None) -> None:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power=None) -> None:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass
