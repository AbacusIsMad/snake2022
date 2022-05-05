class Tile(): 
    def __init__(self, Type, x, y):
        self.type = Type
        self.x = x
        self.y = y


class Map():
    def __init__(self, mapdir=None, custom=False):
        self.tiles = []
        if mapdir is not None:
            self.loadMap(mapdir, custom)

    def loadMap(self, mapdir, custom):
        with open("levels/" + mapdir + "/map.txt", "r") as f:
            for i in range(0, 28): 
                line = f.readline()
                tileLine = []
                for k in range(0, 28): 
                    letter = line[k]
                    if (letter == "W"):
                        tile = Tile("Solid", k, i)
                    elif (letter == " "):
                        tile = Tile("Empty", k, i)
                    elif (letter == "B" or letter == "G" or letter == "Y" or letter == "R" or letter == "P"): 
                        tile = Tile("Other", k, i)
                    tileLine.append(tile)
                self.tiles.append(tileLine)

    def readMap(self):
        for i in range(0, 28): 
            tiles = "Tiles on line " + str(i) + " "
            for k in range(0, 28): 
                tiles = tiles + self.tiles[i][k].type + " "
            print(tiles)

    def writeMap(self, dest):
        pass
