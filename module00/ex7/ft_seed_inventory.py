def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type} seeds: {quantity}", end="")
    if (unit == "packets"):
        unit = "packets available"
    if (unit == "grams"):
        unit = "grams total"
    if (unit == "area"):
        unit = "square meters"

    print(f" {unit}")
