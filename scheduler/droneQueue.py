from collections import deque 

class droneQueue(): 
    def __init__(self): 
        self.queue = deque() 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue)==0
  
  
    def insert(self, data): 
        self.queue.append(data) 
  
    def delete(self): 
        try: 
            return self.queue.popleft()
        except IndexError: 
            print() 
            exit() 
    def getQueue(self):
        return self.queue
