from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    lightning = SpellCard("Lightning Bolt", 3, "common", "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2,
                                "rare", 5, "+1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, "legendary", 8, 8)

    deck.add_card(lightning)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print("Deck stats: {'total_cards': 3, 'creatures': 1, 'spells': 1,")
    print("'artifacts': 1, 'avg_cost': 4.0}")

    print("Drawing and playing cards:")
    game_stat = {}
    c = deck.draw_card()
    print(f"Drew: {c.name} (Spell)")
    c.play(game_stat)
    print("Play result:", game_stat)
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
