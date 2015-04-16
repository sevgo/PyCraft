class Dungeon:
    def __init__(self, level_file):
        f = open(level_file, "r")
        dungeon_list = f.readlines()
        f.close()
        self.dungeon_map = [list(x.rstrip('\n')) for x in dungeon_list]

    def _find_item_coordinates(self, item):
        for i in range(len(self.dungeon_map)):
            if item in self.dungeon_map[i]:
                return (i, self.dungeon_map[i].index(item))

    def print_map(self):
        for row in self.dungeon_map:
            print(''.join(row))

    def spawn(self, hero):
        spawn_location = self._find_item_coordinates('S')
        self.dungeon_map[spawn_location[0]][spawn_location[1]] = 'H'

if __name__ == '__main__':
    dungeon = Dungeon('level1.txt')
    dungeon.print_map()
