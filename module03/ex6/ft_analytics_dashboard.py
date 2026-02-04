
def list_comprehension_examples():
    players = [("alice", 2300, True), ("bob", 1800, True),
               ("charlie", 2150, False), ("diana", 2050, True),]
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000):", [n[0] for n in players if n[1] >= 2000])
    print("Scores doubled:", [n[1] * 2 for n in players])
    print("Active players:", [n[0] for n in players if n[2]])


def dict_comprehension_examples():
    players = [("alice", 2300, True, 5), ("bob", 1800, True, 3),
               ("charlie", 2150, False, 7), ("diana", 2050, True, 0),]

    ctegories = {'high':
                 len([n for n in players if n[1] >= 2000]),
                 'medium':
                 len([n for n in players if n[1] < 2000 and n[1] >= 1000]),
                 'low':
                 len([n for n in players if n[1] < 1000])}

    print("=== Dict Comprehension Examples ===")
    print("Player scores:", {player[0]: player[1] for player in players})
    print("Score categories:", ctegories)
    print("Achievement counts:", {name: achive for name, _, _, achive in
                                  players if achive > 0})


def set_comprehension_examples():
    players = ["alice", "bob", "charlie", "alice", "diana", "bob"]

    achievements = {
    "alice": ["first_kill", "level_10", "boss_slayer"],
    "bob": ["first_kill", "level_5"],
    "charlie": ["boss_slayer", "level_10"]}

    player_regions = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "north"}

    unique_player = {player for player in players}
    unique_achive = {achive for achive in achievements}
    active_regoins = {regoin for regoin in player_regions}
    print("=== Dict Comprehension Examples ===")
    print("Achievement counts:", unique_player)
    print("Unique achievements:", unique_achive)
    print("Active regions:", active_regoins)
    

set_comprehension_examples()
