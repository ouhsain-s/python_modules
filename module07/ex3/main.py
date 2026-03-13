from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def fmt_card(card):
    if card is None:
        return "None"
    name = getattr(card, "name", None)
    cost = getattr(card, "cost", None)
    if name is None:
        name = getattr(card, "__class__", type(card)).__name__
    if cost is None:
        return f"{name}"
    return f"{name} ({cost})"


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print(end="\n")

    print("Simulating aggressive turn...")
    data = engine.simulate_turn()
    hand = data["hand"]

    print("Hand:", [fmt_card(c) for c in hand])

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", data["result"])

    print("Game Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
