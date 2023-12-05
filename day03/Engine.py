class Engine():
    def __init__(self, schematic:str):
        self.schematic = schematic
        self.size = len(schematic), len(schematic[0])

    def find_adjacent(self, x:int, y:int):
        adjacent = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                # If we're looking at the current spot, skip it
                if i == x and j == y:
                    continue
                # If either index is negative, skip it
                if i < 0 or j < 0:
                    continue
                try:
                    # adjacent.append(self.schematic[j][i])
                    target = self.schematic[j][i]
                    if target != '.' and target is not None:
                        adjacent.append(target)
                except IndexError:
                    pass
        return adjacent

    def find_part(self, x:int, y:int):
        try:
            target = self.schematic[y+dy][x+dx]
            if target != '.' and target is not None:
                return target
        except IndexError:
            pass
        return None