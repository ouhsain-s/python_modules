from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:

        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be positive")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be positive")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = "Creature summoned to battlefield"
        return game_state

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
