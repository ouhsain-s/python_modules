def show_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
                'first_kill'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                  'perfectionist'])
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print("\n=== Achievement Analytics ===")
    all_unique = alice.union(bob, charlie)
    rave = alice.difference(bob, charlie).union(
        bob.difference(alice, charlie),
        charlie.difference(bob, alice))
    common = alice.intersection(bob, charlie)
    len_all_unique = len(all_unique)
    print("All unique achievements:", all_unique)
    print("Total unique achievements:", len_all_unique)
    print("Common to all players:", common)
    print("Rare achievements (1 player):", rave)
    print(end="\n")
    bob_vs_alice = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print("Alice vs Bob common:", bob_vs_alice)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    show_achievement_tracker()
