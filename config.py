class Config():
    def __init__(self, mapdir=None, custom=False):
        if mapdir is not None:
            self.loadConfig(mapdir, custom)

    def loadConfig(self, mapdir, custom):
        with open("./levels/" + mapdir + "/config.txt", "r") as c:
            l = c.readlines()
            new = []
        for line in l:
            if line != '\n':
                new.append(line[:-1].split(":="))
        self.settings = dict(new)
