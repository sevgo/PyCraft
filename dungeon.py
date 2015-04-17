class Dungeon:
    def __init__(self, level_file):
        f = open(level_file, "r")
        dungeon_list = f.readlines()
        f.close()
        self.dungeon_map = [list(x.rstrip('\n')) for x in dungeon_list]
        self.hero_possition = None

    def _find_item_coordinates(self, item):
        for i in range(len(self.dungeon_map)):
            if item in self.dungeon_map[i]:
                return (self.dungeon_map[i].index(item), i)

    def print_map(self):
        return '\n'.join([''.join(x) for x in self.dungeon_map])

    def spawn(self, hero):
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
                self._found_treasure()
            self.dungeon_map[self.hero_possition[0]][self.hero_possition[1]] = '.'
            self.dungeon_map[new_possition[0]][new_possition[1]] = 'H'
            self.hero_possition = tuple(new_possition)
            return True
        return False

    def _found_treasure(self):
        pass


if __name__ == '__main__':
    dungeon = Dungeon('level1.txt')
    dungeon.spawn('1')
    print(dungeon.move_hero('rigth'))
    print(dungeon.move_hero('down'))
    print(dungeon.move_hero('down'))
    print(dungeon.print_map())
