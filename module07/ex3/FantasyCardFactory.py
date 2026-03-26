from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power:
            name = name_or_power
        else:
            name = "Goblin Warrior"
        cost = 2
        if name_or_power == "Fire Dragon":
            cost = 5
        return CreatureCard(name, cost, "Common", 2, 2)

    def create_spell(self, name_or_power=None) -> SpellCard:
        if name_or_power:
            name = name_or_power
        else:
            name = "Lightning Bolt"
        return SpellCard(name, 3, "Common", "Deal 3 damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        if name_or_power:
            name = name_or_power
        else:
            name = "Mana Ring"
        return ArtifactCard(name, 1, "Rare", 3, "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        try:
            deck.append(self.create_creature("dragon"))
        except Exception:
            pass
        try:
            deck.append(self.create_creature("goblin"))
        except Exception:
            pass
        try:
            deck.append(self.create_spell("fireball"))
        except Exception:
            pass
        return {"deck": deck[:max(0, size)]}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
