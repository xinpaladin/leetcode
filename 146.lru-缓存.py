#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#


        

# @lc code=start
# class LRUCache:

#     def __init__(self, capacity: int):
#         '''
#         cache = {key: {val:val, index: index}}
#         index_d = {index: key}
#         '''
#         self.cache = {}
#         self.index_d = {}
#         self.capacity = capacity
#         self.cur_capacity = 0
#         self.index_begin = 0
#         self.index_last = 0
        

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             # todo update use
#             old_index = self.cache[key]['index']
#             del self.index_d[old_index]
#             self.index_last += 1
#             self.cache[key]['index'] = self.index_last
#             self.index_d[self.index_last] = key
#             return self.cache[key]['val']
#         else:
#             return -1


#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             old_index = self.cache[key]['index']
#             del self.index_d[old_index]
#             self.index_last += 1
#             self.cache[key] = {'val':value, 'index': self.index_last}
#             self.index_d[self.index_last] = key
#         else:
#             self.index_last += 1
#             self.cache[key] = {'val':value, 'index': self.index_last}
#             self.index_d[self.index_last] = key
#             self.cur_capacity += 1
            
#             while self.cur_capacity > self.capacity:
#                 if self.index_begin in self.index_d:
#                     del self.cache[self.index_d[self.index_begin]]
#                     del self.index_d[self.index_begin]
#                     self.cur_capacity -= 1
                    
#                 self.index_begin += 1

class DLinkedDict:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedDict()
        self.tail = DLinkedDict()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value  
            self.moveToHead(node)
        else:
            node = DLinkedDict(key, value)
            self.addToHead(node)
            self.cache[key] = node
            self.size += 1
            if self.size> self.capacity:
                removed = self.removeTail()
                del self.cache[removed.key]
                self.size -= 1

    def addToHead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node
    
    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

