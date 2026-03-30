class ListNode:
    def __init__(self, key = -1, value = -1, next = None):

        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        
        self.n = ((10 ** 3) + 1)
        self.hhash = [ListNode()] * self.n
        
    def hash(self, key):
        return key % self.n

    def put(self, key: int, value: int) -> None:

        idx = self.hash(key)
        curr = self.hhash[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
            
        newNode = ListNode(key, value)
        curr.next = newNode

    def get(self, key: int) -> int:

        idx = self.hash(key)
        curr = self.hhash[idx]
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:

        idx = self.hash(key)
        curr = self.hhash[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)