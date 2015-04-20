#!/usr/bin/env python3
from spell import Spell
from weapon import Weapon


class Unit:
    """ Basic class that is common for Hero and Enemy """

    def __init__(self, health, mana, mana_regeneration_rate=0, damage=0):
        self.health = health
        self._max_health = health
        self.mana = mana
        self._max_mana = mana
        self.mana_regeneration = mana_regeneration_rate
        self.damage = 0
        self.weapon = Weapon('none', 0)
        self.spell = Spell('none', 0, 0, 0)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return 0 != self.health

    def take_healing(self, health_points):
        """
            If our hero is dead, the method should return False. It's too late
            to heal our hero. We cannot heal our hero above the maximum health,
            which is given by health If healing is successful (Our hero is not
            dead), the method should return True
        """
        if not self.is_alive():
            return False

        self.health += abs(health_points)
        if self.health > self._max_health:
            self.health = self._max_health

        return True

    def take_mana(self, mana_points=0, moved=False):
        """
        Each time he makes a move, his mana is increased by
            mana_regeneration_rate amount which is 0 for Enemy Unit.
        He can drink a mana potion, which will increse his mana by the amount
            of mana points the potion have.
        It's mana cannot go above the start mana given to him, neither he can
        go down below 0 mana. """
        if moved:
            mana_points += self.mana_regeneration

        self.mana += abs(mana_points)
        if self.mana > self._max_mana:
            self.mana = self._max_mana

        return True

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def __reduce_mana(self, reduce_mana_by):
        self.mana -= reduce_mana_by

    # def attack(self, by=None, distance=0):
    def attack(self, by=None):
        spell = self.spell
        weapon = self.weapon

        if by is None:
            # if self.can_cast(distance):
            if self.can_cast():
                attack = spell if spell.damage >= weapon.damage else weapon
                if attack == spell:
                    by = 'spell'
                    self.__reduce_mana(attack.mana_cost)
                else:
                    by = 'weapon'

                return (by, attack.damage)
        elif by.lower() == "weapon" and self.weapon:
            return (by, weapon.damage)
        # elif by.lower() == "spell" and self.spell and self.can_cast(distance):
        elif by.lower() == "spell" and self.spell and self.can_cast():
            attack = spell
            self.__reduce_mana(attack.mana_cost)
            return (by, attack.damage)

        return ('Hands', self.damage)

    def take_damage(self, damage_points):
        self.health -= abs(damage_points)
        if self.health < 0:
            self.health = 0

    def can_cast(self):
        # if (self.spell and self.spell.cast_range >= distance
        #         and self.mana >= self.spell.mana_cost):
        if (self.spell and self.mana >= self.spell.mana_cost):
            return True
        return False
