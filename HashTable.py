class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash_value(self, key):
        asc = 0
        for w in key:
            asc+=ord(w)
        return asc % self.max

    def __setitem__(self, key, value):
        s = self.get_hash_value(key)
        if self.arr[s] == []:
            self.arr[s] = [[key,value]]
        else:
            self.arr[s].append([key, value])

    def __getitem__(self, key):
        s = self.get_hash_value(key)
        for i in self.arr[s]:
            if i[0] == key:
                return i[1]

    def __delitem__(self, key):
        s = self.get_hash_value(key)
        for idx, ele in enumerate(self.arr[s]):
            if ele[0] == key:
                del self.arr[s][idx]

h = HashTable()

h['march 6'] = 22
h['july 22'] = 275
h['march 18'] = 21
h['may 2'] = 24
del h['july 22']
print(h.arr)