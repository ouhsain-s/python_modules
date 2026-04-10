import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def timer(*args: tuple, **kwargs: dict):
        start = time.time()
        print(f"Casting {func.__name__}")
        res = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.6f} seconds")
        return res
    return timer


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def validate(*args: tuple, **kwargs: dict) -> str:
            power = kwargs.get('power')
            power = args[-1] if power is None else power
            if power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)
        return validate
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def retry(*args: tuple, **kwargs: dict) -> str:
            for attempt in range(1, max_attempts + 2):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt <= max_attempts:
                        print(f"Spell failed, retrying... (attempt \
{attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after \
{max_attempts} attempts"
        return retry
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all([c.isalpha() or c == " " for c in name])

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def cast(spell: str) -> str:
    print(f"Casting {spell}...")
    return f"{spell} cast!"


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {cast('fireball')}")
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("merlin"))
    print(guild.validate_mage_name("32"))
    print(guild.cast_spell('Lightning', 15))
    print(guild.cast_spell('Lightning', 5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)