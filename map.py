class Tile(): 
    def __init__(self, parent, Type, x, y, varient=0, varient2=0):

        # Tile initialised with a type, a 'parent' game that it exists in, x coordinates, y coordinates, and different variants 
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

        #pressure plates and clone blocks on this end
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

        # Map is initialised with a parent game 
        self.parent = parent
        print(self.parent.config.settings)

        # This will store all of the tiles in the map
        self.tiles = []

        #pressure plate goals
        self.goals = []
        self.alt_goals = []
        self.clones = []
        
        if mapdir is not None:
            self.loadMap(mapdir, custom)

    def loadMap(self, mapdir, custom):
        # loading in the map from a text-file 
        #  Generates a multi-dimensional list where each element is a tile object
        with open(self.parent.src + "/levels/" + mapdir + "/map1.txt", "r") as f, open(self.parent.src + "/levels/" + mapdir + "/map2.txt", "r") as g:
            for i in range(0, int(self.parent.config.settings["mapY"])): 
                line = f.readline()
                line2 = g.readline()

                # Creates a list for each row 
                tileLine = []
                for k in range(0, int(self.parent.config.settings["mapX"])): 
                    letter = line[k]
                    letter2 = line2[k]

                    #  If the letter represents a solid tile, this is put in the map (with its respective variants)
                    #  Translates the letter to a unicode code and then checks it against our criteria 
                    if (ord(letter) >= 65 and ord(letter) <= 80):
                        tile = Tile(self, "Solid", k, i, varient=ord(letter)-65, varient2=ord(letter2)-65)
                    
                    # If the letter represents an empty tile, this is put in the map with its respective variations
                    elif (ord(letter) >= 81 and ord(letter) <= 85):
                        tile = Tile(self, "Empty", k, i, varient=ord(letter)-65)

                    # If the letter is blank, this is an 'other' space
                    elif (letter == ' '): 
                        tile = Tile(self, "Other", k, i)
                    tileLine.append(tile)
                # Added to the big list of tiles stored in the map object 
                self.tiles.append(tileLine)
        print(self.goals, self.alt_goals, self.clones)

    def readMap(self):
        #  This is just a helper function to ensure that the map loads in from the file correctly, it is not used in the game

        #  The function goes through the multi-dimensional map list and prints all the types. This was then cross-checked with the file
        for i in range(0, 28): 
            tiles = "Tiles on line " + str(i) + " "
            for k in range(0, 28): 
                tiles = tiles + self.tiles[i][k].type + " "
            print(tiles)

    def writeMap(self, dest):
        pass
