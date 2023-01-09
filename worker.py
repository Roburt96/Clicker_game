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
            self.__seconds_for_gold = value
        else:
            raise ValueError("Seconds must be positive number.")

    def level_up(self, stats):
        if stats.current_gold >= self.start_gold_cost:
            if self.current_level == 0:
                self.current_level += 1
                self.start_gold = 3
                stats.current_gold -= self.start_gold_cost
                self.start_gold_cost = ceil(self.start_gold_cost * Worker.__GOLD_COST_PER_LEVEL)
            else:
                self.start_gold = ceil(self.start_gold * Worker.__GOLD_INCREASE_PER_LEVEL)
                self.start_gold_cost = ceil(self.start_gold_cost * Worker.__GOLD_COST_PER_LEVEL)
                stats.current_gold -= self.start_gold_cost
                stats.current_gold += ceil(self.start_gold * Worker.__GOLD_INCREASE_PER_LEVEL)
                self.current_level += 1

        else:
            print('no gold')

    def add_gold_from_worker(self, sec, stats):
        if self.current_level % 6 == 0:
            self.seconds_for_gold -= Worker.__SEC_DECREASE_PER_6_LEVELS
            if self.seconds_for_gold <= 0:
                self.seconds_for_gold = 1

        if int(sec) % self.seconds_for_gold == 0:
            print(self.start_gold)
            stats.current_gold += self.start_gold
            stats.total_gold += self.start_gold


stat_test = Statistics()