from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy import transmutation
import alchemy


def testing_absolute_imports() -> None:
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def testing_releative_imports() -> None:
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {transmutation.elixir_of_life()}")


def testing_package_access() -> None:
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")
    testing_absolute_imports()
    testing_releative_imports()
    testing_package_access()
