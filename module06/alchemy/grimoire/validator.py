def validate_ingredients(ingredients: str) -> str:
    valid: list[str] = ["fire", "water", "earth", "air"]
    if isinstance(ingredients, str) and any(x in valid
                                            for x in ingredients.split()):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
