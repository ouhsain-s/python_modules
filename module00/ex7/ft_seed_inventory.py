def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    capitalized_seed = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{capitalized_seed} seeds: {quantity}", end="")
        unit = "packets available"
        print(f" {unit}")
    elif (unit == "grams"):
        print(f"{capitalized_seed} seeds: {quantity}", end="")
        unit = "grams total"
        print(f" {unit}")
    elif (unit == "area"):
        print(f"{capitalized_seed} seeds: covers {quantity}", end="")
        unit = "square meters"
        print(f" {unit}")
    else:
        print("Unknown unit type")
        return
