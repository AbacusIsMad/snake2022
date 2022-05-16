import os


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
    def __init__(self, parent=None, mapdir=None):
        self.parent = parent
        self.tiles = []
        #pressure plate goals
        self.goals = []
        self.goalsMet = False
        self.alt_goals = []
        self.alt_goalsMet = False
        self.clones = []
        self.mainGoal = ''
        self.strawberry_valid = []
        #can create an empty instance to write to!
        if mapdir is not None:
            self.loadMap(mapdir)

    def loadMap(self, mapdir):
        if self.parent.custom:
            path = self.parent.srcreal + '/snakeData'
        else:
            path = self.parent.src

        with open(path + "/levels/" + mapdir + "/map1.txt", "r") as f, open(path + "/levels/" + mapdir + "/map2.txt", "r") as g:
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

    #only used in game, not level maker!
    def generate_spaces(self):
        for line in self.tiles:
            for tile in line:
                if tile.true_empty:
                    self.strawberry_valid.append([tile.x, tile.y])



    def readMap(self):
        for i in range(len(self.tiles)): 
            tiles = "Line " + str(i) + ":"
            for k in range(len(self.tiles[0])): 
                tiles = tiles + self.tiles[i][k].type + " "
            print(tiles)

    #destination directory:
    def writeMap(self, dest):
        if not os.path.exists(dest):
            os.makedirs(dest)

        #write config:
        with open(dest + "/config.txt", "w") as f:
            for key in self.parent.config.settings:
                f.write("{}:={}\n".format(key, self.parent.config.settings[key]))

        #write snake:
        with open(dest + "/snake.txt", "w") as f:
            snake = self.parent.snake
            for i in range(len(snake.segments)):
                f.write("{},{},{},{}\n".format(snake.segments[i][0], snake.segments[i][1],\
                                            snake.segmentd[i][0], snake.segmentd[i][1]))

        with open(dest + "/map1.txt", "w") as f, open(dest + "/map2.txt", "w") as g:
            for index, line in enumerate(self.tiles):
                for tile in line:
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

                if index < len(self.tiles) - 1:
                    f.write("\n")
                    g.write("\n")












