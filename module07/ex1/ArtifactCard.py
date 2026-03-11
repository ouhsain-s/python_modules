from ex0.Card import Card
from typing import Dict, Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = int(durability)
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        effect_text = self.resolve_effect([])
        game_state["card_played"] = self.name
        game_state["mana_used"] = self.cost
        game_state["effect"] = effect_text
        return game_state

    def activate_ability(self) -> Dict[str, Any]:
        if self.durability <= 0:
            return {"activated": False, "reason": "broken"}
        self.durability -= 1
        res = {"activated": True, "name": self.name, "effect": self.effect,
               "remaining": self.durability}
        if self.durability <= 0:
            res["destroyed"] = True
        return res
