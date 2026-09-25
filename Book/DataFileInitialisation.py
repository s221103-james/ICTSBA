class BookDataHashmapinitialise:
    def __init__(self, data):
        self.range = 30000
        self.hashmap = data

    def GetHashIndex(self, key):
        Index = 0
        for i in str(key):
            Index += ord(i)
            Index = Index % self.range
        return Index
    
    def __setitem__(self, key, data):
        index = self.GetHashIndex(key)
        exist = False
        if len(self.hashmap[index]) >= 1:
            if self.hashmap[index][-1] == None:
                self.hashmap[index][-1] = [key, data]
            else:
                self.hashmap[index].append([key, data])
        else:
            self.hashmap[index].append([key, data])

    def __getitem__(self, key):
        index = self.GetHashIndex(key)
        return self.hashmap[index]
    