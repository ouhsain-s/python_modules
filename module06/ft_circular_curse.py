from alchemy.grimoire import record_spell, validate_ingredients


def record_spell_injected(spell_name: str, ingredients: str,
                          validator_fn) -> str:
    # using dependency injection to avoid Circular import
    valid = validator_fn(ingredients)
    if valid.endswith("INVALID"):
        return f"Spell rejected: {spell_name} ({valid})"
    else:
        return f"Spell recorded: {spell_name} ({valid})"


def main() -> None:
    try:
        print("\n=== Circular Curse Breaking ===\n")
        print("Testing ingredient validation:")
        print("validate_ingredients(\"fire air\"): "
              + validate_ingredients("fire air"))
        print("validate_ingredients(\"dragon scales\"): "
              + validate_ingredients("dragon scales"))
        print("\nTesting spell recording with validation:")
        print(f"record_spell(\"Fireball\", \"fire air\"): \
        {record_spell('Fireball', 'fire air')}")
        print(f"record_spell(\"Dark Magic\", \"shadow\"): \
        {record_spell_injected('Dark Magic', 'shadow', validate_ingredients)}")
        print("\nTesting late import technique:")
        print(f"record_spell(\"Lightning\", \"air\"): \
        {record_spell('Lightning', 'air')}")
        print("\nCircular dependency curse avoided using late imports!")
        print("All spells processed safely!")
    except ImportError:
        print("Warning: Circular import detected")


if __name__ == "__main__":
    main()
