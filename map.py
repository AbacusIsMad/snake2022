class Tile(): 
    def __init__(self, parent, Type, x, y, varient=0, varient2=0):
        self.type = Type
        self.true_empty = False
        self.wrap_plate = None
        self.pad_clone = None
        self.movable = False
        self.x = x
        self.y = y
        #A completely empty tile
        if varient == 16: #Q
            self.true_empty = True
        
        #solid tile permutations:
        if self.type == "Solid":
            self.wrap_plate = varient
            self.pad_clone = varient2

class Map():
    def __init__(self, mapdir=None, custom=False, config=None):
        self.tiles = []
        #pressure plate goals
        self.goals = []
        self.alt_goals = []
        #can create an empty instance to write to!
        if mapdir is not None:
            self.loadMap(mapdir, custom)

    def loadMap(self, mapdir, custom):
        with open("levels/" + mapdir + "/map1.txt", "r") as f, open("levels/" + mapdir + "/map2.txt", "r") as g:
            for i in range(0, 28): 
                line = f.readline()
                line2 = g.readline()
                tileLine = []
                for k in range(0, 28): 
                    letter = line[k]
                    letter2 = line2[k]
                    if (ord(letter) >= 65 and ord(letter) <= 80):
                        tile = Tile(self, "Solid", k, i, varient=ord(letter)-65, varient2=ord(letter2)-65)
                    elif (ord(letter) >= 81 and ord(letter) <= 85):
                        tile = Tile(self, "Empty", k, i, varient=ord(letter)-65)
                    elif (letter == ' '): 
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
