from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Magical(ABC):
    """Abstract interface for magic-related abilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        """Cast a spell named `spell_name` on `targets`.
        Returns a dictionary describing the spell result.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """Channel (gain) `amount` mana. Returns current mana state."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Return magic stats such as current mana and max mana."""
        pass
