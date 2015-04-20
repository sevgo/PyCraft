#!/usr/bin/env python3
from weapon import Weapon
from spell import Spell
from random import choice, randint


class Treasure:

    WEAPON_NAMES = ['axe', 'sword', 'pike', 'bow']
    SPELLS = ['fireball', 'meteor_shower', 'lightning', 'emp']
    POINTS = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    HOW_MUCH_POTIONS = 5
    def __init__(self):
        self.weapons = self.load_weapons()
        self.spells = self.load_spells()
        self.health_potions = self.load_potions(Treasure.HOW_MUCH_POTIONS)
        self.mana_potions =self.load_potions(5)

    def load_weapons(self):
        weapons_list = []
        for element in Treasure.WEAPON_NAMES:
            weapons_list.append(Weapon(element, choice(Treasure.POINTS)))

        return weapons_list

    def load_spells(self):
        spells_list = []
        for element in Treasure.SPELLS:
            spells_list.append(Spell(element,choice(Treasure.POINTS),
                                     choice(Treasure.POINTS), randint(1, 5)))

        return spells_list

    def load_potions(self, potion_counts):
        potions_list = []
        for i in range(0, potion_counts):
            potions_list.append(choice(Treasure.POINTS))
        return potions_list

    def get_weapon(self):
        return choice(self.weapons)

    def get_spell(self):
        return choice(self.spells)



if __name__ == "__main__":
    t = Treasure()
    w = t.get_spell()
    for element in t.spells:
        print(element.name)
        print(element.damage)
        print(element.mana_cost)
