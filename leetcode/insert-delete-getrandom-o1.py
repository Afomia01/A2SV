class RandomizedSet:

    def __init__(self):
       
        self.list=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.list:
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.list:
            self.list.remove(val)
            return True
    
    def getRandom(self) -> int:
        
           index =randint(0, len(self.list)-1)
           return self.list[index]

            
            #num=self.set.pop()
            #self.set.add(num)
            #return num
            
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()