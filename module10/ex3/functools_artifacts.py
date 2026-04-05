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
        if operator == "add":
            return reduce(operator.add, spells)
        elif operator == "multiply":
            return reduce(operator.mul, spells)
        elif operator == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        elif operator == "min":
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
