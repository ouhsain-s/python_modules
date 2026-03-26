from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = int(durability)
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = self.effect
        return game_state

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"activated": False, "reason": "broken"}
        self.durability -= 1
        res = {"activated": True, "name": self.name, "effect": self.effect}
        if self.durability <= 0:
            res["destroyed"] = True
        return res
