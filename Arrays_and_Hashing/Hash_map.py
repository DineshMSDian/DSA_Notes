# HashMap - python DICT

class HashMap:
    def __init__(self, size = 10):
        self.size = size
        self.HashTable = [[] for _ in range(size)]
        """
        -> index    [0][1][2][3][4][5]
        -> bucket   [ ][ ][ ][ ][ ][ ]
        -> bucket   [ ][ ][ ][ ][ ][ ]

        Index | Bucket
        ----------------
        0     | []
        1     | []
        2     | []
        3     | []
        4     | []
        """
        """ s = "anagram"
            t = "nagaram"
        """ 
    def SetVal(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.HashTable[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return
        bucket.append((key, val))

    def GetVal(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.HashTable[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        return "Value not found"
    
    def DeleteVal(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.HashTable[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return
    
    def __str__(self):
        return "".join(str(bucket) for bucket in self.HashTable)

# dictionary = HashMap()
if __name__ == '__main__':
    dictionary = HashMap()
    dictionary = HashMap(5)
    print(dictionary.HashTable)
    dictionary.SetVal("Apple", 20)
    print(dictionary.HashTable)
    dictionary.SetVal("Banana", 10)
    print(dictionary.HashTable)
    print(dictionary.GetVal("Apple"))
    dictionary.DeleteVal("Banana")
    print(dictionary.HashTable)