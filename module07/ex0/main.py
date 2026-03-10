from ex0.CreatureCard import CreatureCard


def main() -> None:

    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(card.get_card_info())

    available_mana = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")

    playable = card.is_playable(available_mana)
    print("Playable:", playable)

    if playable:
        print("Play result:", card.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    attack1 = card.attack_target("Goblin Warrior")
    print("Attack result:", attack1)

    available_mana = 3
    print(f"\nTesting insufficient mana ({available_mana} available):")
    print("Playable:", card.is_playable(available_mana))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
