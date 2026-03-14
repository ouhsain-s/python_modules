from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage = 0

        for card in hand:
            try:
                cost = card.cost
                name = card.name
            except AttributeError:
                cost = 0
                name = card.__class__.__name__

            if isinstance(cost, (int, float)) and cost <= 3:
                cards_played.append(name)
                mana_used += cost
                damage += int(cost) + 1.5

            elif not isinstance(cost, (int, float)):
                lname = str(name).lower()
                if "lightning" in lname or "bolt" in lname or "fire" in lname:
                    cards_played.append(name)
                    mana_used += 3
                    damage += 3 + 1
            battlefield = cards_played
        return {
            "cards_played": battlefield,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": int(damage)
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets)
