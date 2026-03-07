from . import elements


def healing_potion() -> str:
    return (f"Healing potion brewed with {elements.create_fire()} and"
            f"{elements.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {elements.create_earth()}"
            f"and {elements.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {elements.create_air()}"
            f"and{elements.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: "
            f"{elements.create_water()}, {elements.create_fire()},"
            f"{elements.create_earth()}, {elements.create_air()}"
            )
