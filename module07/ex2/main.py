from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def _callable_public_names(cls) -> list:
    return [
        name for name, value in cls.__dict__.items()
        if callable(value) and not name.startswith("_")
    ]


def main():
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print(f"- Card: {_callable_public_names(Card)}")
    print(f"- Combatable: {_callable_public_names(Combatable)}")
    print(f"- Magical: {_callable_public_names(Magical)}")

    c = EliteCard("Arcane Warrior", cost=3)

    print(f"\nPlaying {getattr(c, 'name', 'Unknown')}"
          f"({c.__class__.__name__}):\n")

    print("Combat phase:")
    attack_res = c.attack("Enemy")
    print("Attack result:", attack_res)

    defend_res = c.defend(5)
    print("Defense result:", defend_res)

    print("\nMagic phase:")
    spell_res = c.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_res)

    mana_res = c.channel_mana(3)
    print("Mana channel:", mana_res)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
