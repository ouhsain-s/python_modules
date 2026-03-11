
def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator
    valid_stat = validator.validate_ingredients(ingredients)
    if "INVALID" in valid_stat:
        return f"Spell rejected: {spell_name} ({valid_stat})"
    else:
        return f"Spell recorded: {spell_name} ({valid_stat})"
