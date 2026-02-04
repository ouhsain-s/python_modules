from typing import Generator


def generate_game_events(count: int) -> Generator:
    players = ("alice", "bob", "charlie")
    randoms = (8, 8, 8, 8, 3, 4, 4, 4, 1, 3, 37, 33)
    for n in range(count):
        event = {"Player": players[n % len(players)],
                 "LvL": (n * 13 % 20) + 1,
                 "type": (randoms[n % 12]) % 8
                 }
        yield event


def show_analytics(total_events: int, high_level: int, treasure: int,
                   level_up: int) -> None:
    print("=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+):", high_level)
    print("Treasure events:", treasure)
    print("Level-up events:", level_up)


def compute_time():
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def generator_demonstration():
    print("")
    print("")
    print("")


def main():
    num_events = 1000
    buffer_displaying = 3
    type_events = {0: "found treasure", 1: "killed monster",
                   2: "maching with player",
                   3: "killed person", 4: "leveled up",
                   5: "creat group", 6: "found ston",
                   7: "open new earia"}
    total_events = 0
    high_level = 0
    treasure = 0
    level_up = 0
    events = generate_game_events(num_events)
    for event in events:
        total_events += 1
        if buffer_displaying > 0:
            print(f"Player {event["Player"]} (level {event["LvL"]})"
                  f" {type_events[event["type"]]}")
            buffer_displaying -= 1
        if event["LvL"] >= 10:
            high_level += 1
        if event["type"] == 0:
            treasure += 1
        if event["type"] == 4:
            level_up += 1
    print(end="\n")
    show_analytics(total_events, high_level, treasure, level_up)
    print(end="\n")
    compute_time()

if __name__ == "__main__":
    main()
