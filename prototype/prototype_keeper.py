class PrototypeKeeper:
    def __init__(self):
        self.map_ = dict()
    def addCloneable(self, key, prototype):
        self.map_[key] = prototype
    def getClone(self, key):
        prototype = self.map_[key]
        return prototype.createClone();
