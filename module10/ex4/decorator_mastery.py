import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> None:
        print(f"Casting {func.__name__}...")
        start = time.time()
        func()
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(*args: tuple, **kwargs: dict) -> Callable:
        def wrapper(*args: tuple, **kwargs: dict) -> str:
            if args[0] >= min_power:
                kwargs['func'](args[0])
                return ""
            return "Insufficient power for this spell"
        return wrapper
    return decorator




# def retry_spell(max_attempts: int) -> Callable

# class MageGuild:
#     @staticmethod
#     def validate_mage_name(name: str) -> bool
#     def cast_spell(self, spell_name: str, power: int) -> str


@spell_timer
def fireball():
    for _ in range(10000000):
        pass


if __name__ == "__main__":
    print("Testing spell timer...")
    fireball()
    print(f"Result {fireball.__name__.capitalize()} cast!")
