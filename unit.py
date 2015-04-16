#!/usr/bin/env python3


class Unit:
    """ Basic class that is common for Hero and Enemy """

    def __init__(self, health, mana, mana_regeneration_rate=0):
        self.health = health
        self._max_health = health
        self.mana = mana
        self._max_mana = mana
        self.mana_regeneration = mana_regeneration_rate
        self.weapon = None
        self.spell = None

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
        if 0 == self.health:
            return False

        self.health += health_points
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

        self.mana += mana_points
        if self.mana > self._max_mana:
            self.mana = self._max_mana

        return True

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        spell = self.spell.damage
        weapon = self.weapon.damage

        if by is None and self.can_cast():
            attack = spell if spell > weapon else weapon
        elif by.lower() == "weapon" and self.weapon:
            attack = weapon
        elif by.lower() == "spell" and self.spell and self.can_cast():
            attack = spell
            self.mana -= spell
        else:
            attack = self.damage

        return attack

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0
