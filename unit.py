#!/usr/bin/env python3

class Unit:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def is_alive(self):
        return 0 != self.health

