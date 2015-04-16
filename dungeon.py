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
        directions = {'up': (0, -1), 'down': (0, 1),
                      'left': (-1, 0), 'rigth': (1, 0)}
        new_possition = list(map(sum, zip(*[self.hero_possition, directions[direction]])))
        if new_possition[0] >= 0 and new_possition[1] >= 0:
            self.hero_possition = tuple(new_possition)
            return True
        return False


if __name__ == '__main__':
    dungeon = Dungeon('level1.txt')
    print(dungeon.print_map())
