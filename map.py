
class Tile(): 
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

class Map():
    # separate file for time being 
    def __init__(self, mapfile):
        self.tiles = []
        self.mapfile = mapfile
    
    def loadMap(self): 
        f = open(self.mapfile, "r")
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
                
map = Map("map.txt")
map.loadMap()
map.readMap()
        
# ideally, this map oculd be loaded in from like a text file or something...., so that players could make their own levels? 

