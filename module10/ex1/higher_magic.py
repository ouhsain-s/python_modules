from collections.abc import Callable
from typing import Union


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> Union[Callable, str]:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spells(target: str, power: int) -> list[str]:
        spells_output = [output(target, power) for output in spells]
        return spells_output
    return sequence_spells


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def testing_spell_combiner() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")


def testing_power_amplifier() -> None:
    print("Testing power amplifier...")
    print_status_only = True
    original_power = 10
    amplifier_power = 3
    amplified_fireball = power_amplifier(fireball, amplifier_power)

    amplified_result = amplified_fireball("Dragon", original_power)

    print(f"Original: {original_power},"
          f" Amplified: {original_power * amplifier_power}")
    if not print_status_only:
        print(amplified_result)


if __name__ == "__main__":
    print()
    testing_spell_combiner()
    print()
    testing_power_amplifier()
