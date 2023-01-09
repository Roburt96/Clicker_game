from math import ceil
from statistics import *


class Worker:
    __GOLD_INCREASE_PER_LEVEL = 1.2
    __SEC_DECREASE_PER_6_LEVELS = 2
    __GOLD_COST_PER_LEVEL = 1.7

    def __init__(self, start_gold=0, seconds_for_gold=15, start_gold_cost=18):
        self.start_gold = start_gold
        self.start_gold_cost = start_gold_cost
        self.seconds_for_gold = seconds_for_gold
        self.current_level = 0

    # @property
    # def start_gold(self):
    #     return self.__start_gold
    #
    # @start_gold.setter
    # def start_gold(self, value):
    #     if isinstance(value, int):
    #         self.__start_gold = value
    #     else:
    #         raise ValueError("Start gold must be integer.")
    #
    # @property
    # def start_gold_cost(self):
    #     return self.__start_gold_cost
    #
    # @start_gold_cost.setter
    # def start_gold_cost(self, value):
    #     if stat_test.current_gold >= Worker.start_gold_cost:
    #         print('Upgrade')
    #
    #         self.__start_gold_cost = value
    #     else:
    #         raise ValueError("Start gold cost must be integer.")
    #
    # @property
    # def seconds_for_gold(self):
    #     return self.__seconds_for_gold
    #
    # @seconds_for_gold.setter
    # def seconds_for_gold(self, value):
    #     if isinstance(value, int):
    #         self.__seconds_for_gold = value
    #     else:
    #         raise ValueError("Seconds must be positive number.")

    def level_up(self):
        if self.current_level == 0:
            if stat_test.current_gold >= self.start_gold_cost:
                self.current_level += 1
                self.start_gold = 3
                stat_test.current_gold -= self.start_gold_cost
                if stat_test.current_gold < 0:
                    stat_test.current_gold = 0
            else:
                print('no gold')

        else:
            self.start_gold = ceil(self.start_gold * Worker.__GOLD_INCREASE_PER_LEVEL)
            self.start_gold_cost = ceil(self.start_gold_cost * Worker.__GOLD_COST_PER_LEVEL)
            statis_test.worker_gold += ceil(self.start_gold * Worker.__GOLD_INCREASE_PER_LEVEL)
            if self.current_level % 6 == 0:
                self.seconds_for_gold -= Worker.__SEC_DECREASE_PER_6_LEVELS
                if self.seconds_for_gold <= 0:
                    self.seconds_for_gold = 1



stat_test = Statistics()