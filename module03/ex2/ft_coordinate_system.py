import math


def parse_coordinate(pos_str: str) -> tuple:
    try:
        x, y, z = [int(i) for i in pos_str.split(",")]
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{pos_str}\"")
        print("Error parsing coordinates:", e)
        print("Error details - Type: ValueError, Args:", e.args)
        return None
    pos = (x, y, z)
    return (pos)


def get_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return (dist)


def show_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    start = "0, 0, 0"
    dest = "10, 20, 5"
    pos1_x1 = parse_coordinate(start)
    pos2_x1 = parse_coordinate(dest)
    if pos1_x1 and pos2_x1:
        distance = get_distance(pos1_x1, pos2_x1)

        print("Position created:", pos2_x1)
        print(f"Distance between {pos1_x1} and {pos2_x1}:"
              f" {distance:.2f}")

    print(end="\n")
    dest = "3,4,0"
    pos1_x2 = parse_coordinate(start)
    pos2_x2 = parse_coordinate(dest)
    if pos1_x2 and pos2_x2:
        distance = get_distance(pos1_x2, pos2_x2)
        print(f"Parsing coordinates: \"{dest}\"")
        print("Parsed position:", pos2_x2)
        print(f"Distance between {pos1_x2} and {pos2_x2}: {distance}")

    print(end="\n")
    dest = "abc,def,ghi"
    pos1_x3 = parse_coordinate(start)
    pos2_x3 = parse_coordinate(dest)
    if pos1_x3 and pos2_x3:
        distance = get_distance(pos1_x3, pos2_x3)
        print("Distance is ", distance)

    print("\nUnpacking demonstration:")
    dest = "3,4,0"
    tst_unpacking = parse_coordinate(dest)
    if tst_unpacking:
        x, y, z = tst_unpacking
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    show_coordinate_system()
