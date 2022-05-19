import os
class Tile(): 
    def __init__(self, parent, Type, x, y, varient=0, varient2=0):
        # Tile object exists to occupy a place in the map 
        # There are multiple variants that are indicated from the text file
        # Tiles are initialised with 2 variants, a parent game, a type, 
        # as well as x and y coords

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
        
        # Different tupes of solid tile permutations 
        # Solid tiles may have padded or wrap walls
        if self.type == "Solid":
            self.wrap_plate = varient
            self.pad_clone = varient2

        # Different type of empty tile permutations
        # Empty tiles may have plates or clones
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

    #copy the contents of a tile by making another tile object and puts it in a clipboard
    def copy(self, x, y):
        temp = Tile(self.parent, self.type, x, y, 0, 0)
        temp.true_empty = self.true_empty
        temp.wrap_plate = self.wrap_plate
        temp.pad_clone = self.pad_clone
        return temp

    #given a tile object copied by the clipboard, paste its properties to another tile
    def paste(self, dest_x, dest_y):
        target = self.parent.tiles[dest_y][dest_x]

        #remove all of the old listings in the target 
        if target.type == "Empty":
            if target.wrap_plate == 1:
                del self.parent.goals[self.parent.goals.index([target.x, target.y])]
            elif target.wrap_plate == 2:
                del self.parent.alt_goals[self.parent.alt_goals.index([target.x, target.y])]
            elif target.pad_clone == 1:
                del self.parent.clones[self.parent.clones.index([target.x, target.y])]

        #transfer new listings to new tile
        target.type = self.type
        target.true_empty = self.true_empty
        target.wrap_plate = self.wrap_plate
        target.pad_clone = self.pad_clone
        if target.type == "Empty":
            if target.wrap_plate == 1:
                self.parent.goals.append([target.x, target.y])
            elif target.wrap_plate == 2:
                self.parent.alt_goals.append([target.x, target.y])
            elif target.pad_clone == 1:
                self.parent.clones.append([target.x, target.y])
        
    #  returns a string representation of the tile's coords
    def __repr__(self):
        return("{}, {}".format(self.x, self.y))

            
class Map():
    def __init__(self, parent=None, mapdir=None):
        self.parent = parent

        # This ls is used to store all tiles 
        self.tiles = []

        # Map also stores information about pressure plate goals
        self.goals = []
        self.goalsMet = False
        self.alt_goals = []
        self.alt_goalsMet = False

        #  Map also stores information about locations of clone plates
        self.clones = []

        # Each map has an objective
        self.mainGoal = ''

        # Map also stores info about valid strawberry spawn locations
        self.strawberry_valid = []

        #can create an empty instance to write to!
        if mapdir is not None:
            self.loadMap(mapdir)

    def loadMap(self, mapdir):
        #  Loads the map from the directory and the two text files 

        if self.parent.custom:
            path = self.parent.srcreal + '/snakeData'
        else:
            path = self.parent.src

        # Parses through the file line by line to read in map info 
        with open(path + "/levels/" + mapdir + "/map1.txt", "r") as f, open(path + "/levels/" + mapdir + "/map2.txt", "r") as g:
            # Reads each line first  
            for i in range(0, int(self.parent.config.settings["mapY"])): 
                line = f.readline()
                line2 = g.readline()
                tileLine = []

                # Read each character in the line 
                # creates a tile type depending on the rules defined in writing_maps.txt
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

                # Adds to tiles list
                self.tiles.append(tileLine)

    #only used in game, not level maker!
    def generate_spaces(self):
        for line in self.tiles:
            for tile in line:
                if tile.true_empty:
                    self.strawberry_valid.append([tile.x, tile.y])


    # Reads the map based on tiles - only used during debugging stages of development 
    def readMap(self):
        for i in range(len(self.tiles)): 
            tiles = "Line " + str(i) + ":"
            for k in range(len(self.tiles[0])): 
                tiles = tiles + self.tiles[i][k].type + " "
            print(tiles)

    
    def writeMap(self, dest):
        #  Used by the levelmaker 

        #destination directory:
        if not os.path.exists(dest):
            os.makedirs(dest)

        #write config file first :
        with open(dest + "/config.txt", "w") as f:
            for key in self.parent.config.settings:
                f.write("{}:={}\n".format(key, self.parent.config.settings[key]))

        #write the snake information:
        with open(dest + "/snake.txt", "w") as f:
            snake = self.parent.snake
            for i in range(len(snake.segments)):
                f.write("{},{},{},{}\n".format(snake.segments[i][0], snake.segments[i][1],\
                                            snake.segmentd[i][0], snake.segmentd[i][1]))


        #  Create the two necessary textfiles for map-reading 
        with open(dest + "/map1.txt", "w") as f, open(dest + "/map2.txt", "w") as g:
            for index, line in enumerate(self.tiles):
                for tile in line:

                    #  Write a character to the textfile corresponding to the tile tyep
                    # based on the rules + info defined in writing_maps.txt
                    if tile.type == "Other":
                        f.write(' ')
                        g.write(' ')
                    elif tile.type == "Empty":
                        g.write('R')
                        if tile.true_empty == True:
                            f.write('Q')
                        else:
                            f.write(chr(ord('R') + tile.wrap_plate + 3*tile.pad_clone))
                    elif tile.type == "Solid":
                        f.write(chr(ord('A') + tile.wrap_plate))
                        g.write(chr(ord('A') + tile.pad_clone))

                # Ensures that new line characters are inserted 
                if index < len(self.tiles) - 1:
                    f.write("\n")
                    g.write("\n")












