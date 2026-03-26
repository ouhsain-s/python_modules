from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    lightning = SpellCard("Lightning Bolt", 3, "common", "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2,
                                "rare", 5, "Permanent: +1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, "legendary", 8, 8)

    deck.add_card(lightning)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    for _ in range(len(deck.cards)):
        c = deck.draw_card()
        tp = c.__class__.__name__.strip("Card")
        print(f"Drew: {c.name} ({tp})")
        print("Play result:", c.play({}), "\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
