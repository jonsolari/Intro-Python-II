class Item:
    def __init__(self, name, desc, noise):
        self.name = name
        self.desc = desc
        self.noise = noise

    def __str__(self):
        return "{}".format(self.name)
    
    def shake():
        print(self.noise)