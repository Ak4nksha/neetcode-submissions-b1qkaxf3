class MyHashMap:

    def __init__(self):
        
        self.hhash = [None] * ((10 ** 6) + 1)
        self.size = 0


    def put(self, key: int, value: int) -> None:

        #print(len(self.hhash))
        if self.hhash[key] is None:
            self.size += 1  
        self.hhash[key] = value

    def get(self, key: int) -> int:

        if self.hhash[key] is None:
            return -1  
        else:
            return self.hhash[key]

    def remove(self, key: int) -> None:

        if self.hhash[key] is None:
            return
        else:
            self.hhash[key] = None
            self.size -= 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)