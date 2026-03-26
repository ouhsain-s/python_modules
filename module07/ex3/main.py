from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def fmt_card(card) -> None:
    if card is None:
        return "None"
    try:
        name = card.name
        cost = card.cost
        return f"{name} ({cost})"
    except AttributeError:
        return "Error"


def main() -> None:
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

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
