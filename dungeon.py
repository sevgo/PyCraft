from weapon import Weapon
from spell import Spell
from enemy import Enemy
from fight import Fight
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
                return (i, self.dungeon_map[i].index(item))

    def print_map(self):
        return '\n'.join([''.join(x) for x in self.dungeon_map])

    def spawn(self, hero):
        self.hero = hero
        spawn_location = self._find_item_coordinates('S')
        self.dungeon_map[spawn_location[0]][spawn_location[1]] = 'H'
        self.hero_possition = spawn_location

    def _new_possition(self, coordinates, direction):
        directions = {'up': (-1, 0), 'down': (1, 0),
                      'left': (0, -1), 'rigth': (0, 1)}
        new_possition = list(map(sum, zip(*[coordinates, directions[direction]])))
        return new_possition

    def _can_move(self, coordinates):
        return (coordinates[0] < len(self.dungeon_map)
                and coordinates[1] < len(self.dungeon_map[0])
                and coordinates[0] >= 0
                and coordinates[1] >= 0
                and self.dungeon_map[coordinates[0]][coordinates[1]] != '#')

    def move_hero(self, direction):
        new_possition = self._new_possition(self.hero_possition, direction)
        if self._can_move(new_possition):
            if self.dungeon_map[new_possition[0]][new_possition[1]] == 'T':
                treasure = random.choice(self.treasures)
                self._found_treasure(treasure)
            self.dungeon_map[self.hero_possition[0]][self.hero_possition[1]] = '.'
            self.dungeon_map[new_possition[0]][new_possition[1]] = 'H'
            self.hero_possition = tuple(new_possition)
            if self.dungeon_map[new_possition[0]][new_possition[1]] == 'E':
                self._start_fight(self.hero_possition)
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

    def _create_enemy(self, health=None, mana=None, damage=None):
        if health is None:
            health = random.randint(10, 50)
        if mana is None:
            mana = random.randint(10, 40)
        if damage is None:
            damage = random.randint(5, 15)
        return Enemy(health, mana, damage)

    def _start_fight(self, enemy_possition):
        return Fight(self.hero, self._create_enemy(), self.hero_possition, enemy_possition)

    def _find_enemy(self, cast_range):
        for d in ['up', 'down', 'left', 'rigth']:
            pos = self.hero_possition
            for i in range(cast_range):
                pos = self._new_possition(pos, d)
                if self._can_move(pos):
                    if self.dungeon_map[pos[0]][pos[1]] == 'E':
                        return pos
                else:
                    break
        return False

    def hero_attack(self, by):
        if self.hero.spell and self._find_enemy(self.hero.spell.cast_range):
            return self._start_fight()
        else:
            return 'Nothing in casting range ' + str(self.hero.spell.cast_range)
