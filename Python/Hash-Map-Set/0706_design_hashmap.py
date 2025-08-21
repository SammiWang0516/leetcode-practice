# 706 Design HashMap
'''
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
'''
''' only use list
class MyHashMap(object):
    def __init__(self):
        self.list = []
    def put(self, key, value):
        if len(self.list) == 0:
            self.list.append([key, value])
        else:
            count = 0
            while count < len(self.list):
                if self.list[count][0] == key:
                    self.list[count][1] = value
                    break
                else:
                    count += 1
            if count == len(self.list):
                self.list.append([key, value])
        return self.list
    def get(self, key):
        for small_list in self.list:
            if small_list[0] == key:
                return small_list[1]
        return -1
    def remove(self, key):
        for i in range(len(self.list)):
            if self.list[i][0] == key:
                self.list.pop(i)
                break
        return self.list
'''
'''
class MyHashMap(object):
    def __init__(self):
        # since there is no need to ouput the whole hashmap, then i can store key using set()
        # however, value can duplicate, so ill use list to store the value
        # key and value share the same index, but set() has no index
        self.key = set()
        self.list = []
    def put(self, key, value):
        if key not in self.key:
            self.list.append([key, value])
            self.key.add(key)
        else:
            for small_list in self.list:
                if small_list[0] == key:
                    small_list[1] = value
        return self.list
    def get(self, key):
        if key not in self.key:
            return -1
        else:
            for small_list in self.list:
                if small_list[0] == key:
                    return small_list[1]
    def remove(self, key):
        n = len(self.list)
        if key in self.key:
            self.key.remove(key)
            for i in range(n):
                if self.list[i][0] == key:
                    self.list.pop(i)
                    break
'''
class MyHashMap(object):
    # change the key to the index of the list
    # this case, i can find the value through the index (key)
    # those indexes which has no value or no put function will remain None
    def __init__(self):
        self.data = [None] * 1000000
    def put(self, key, value):
        self.data[key] = value
    def get(self, key):
        if self.data[key] != None:
            return self.data[key]
        else:
            return -1
    def remove(self, key):
        self.data[key] = None
hashmap = MyHashMap()
print(hashmap.put(1, 1))
print(hashmap.put(2, 2))
print(hashmap.get(1))
print(hashmap.get(3))
print(hashmap.put(2, 1))
print(hashmap.get(2))
print(hashmap.remove(2))
print(hashmap.get(2))