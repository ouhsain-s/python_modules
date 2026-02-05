
def list_comprehension_examples():
    players = [("alice", 2300, True), ("bob", 1800, True),
               ("charlie", 2150, False), ("diana", 2050, True),]
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000):", [n[0] for n in players if n[1] >= 2000])
    print("Scores doubled:", [n[1] * 2 for n in players])
    print("Active players:", [n[0] for n in players if n[2]])


def dict_comprehension_examples():
    players = [("alice", 2300, True, 5), ("bob", 1800, True, 3),
               ("charlie", 2150, False, 7), ("diana", 2050, True, 0)]

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

    achievements = [
                    "first_kill", "level_10", "boss_slayer", "first_kill",
                    "level_5", "boss_slayer", "level_10"]

    player_regoin = ["north", "east", "east", "north"]

    unique_players = {player for player in players}
    unique_achive = {achive for achive in achievements}
    active_regoins = {regoin for regoin in player_regoin}
    print("=== Set Comprehension Examples ===")
    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achive)
    print("Active regions:", active_regoins)


def combined_analysis():
    players = [("alice", 2300, True, 5), ("bob", 1800, True, 3),
               ("charlie", 2150, False, 7), ("diana", 2050, True, 0)]
    achievements = [
                    "first_kill", "level_10", "boss_slayer", "first_kill",
                    "level_5", "boss_slayer", "level_10"]
    total_players = len([item for item in players])
    total_unique = len({achive for achive in achievements})
    total_score = sum([scr for _, scr, _, _ in players])
    max_scor = max([scr for _, scr, _, _ in players])
    top_performer = [top for top in players if top[1] == max_scor]
    print("=== Combined Analysis ===")
    print("Total players:", total_players)
    print("Total unique achievements:", total_unique)
    print("Average score:", total_score / total_players)
    print(f"Top performer: {top_performer[0][0]}"
          f" ({top_performer[0][1]} points,"
          f" {top_performer[0][3]} achievements)")


def main():
    list_comprehension_examples()
    print(end="\n")
    dict_comprehension_examples()
    print(end="\n")
    set_comprehension_examples()
    print(end="\n")
    combined_analysis()


if __name__ == "__main__":
    main()
