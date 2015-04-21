#!/usr/bin/env python3
import json
from weapon import Weapon
from spell import Spell
from random import choice, randint


class Treasure:

    @staticmethod
    def load_treasures(fpath):
        with open(fpath, 'r') as fd:
            treasures_dict = json.load(fd)

        return treasures_dict

    def __init__(self, fpath="treasures.json"):
        self.treasures = Treasure.load_treasures(fpath)
        self.weapons = self.treasures['weapons']
        self.spells = self.treasures['spells']
        self.health_potions = self.treasures['health']
        self.mana_potions = self.treasures['mana']

    def __random_key(self, dict_obj):
        return choice(list(dict_obj.keys()))

    def _get_random_weapon(self):
        name = self.__random_key(self.weapons)

        return Weapon(name, self.weapons[name])

    def _get_random_spell(self):
        name = self.__random_key(self.spells)
        damage, mana_cost, cost_range = self.spells[name]

        return Spell(name, damage, mana_cost, cost_range)

    def _get_random_health(self):
        return choice(self.health_potions)

    def _get_random_mana(self):
        return choice(self.mana_potions)

    def get_treasure(self):
        return choice([self._get_random_weapon(), self._get_random_mana(),
                       self._get_random_spell(), self._get_random_health()])

if __name__ == "__main__":
    t = Treasure()
    pick_up = t.get_treasure()
    print(type(pick_up))
