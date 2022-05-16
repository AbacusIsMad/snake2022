class Config():
    def __init__(self, parent=None, mapdir=None):
        self.parent = parent
        if mapdir is not None:
            self.loadConfig(mapdir)

    def loadConfig(self, mapdir):
        if self.parent.custom:
            path = self.parent.srcreal + '/snakeData'
        else:
            path = self.parent.src

        with open(path + "/levels/" + mapdir + "/config.txt", "r") as c:
            l = c.readlines()
            new = []
        for line in l:
            if line != '\n':
                new.append(line[:-1].split(":="))
        self.settings = dict(new)
