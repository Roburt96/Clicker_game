from click_buff import *


class Statistics:

    def __init__(self, current_gold=0, total_gold=0, total_monster_kills=0, total_boss_kills=0, current_level_upgrade=0,
                 current_level_worker=0, start_dmg=1):
        self.current_gold = current_gold
        self.total_gold = total_gold
        self.total_monsters_kills = total_monster_kills
        self.total_boss_kills = total_boss_kills
        self.current_level_upgrade = current_level_upgrade
        self.current_level_worker = current_level_worker
        self.start_dmg = start_dmg

    def add_gold_for_kill(self, gold):
        self.current_gold += gold
        self.total_gold += gold

    def total_monsters_kill(self, monster_kill):
        self.total_boss_kills += monster_kill

    def total_boss_kill(self, boss_kill):
        self.total_boss_kills += boss_kill

    def add_level_to_upgrade(self, lvl_upgrade):
        self.current_level_upgrade += lvl_upgrade

    def add_level_to_worker(self, lvl_worker):
        self.current_level_worker += lvl_worker

    def add_dpc(self, add_dpc):
        self.start_dmg += add_dpc



