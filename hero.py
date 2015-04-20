#!/usr/bin/env python3

from unit import Unit


class Hero(Unit):
    def __init__(self, name="Name", title="title", health=100, mana=100,
                 mana_regeneration_rate=2):

        super().__init__(health, mana, mana_regeneration_rate)
        self.name = name
        self.title = title

    def known_as(self):
        return "{} the {}".format(self.name, self.title)
