class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        created = []
        try:
            d = self.factory.create_creature("Fire Dragon")
            created.append(d)
        except Exception:
            pass
        try:
            g = self.factory.create_creature("Goblin Warrior")
            created.append(g)
        except Exception:
            pass
        try:
            s = self.factory.create_spell("Lightning Bolt")
            created.append(s)
        except Exception:
            pass

        hand = created[:]
        self.cards_created += len(created)

        result = self.strategy.execute_turn(hand, [])
        self.turns += 1
        self.total_damage += int(result.get("damage_dealt", 0))

        return {
            "hand": hand,
            "result": result
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used":
            self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
