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
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> str:
            try:
                if args[0] >= min_power:
                    return (func(*args, **kwargs))

            except (TypeError, KeyError, IndexError) as e:
                print("Error:", e)
                chois = input("if you want to creat decorator"
                              " by defualt just pass \'y\'=> ")
                if chois == "y":
                    return wrapper(10, type_p='AC')
                exit(1)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable):
        def wrapper(*args: tuple, **kwargs: dict) -> None:
            for n in range(1, max_attempts):
                try:
                    func(*args, **kwargs)
                    return
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {n}/{max_attempts})")
            print(f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for c in name:
                if not c.isalpha() and c != ' ':
                    return False
            return True
        return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        if self.validate_mage_name(self.cast_spell):
            
        else:
            return "Insufficient power for this spell"


def testing_spell_timer() -> None:
    @spell_timer
    def fireball():
        for _ in range(10000000):
            pass

    print("Testing spell timer...")
    fireball()
    print(f"Result {fireball.__name__.capitalize()} cast!")


def testing_power_validator() -> None:
    print("Testing power validator...")
    my_dec = power_validator(10)

    @my_dec
    def get_valid_power(power: int, type_p: str) -> str:
        if type_p == 'AC':
            return f"the power {power} is valid"
        else:
            return f"{type_p} power is not supported"

    print("result of validation:")
    print(get_valid_power(23, type_p="AC"))


def testing_retry_spell() -> None:
    print("Testing retrying spell...")
    my_dec = retry_spell(3)

    @my_dec
    def n_valid_testing(value: int) -> None:
        raise ValueError()
        print(value)

    @my_dec
    def valid_test() -> None:
        print("Waaaaaaagh spelled !")

    n_valid_testing(5)
    print()
    valid_test()


if __name__ == "__main__":
    testing_power_validator()
