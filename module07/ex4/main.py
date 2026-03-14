from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===")

platform = TournamentPlatform()

print("\nRegistering Tournament Cards...")
dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 1200)
wizard = TournamentCard("wizard_001", "Ice Wizard", 3, "Epic", 1150)

for card in [dragon, wizard]:
    platform.register_card(card)
    info = card.get_rank_info()
    print(f"{info['name']} (ID: {info['card_id']}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {info['rating']}")
    print(f"- Record: {info['record']}")

print("\nCreating tournament match...")
match_result = platform.create_match("dragon_001", "wizard_001")
print(f"Match result: {match_result}")

print("Tournament Leaderboard:")
leaderboard = platform.get_leaderboard()
for entry in leaderboard:
    print(f"{entry['position']}. {entry['name']} - Rating: {entry['rating']}"
          f" ({entry['record']})")

print("Platform Report:")
report = platform.generate_tournament_report()
print(report)

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
