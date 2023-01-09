class Statistics:
    # statistic = {
    #     'Current Gold': 0,
    #     'Total gold earned': 0,
    #     'Total monsters kills': 0,
    #     'Total boss kills': 0
    # }
    def __init__(self, current_gold=0, total_gold=0, total_monster_kills=0, total_boss_kills=0, current_level_upgrade=0,
                 current_level_worker=0):
        self.current_gold = current_gold
        self.total_gold = total_gold
        self.total_monsters_kills = total_monster_kills
        self.total_boss_kills = total_boss_kills
        self.current_level_upgrade = current_level_upgrade
        self.current_level_worker = current_level_worker

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


