from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable
from typing import Dict
import random

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int = 3, rarity: str = "Common", base_rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    # Rankable methods
    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins - self.losses) * 16
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> Dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    # Combatable methods
    def attack(self, target) -> Dict:
        outcome = random.choice([True, False])
        if outcome:
            self.update_wins(1)
            target.update_losses(1)
        else:
            self.update_losses(1)
            target.update_wins(1)
        return {
            "attacker": self.card_id,
            "defender": target.card_id,
            "attacker_wins": self.wins,
            "defender_wins": target.wins,
            "outcome": "attacker" if outcome else "defender"
        }

    def defend(self, incoming_damage: int) -> Dict:
        # مجرد مثال دفاعي بسيط
        blocked = min(5, incoming_damage)
        taken = max(0, incoming_damage - 5)
        return {
            "defender": self.card_id,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict:
        return {"attack": 5, "defense": 5}

    # Card method
    def play(self, game_state: Dict) -> Dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        return game_state

    def get_tournament_stats(self) -> Dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }