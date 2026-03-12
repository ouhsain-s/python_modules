"""Simple demonstration script for ex2 Ability System.
Run with: python3 -m ex2.main
"""
from ex2.EliteCard import EliteCard
from ex0.Card import Card


def _callable_public_names(obj) -> list:
    return sorted([
        name for name in dir(obj)
        if not name.startswith("_") and callable(getattr(obj, name))
    ])


def main():
    print("=== DataDeck Ability System ===")
    print()

    # show capabilities
    print("EliteCard capabilities:")
    print(f"- Card: {_callable_public_names(Card)}")
    print(f"- Combatable: {['attack', 'defend', 'get_combat_stats']}")
    print(f"- Magical: {['cast_spell', 'channel_mana', 'get_magic_stats']}\n")

    c = EliteCard("Arcane Warrior", cost=3)

    print(f"Playing {getattr(c, 'name', 'Unknown')} (Elite Card):\n")
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