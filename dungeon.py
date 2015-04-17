from weapon import Weapon
from spell import Spell
import random


class Dungeon:
    def __init__(self, level_file):
        f = open(level_file, "r")
        dungeon_list = f.readlines()
        f.close()
        self.dungeon_map = [list(x.rstrip('\n')) for x in dungeon_list]
        self.hero_possition = None
        self.treasures = ['mana', 'health', 'weapon', 'spell']
        self.weapon_names = ['weapon name']
        self.spell_names = ['spell name']

    def _find_item_coordinates(self, item):
        for i in range(len(self.dungeon_map)):
            if item in self.dungeon_map[i]:
                return (self.dungeon_map[i].index(item), i)

    def print_map(self):
        return '\n'.join([''.join(x) for x in self.dungeon_map])

    def spawn(self, hero):
        self.hero = hero
        spawn_location = self._find_item_coordinates('S')
        self.dungeon_map[spawn_location[0]][spawn_location[1]] = 'H'
        self.hero_possition = spawn_location

    def move_hero(self, direction):
        directions = {'up': (-1, 0), 'down': (1, 0),
                      'left': (0, -1), 'rigth': (0, 1)}
        new_possition = list(map( sum, zip(*[self.hero_possition, directions[direction]])))

        if (new_possition[0] >= 0 and new_possition[1] >= 0
            and self.dungeon_map[new_possition[0]][new_possition[1]] not in ['#', 'E']):
            if self.dungeon_map[new_possition[0]][new_possition[1]] == 'T':
                treasure = random.choice(self.treasures)
                self._found_treasure(treasure)
            self.dungeon_map[self.hero_possition[0]][self.hero_possition[1]] = '.'
            self.dungeon_map[new_possition[0]][new_possition[1]] = 'H'
            self.hero_possition = tuple(new_possition)
            return True
        return False

    def _found_treasure(self, treasure):
        if treasure == 'mana':
            self.hero.take_mana(random.randint(10, 50))
        if treasure == 'health':
            self.hero.take_healing(random.randint(10, 50))
        if treasure == 'weapon':
            name = random.choice(self.weapon_names)
            damage = random.randint(10, 50)
            self.hero.equip(Weapon(name, damage))
        if treasure == 'spell':
            name = random.choice(self.spell_names)
            damage = random.randint(10, 50)
            cost = random.randint(int(0.5 * damage), int(0.7 * damage))
            cast_range = random.randint(2, 4)
            self.hero.learn(Spell(name, damage, cost, cast_range))


if __name__ == '__main__':
    dungeon = Dungeon('level1.txt')
    dungeon.spawn('1')
    print(dungeon.move_hero('rigth'))
    print(dungeon.move_hero('down'))
    print(dungeon.move_hero('down'))
    print(dungeon.print_map())
