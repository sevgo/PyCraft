#!/usr/bin/env python3
from unit import Unit


class Enemy(Unit):

    def __init__(self, health=50, mana=45, damage=10):
        super(Enemy, self).__init__()
        self.damage = damage
