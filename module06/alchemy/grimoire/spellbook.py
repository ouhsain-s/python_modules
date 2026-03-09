def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator
    result = validator.validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    else:
        return f"Spell recorded: {spell_name} ({result})"
