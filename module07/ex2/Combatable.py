from abc import ABC, abstractmethod
from typing import Dict, Any


class Combatable(ABC):
    """Abstract interface for combat-related abilities."""

    @abstractmethod
    def attack(self, target) -> Dict[str, Any]:
        """Perform an attack against `target`.
        Returns a dictionary describing the attack result.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Defend against incoming damage.
        Returns a dictionary describing the defense result.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """Return combat stats such as attack power and defense."""
        pass
