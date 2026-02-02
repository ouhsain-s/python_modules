def show_inventory_analysis(total_items: int, unique_items: int) -> None:
    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_items)


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


def classification_items(inventory_dict: dict, categories_dict: dict):
    scarce_avg = {"scarce_min": 0, "scarce_max": 4}
    moderate_avg = {"moderate_min": 5, "moderate_max": 9}
    abundant_avg = {"abundant_min": 10, "abundant_max": 9999}

    for key, value in inventory_dict.items():

        min_avg = scarce_avg.get("scarce_min")
        max_avg = scarce_avg.get("scarce_max")
        if value >= min_avg and value <= max_avg:
            categories_dict["scarce"].update({key: value})
        min_avg = moderate_avg.get("moderate_min")
        max_avg = moderate_avg.get("moderate_max")
        if value >= min_avg and value <= max_avg:
            categories_dict["moderate"].update({key: value})
        min_avg = abundant_avg.get("abundant_min")
        max_avg = abundant_avg.get("abundant_max")
        if value >= min_avg and value <= max_avg:
            categories_dict["abundant"].update({key: value})


def show_items_categories(categories_dict: dict):
    print("=== Item Categories ===")
    print("Moderate:", categories_dict.get("moderate"))
    print("Scarce:", categories_dict.get("scarce"))


def properties_dimo(inventory_dict: dict):
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory_dict.keys()))
    print("Dictionary values:", list(inventory_dict.values()))
    print("Sample lookup - 'sword' in inventory:", 'sword' in inventory_dict)


def managment_suggestions(categories_dict: dict):
    print_first_comma = False
    print("=== Management Suggestions ===")
    print("Restock needed: [", end="")
    for key, value in categories_dict["scarce"].items():
        if value <= 1:
            if print_first_comma:
                print(", ", end="")
            print_first_comma = True
            print(f"'{key}'", end="")
    print("]")


def inventory_manager():
    inventory_dict = {"potion": 5, "armor": 3, "shield": 2,
                      "sword": 1, "helmet": 1}
    total_items = 0

    for item in inventory_dict.values():
        total_items += item
    unique_items = len(inventory_dict.keys())

    most_abundant = ""

    for item in inventory_dict.keys():
        if (most_abundant == ""):
            most_abundant = item
        elif (inventory_dict.get(item)) > (inventory_dict.get(most_abundant)):
            most_abundant = item

    least_abundant = ""

    for item in inventory_dict.keys():
        if (least_abundant == ""):
            least_abundant = item
        elif inventory_dict.get(item) < inventory_dict.get(least_abundant):
            least_abundant = item

    scarce_dict = {}
    moderate_dict = {}
    abundant_dict = {}

    categories_dict = {"scarce": scarce_dict, "moderate": moderate_dict,
                       "abundant": abundant_dict}

    show_inventory_analysis(total_items, unique_items)
    print(end="\n")
    current_inventory(inventory_dict, total_items)
    print(end="\n")
    inventory_statistics(inventory_dict, most_abundant, least_abundant)
    print(end="\n")
    classification_items(inventory_dict, categories_dict)
    show_items_categories(categories_dict)
    managment_suggestions(categories_dict)
    properties_dimo(inventory_dict)


if __name__ == "__main__":
    inventory_manager()
