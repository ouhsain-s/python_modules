from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def power_supply(supply: int) -> int:
        nonlocal power
        power += supply
        return power
    return power_supply


def enchantment_factory(enchantment_type: str) -> Callable:
    def get_item_status(item: str) -> str:
        return (f"{enchantment_type} {item}")
    return get_item_status


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        geted = ""
        try:
            geted = vault[key]
        except KeyError:
            geted = "Memory not found"
        finally:
            return geted

    return {'Store': store, 'Recall': recall}


def testing_mage_counter() -> None:
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()

    print("counter_a call 1:", a())
    print("counter_a call 2:", a())
    print("counter_b call 1:", b())


def testing_spell_accumulator():
    base = 100
    add = 20

    power_supply = spell_accumulator(base)
    print("Testing spell accumulator...")
    print(f"Base {base}, add {add}:", power_supply(add))
    add = 30
    print(f"Base {base}, add {add}:", power_supply(add))


def testing_enchantment_factory():

    print("Testing enchantment factory...")
    stat1 = enchantment_factory("Flaming")
    print(stat1("Sword"))
    stat2 = enchantment_factory("Frozen")
    print(stat2("Shield"))


def testing_memory_vault() -> None:
    print("Testing memory vault...")
    my_secret_memory = memory_vault()

    try:
        key, value = 'secret', 42
        my_secret_memory['Store'](key, value)
        print(f"Store '{key}' = {value}")

        value = my_secret_memory['Recall'](key)
        print(f"Recall '{key}': {value}")
        key = 'unknow'
        value = my_secret_memory['Recall'](key)
        print(f"Recall '{key}': {value}")
    except KeyError as e:
        print("Not found any key named", e)


if __name__ == "__main__":
    testing_mage_counter()
    print()
    testing_spell_accumulator()
    print()
    testing_enchantment_factory()
    print()
    testing_memory_vault()
