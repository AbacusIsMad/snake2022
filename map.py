class Tile(): 
    def __init__(self, parent, Type, x, y, varient=0, varient2=0):
        self.type = Type
        self.true_empty = False
        self.wrap_plate = 0
        self.pad_clone = 0
        self.movable = False
        self.parent = parent
        self.x = x
        self.y = y
        #A completely empty tile
        if varient == 16: #Q
            self.true_empty = True
        
        #solid tile permutations:
        if self.type == "Solid":
            self.wrap_plate = varient
            self.pad_clone = varient2

        #pressure plates and clone blocks on this end. 17, 18, 19, 20
        if self.type == "Empty":
            if varient == 18:
                self.wrap_plate = 1
                self.parent.goals.append([self.x, self.y])
            elif varient == 19:
                self.wrap_plate = 2
                self.parent.alt_goals.append([self.x, self.y])
            elif varient == 20:
                self.pad_clone = 1
                self.parent.clones.append([self.x, self.y])

    def __repr__(self):
        return("{}, {}".format(self.x, self.y))

            
class Map():
    def __init__(self, parent=None, mapdir=None, custom=False):
        self.parent = parent
        print(self.parent.config.settings)
        self.tiles = []
        #pressure plate goals
        self.goals = []
        self.alt_goals = []
        self.clones = []
        #can create an empty instance to write to!
        if mapdir is not None:
            self.loadMap(mapdir, custom)

    def loadMap(self, mapdir, custom):
        with open("./levels/" + mapdir + "/map1.txt", "r") as f, open("./levels/" + mapdir + "/map2.txt", "r") as g:
            for i in range(0, int(self.parent.config.settings["mapY"])): 
                line = f.readline()
                line2 = g.readline()
                tileLine = []
                for k in range(0, int(self.parent.config.settings["mapX"])): 
                    letter = line[k]
                    letter2 = line2[k]
                    if (ord(letter) >= 65 and ord(letter) <= 80):
                        tile = Tile(self, "Solid", k, i, varient=ord(letter)-65, varient2=ord(letter2)-65)
                    elif (ord(letter) >= 81 and ord(letter) <= 85):
                        tile = Tile(self, "Empty", k, i, varient=ord(letter)-65)
                    elif (letter == ' '): 
                        tile = Tile(self, "Other", k, i)
                    tileLine.append(tile)
                self.tiles.append(tileLine)
        print(self.goals, self.alt_goals, self.clones)

    def readMap(self):
        for i in range(0, 28): 
            tiles = "Tiles on line " + str(i) + " "
            for k in range(0, 28): 
                tiles = tiles + self.tiles[i][k].type + " "
            print(tiles)

    def writeMap(self, dest):
        pass
