from .CardFactory import CardFactory

try:
    from ex0.CreatureCard import CreatureCard
except Exception:
    CreatureCard = None

try:
    from ex1.SpellCard import SpellCard
except Exception:
    SpellCard = None

try:
    from ex1.ArtifactCard import ArtifactCard
except Exception:
    ArtifactCard = None


def try_instantiate(cls, *args_options):
    if cls is None:
        raise RuntimeError("Class not available")
    last_exc = None
    for args, kwargs in args_options:
        try:
            return cls(*args, **(kwargs or {}))
        except Exception as e:
            last_exc = e
    raise last_exc if last_exc is not None else\
        RuntimeError("Instantiation failed")


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        name = "Goblin Warrior"
        cost = 2
        if name_or_power == "dragon":
            name = "Fire Dragon"
            cost = 5

        tries = [
            ((name, cost, "Common", 2, 2), {}),
            ((name, cost, 2, 2), {}),
            ((name, cost), {}),
        ]
        return try_instantiate(CreatureCard, *tries)

    def create_spell(self, name_or_power=None):
        name = "Lightning Bolt" if not name_or_power else\
            str(name_or_power).title()
        tries = [
            ((name, 3, "Common", "Deal 3 damage"), {}),
            ((name, 3, "Deal 3 damage"), {}),
            ((name, 3), {}),
        ]
        return try_instantiate(SpellCard, *tries)

    def create_artifact(self, name_or_power=None):
        name = "Mana Ring"
        tries = [
            ((name, 1, "Rare", "Permanent: +1 mana per turn"), {}),
            ((name, 1, "Permanent: +1 mana per turn"), {}),
            ((name, 1), {}),
        ]
        return try_instantiate(ArtifactCard, *tries)

    def create_themed_deck(self, size: int):
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
        return {"deck": deck[:max(0, int(size))]}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "lightning"],
            "artifacts": ["mana_ring"]
        }
