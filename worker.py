from math import ceil


class Worker:
    __GOLD_INCREASE_PER_LEVEL = 1.2
    __SEC_DECREASE_PER_6_LEVELS = 2
    __GOLD_COST_PER_LEVEL = 1.7

    def __init__(self, start_gold=1, seconds_for_gold=15, start_gold_cost=18):
        self.start_gold = start_gold
        self.start_gold_cost = start_gold_cost
        self.__seconds_for_gold = seconds_for_gold
        self.current_level = 0

    @property
    def start_gold(self):
        return self.__start_gold

    @start_gold.setter
    def start_gold(self, value):
        if isinstance(value, int):
            self.__start_gold = value
        else:
            raise ValueError("Start gold must be integer.")

    @property
    def start_gold_cost(self):
        return self.__start_gold_cost

    @start_gold_cost.setter
    def start_gold_cost(self, value):
        if isinstance(value, int):
            self.__start_gold_cost = value
        else:
            raise ValueError("Start gold cost must be integer.")

    @property
    def seconds_for_gold(self):
        return self.__seconds_for_gold

    @seconds_for_gold.setter
    def seconds_for_gold(self, value):
        if isinstance(value, int):
            self.__start_gold_cost = value
        else:
            raise ValueError("Seconds must be positive number.")

    def level_up(self):
        self.start_gold = ceil(self.start_gold * Worker.__GOLD_INCREASE_PER_LEVEL)
        self.current_level += 1
        self.start_gold_cost = ceil(self.start_gold_cost * Worker.__GOLD_COST_PER_LEVEL)
        if self.current_level % 6 == 0:
            self.seconds_for_gold -= Worker.__SEC_DECREASE_PER_6_LEVELS
            if self.seconds_for_gold < 0:
                self.seconds_for_gold = 0

    def __repr__(self):
        return f"Worker status:\n" \
               f"Seconds to make gold: {self.__seconds_for_gold}\n" \
               f"Gold cost for next level: {self.__start_gold_cost}\n" \
               f"Gold making: {self.__start_gold}\n" \
               f"Current WORKER level: {self.current_level}"


