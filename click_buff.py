from math import ceil


class ClickBuff:
    __DMG_INCREASE_PER_LEVEL = 1.1
    __GOLD_COST_PER_LEVEL = 1.2

    def __init__(self, start_damage=1, start_gold_cost=3):
        self.start_damage = start_damage
        self.start_gold_cost = start_gold_cost
        self.current_level = 1

    @property
    def start_damage(self):
        return self.__start_damage

    @start_damage.setter
    def start_damage(self, value):
        if isinstance(value, int):
            self.__start_damage = value
        else:
            raise ValueError("Start damage must be integer.")

    @property
    def start_gold_cost(self):
        return self.__start_gold_cost

    @start_gold_cost.setter
    def start_gold_cost(self, value):
        if isinstance(value, int):
            self.__start_gold_cost = value
        else:
            raise ValueError("Start gold must be integer.")

    def level_up(self):
        self.start_damage = ceil(self.start_damage * ClickBuff.__DMG_INCREASE_PER_LEVEL)
        self.start_gold_cost = ceil(self.start_gold_cost * ClickBuff.__GOLD_COST_PER_LEVEL)
        self.current_level += 1

    def __repr__(self):
        return f"Current ClickBuff statistics:\n" \
               f"Damage - {self.start_damage}\n" \
               f"Gold cost for next level - {self.start_gold_cost}\n" \
               f"Current BUFF level - {self.current_level}"


# test = ClickBuff(1, 3) # this is optional and does not need to be typed
# test = ClickBuff(50, 50) # if you wish to start with higher values


# test = ClickBuff()
# for _ in range(5):
#     test.level_up()
#     print(test)
#     print()
