from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effect_text = self.resolve_effect([])
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = effect_text
        return game_state

    def resolve_effect(self, targets: list) -> str:
        if self.effect_type == "damage":
            return f"Deal {self.cost} damage to target"
        if self.effect_type == "heal":
            return f"Restore {self.cost} health to target"
        if self.effect_type == "buff":
            return "Increase target power"
        if self.effect_type == "debuff":
            return "Reduce target power"
        return "Unknown spell effect"
