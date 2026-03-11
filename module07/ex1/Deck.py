import random
from typing import List
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.cards:
            if getattr(c, "name", None) == card_name:
                self.cards.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("draw from empty deck")
        return self.cards.pop(0)

    # def get_play_result(result: dict):
    #     print(f"play result: card_played : {} {} {} {}")
    def get_deck_stats(self) -> dict:
        creatures = sum(1 for c in self.cards
                        if type(c).__name__ == "CreatureCard")
        spells = sum(1 for c in self.cards
                     if type(c).__name__ == "SpellCard")
        artifacts = sum(1 for c in self.cards
                        if type(c).__name__ == "ArtifactCard")
        total = len(self.cards)
        total_cost = sum(getattr(c, "cost", 0) for c in self.cards)
        avg_cost = total_cost / total if total else 0.0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }

    def __len__(self) -> int:
        return len(self.cards)
