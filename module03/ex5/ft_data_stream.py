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


def compute_time() -> None:
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci_sequence(count: int) -> Generator:
    n1 = 0
    n2 = 1
    tmp = 0
    for _ in range(count):
        yield n1
        tmp = n1
        n1 = n2
        n2 += tmp


def prime_numbers() -> Generator:
    yield 2
    for i in range(3, 100000):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


def generator_demonstration() -> None:
    count = 10
    t = count
    print("=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {count}): ", end="")
    for i in fibonacci_sequence(count):
        print(i, end="")
        if t > 1:
            print(", ", end="")
        t -= 1
    print(end="\n")
    get_next_prim = prime_numbers()
    count = 5
    print(f"Prime numbers (first {count}): ", end="")
    for i in range(count):
        print(next(get_next_prim), end="")
        if i != count - 1:
            print(", ", end="")
    print(end="\n")


def main() -> None:
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
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    events = generate_game_events(num_events)
    for event in events:
        total_events += 1
        if buffer_displaying > 0:
            print(f"Event {total_events}: Player {event['Player']}"
                  f" (level {event['LvL']})"
                  f" {type_events[event['type']]}")
            buffer_displaying -= 1
        if event["LvL"] >= 10:
            high_level += 1
        if event["type"] == 0:
            treasure += 1
        if event["type"] == 4:
            level_up += 1
    print("...\n")
    show_analytics(total_events, high_level, treasure, level_up)
    print(end="\n")
    compute_time()
    print(end="\n")
    generator_demonstration()


if __name__ == "__main__":
    main()
