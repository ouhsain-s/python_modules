from typing import Dict, Any, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, attack_power: int = 5,
                 defense: int = 3, mana: int = 7):
        super().__init__(name, cost)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana
        self.max_mana = mana

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        game_state = game_state or {}
        game_state["card_played"] = getattr(self, "name", "Unknown")
        game_state["mana_used"] = getattr(self, "cost", 0)
        return game_state

    def attack(self, target) -> Dict[str, Any]:
        damage = self.attack_power
        return {
            "attacker": getattr(self, "name", "Unknown"),
            "target": target,
            "damage": damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(self.defense, incoming_damage)
        taken = max(0, incoming_damage - self.defense)
        still_alive = True
        return {
            "defender": getattr(self, "name", "Unknown"),
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": still_alive,
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {"attack_power": self.attack_power, "defense": self.defense}

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        mana_cost = max(1, len(targets) + (len(spell_name) // 6))
        used = min(self.mana, mana_cost)
        self.mana -= used
        return {
            "caster": getattr(self, "name", "Unknown"),
            "spell": spell_name,
            "targets": targets,
            "mana_used": used,
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict[str, Any]:
        return {"mana": self.mana, "max_mana": self.max_mana}
