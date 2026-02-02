def show_inventory_analysis(total_items: int, unique_ites: int) -> None:
    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_ites)


def current_inventory(inventory_dict: dict, total_items: int):
    print("=== Current Inventory ===")
    for item in inventory_dict.keys():
        current_value = inventory_dict.get(item)
        if current_value > 1:
            statment = "units"
        else:
            statment = "unit"
        persontag = (current_value * 100 / total_items)
        print(f"{item}: {current_value} {statment} ({persontag:.1f}%)")


def inventory_statistics(inventory_dict: dict, most: str, least: str):
    most_value = inventory_dict.get(most)
    if most_value > 1:
        statment = "units"
    else:
        statment = "unit"
    print(f"Most abundant: {most} ({most_value} {statment})")
    least_value = inventory_dict.get(least)
    if least_value > 1:
        statment = "units"
    else:
        statment = "unit"
    print(f"Least abundant: {least} ({least_value} {statment})")


def inventory_manager():
    inventory_dict = {"potion": 5, "armor": 3, "shield": 2,
                      "sowrd": 1, "helmet": 1}
    total_items = 0
    for item in inventory_dict.values():
        total_items += item
    unique_ites = len(inventory_dict.keys())

    most_aboundant = ""

    for item in inventory_dict.keys():
        if (most_aboundant == ""):
            most_aboundant = item
        elif (inventory_dict.get(item)) > (inventory_dict.get(most_aboundant)):
            most_aboundant = item

    least_aboundant = ""

    for item in inventory_dict.keys():
        if (least_aboundant == ""):
            least_aboundant = item
        elif inventory_dict.get(item) < inventory_dict.get(least_aboundant):
            least_aboundant = item

    show_inventory_analysis(total_items, unique_ites)
    current_inventory(inventory_dict, total_items)
    inventory_statistics(inventory_dict, most_aboundant, least_aboundant)


if __name__ == "__main__":
    inventory_manager()
