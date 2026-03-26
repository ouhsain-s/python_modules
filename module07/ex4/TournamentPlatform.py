from .TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: dict = {}
        self.matches_played = 0
        self.platform_status = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        winner, loser = (card1, card2) if random.choice([True, False])\
            else (card2, card1)
        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.values(),
                              key=lambda c: c.rating, reverse=True)
        leaderboard = []
        for idx, card in enumerate(sorted_cards, 1):
            leaderboard.append({
                "position": idx,
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = sum(c.rating for c in self.cards.values()) // total_cards\
            if total_cards else 0
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status
        }
