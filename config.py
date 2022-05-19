class Config():
    def __init__(self, parent=None, mapdir=None):

        # Config object is initialised with a parent game
        self.parent = parent

        # can create an 'empty' instance 
        if mapdir is not None:
            self.loadConfig(mapdir)


    def loadConfig(self, mapdir):
        # Config data is read in from a directory 
        if self.parent.custom:
            path = self.parent.srcreal + '/snakeData'
        else:
            path = self.parent.src

        #  Reads the config info for the specific level
        #  Reads info pertaining to level size from this, appends it to a lsit
        with open(path + "/levels/" + mapdir + "/config.txt", "r") as c:
            l = c.readlines()
            new = []
        for line in l:
            if line != '\n':
                new.append(line[:-1].split(":="))

        # creates a dictionary of this previously defined list 
        self.settings = dict(new)
