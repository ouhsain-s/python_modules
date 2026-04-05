from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


class unexpected_operation(Exception):
    pass


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0

    try:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        elif operation == "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        else:
            raise unexpected_operation("Error: "
                                       f"no operatoin named {operation}")
    except unexpected_operation as e:
        print(e)
        exit(1)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {'f1': partial(base_enchantment, 50, "sheld"),
            'f2': partial(base_enchantment, 50, "Sword"),
            'f3': partial(base_enchantment, 50, "crestal boll")}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def implement_spell(spell_type: Any) -> str:
        return "Unknown spell type"

    @implement_spell.register(int)
    def _(spell_type: int) -> str:
        return f"Damage spell: {spell_type} damage"

    @implement_spell.register(str)
    def _(spell_type: str) -> str:
        return f"Enchantment: {spell_type}"

    @implement_spell.register(list)
    def _(spell_type: list) -> str:
        return f"Multi-cast: {len(spell_type)} spells"
    return implement_spell


def test_spell_reducer():
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print()


def test_memoized_fibonacci():
    print("Testing memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}):", memoized_fibonacci(n))
    print()


def test_spell_dispatcher():
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(10.3))
    print()


def test_partial_enchanter():
    print("Testing partial_enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} spell of {power} power hits {target}"

    partials = partial_enchanter(base_enchantment)
    for name, func in partials.items():
        print(f"{name}:", func("Dragon"))
    print()


# ==== Run all tests ====
if __name__ == "__main__":
    test_spell_reducer()
    test_memoized_fibonacci()
    test_spell_dispatcher()
    test_partial_enchanter()
