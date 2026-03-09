def validate_ingredients(ingredients: str) -> str:
    valid: list[str] = ["fire", "water", "earth", "air"]
    return f"{ingredients} - VALID" if isinstance(ingredients, str) \
        and ingredients and any(x in valid for x in ingredients.split())\
        else f"{ingredients} - INVALID"
