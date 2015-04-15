#!/usr/bin/env python3
class Unit:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana
