from math import ceil
from click_buff import ClickBuff
from statistics import Statistics


class Monster:
    __GOLD_INCREASE_PER_NORMAL_KILL = 1.2
    __GOLD_INCREASE_PER_BOSS_KILL = 1.4
    __BOSS_HEALTH_INCREASE = 12.5
    __MONSTER_HEALTH_INCREASE_AFTER_LEVEL_10 = 2.3

    def __init__(self, monster_hp=12, gold_drop_normal_monster=1, gold_per_boss_kill=20):
        self.monster_hp = monster_hp
        self.attacked_monster = self.monster_hp
        self.boss_health = monster_hp * Monster.__BOSS_HEALTH_INCREASE
        self.gold_drop_normal_monster = gold_drop_normal_monster
        self.gold_per_boss_kill = gold_per_boss_kill
        self.current_level = 1
        self.dead_monster = False
        self.current_boss = 0

    @property
    def monster_hp(self):
        return self.__start_monster_hp

    @monster_hp.setter
    def monster_hp(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__start_monster_hp = value
        else:
            raise ValueError("Monster HP must be INTEGER and it has to be more than 0.")

    @property
    def gold_drop_normal_monster(self):
        return self.__gold_drop_normal_monster

    @gold_drop_normal_monster.setter
    def gold_drop_normal_monster(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__gold_drop_normal_monster = value
        else:
            raise ValueError("Gold drop must be INTEGER and it has to be more than 0.")

    @property
    def gold_per_boss_kill(self):
        return self.__gold_per_boss_kill

    @gold_per_boss_kill.setter
    def gold_per_boss_kill(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__gold_per_boss_kill = value
        else:
            raise ValueError("BOSS gold drop must be INTEGER and it has to be more than 0.")

    def attack_monster(self, click_damage: ClickBuff):
        if self.attacked_monster - click_damage.start_damage > 0:
            self.attacked_monster -= click_damage.start_damage
        else:
            """
            TO DO:
            BEFORE IT GOES TO PREPARE_NEXT_LEVEL(), IT HAS TO REWARD THE PLAYER WITH GOLD
            ALSO PARAMETER MUST BE PASSED ,TO ATTACK_MONSTER() METHOD
            """
            self.dead_monster = True

    def check_if_dead(self):
        if self.dead_monster:
            self.dead_monster = False
            return True

    def prepare_next_level(self):

        self.current_level += 1
        if self.current_level < 10:
            self.gold_drop_normal_monster = 1
        elif self.check_for_boss():
            self.current_boss += 1
            self.gold_drop_normal_monster = ceil(self.gold_drop_normal_monster *
                                                 Monster.__GOLD_INCREASE_PER_NORMAL_KILL)
            self.boss_health = ceil(self.monster_hp * Monster.__BOSS_HEALTH_INCREASE)
            self.monster_hp = int(self.monster_hp * Monster.__MONSTER_HEALTH_INCREASE_AFTER_LEVEL_10)
            if self.current_boss == 1:
                self.gold_per_boss_kill = 20
            else:
                self.gold_per_boss_kill = ceil(self.gold_per_boss_kill * Monster.__GOLD_INCREASE_PER_BOSS_KILL)
            self.attacked_monster = self.boss_health
        if self.current_level < 10 or self.current_level % 10 != 0:
            self.attacked_monster = self.monster_hp

    def check_for_boss(self):
        return self.current_level % 10 == 0

    def __repr__(self):
        return f"Monster HP: {self.monster_hp}\n" \
               f"Attacked monster HP: {self.attacked_monster}\n" \
               f"BOSS HP: {self.boss_health}\n" \
               f"Gold drop per normal monster: {self.gold_drop_normal_monster}\n" \
               f"Gold drop per BOSS: {self.gold_per_boss_kill}\n" \
               f"Current level of monster: {self.current_level}"


# default = Monster(12, 1, 20)
"""
no need to type parameters, default ones are included
"""

# higher_values = Monster(50, 50, 50)
"""
if you wish to start with higher values, just put values that are higher than the default ones
"""


# check_monster_health = Monster()
# for _ in range(11):
#     check_monster_health.prepare_next_level()
#     print(check_monster_health)
#     print()


# click_power_test = ClickBuff()
# monster = Monster()
# for _ in range(12):  # test for level 1
#     monster.attack_monster(click_power_test)
#     print(monster)
#     print()
