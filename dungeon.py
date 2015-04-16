class Dungeon:
    def __init__(self, level_file):
        f = open(level_file, "r")
        dungeon_list = f.readlines()
        f.close()
        self.dungeon_map = [list(x.rstrip('\n')) for x in dungeon_list]
