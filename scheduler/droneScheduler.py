from collections import deque 
from droneQueue import droneQueue
from itemQueue import itemQueue  
from destinationQueue import destinationQueue
import math

class droneScheduler():

    drones = deque()
    items = deque()
    destinations = deque() 
    maplist= []
    droneToItem= []
    itemToDestination= []

    def distance(self,x1 , y1 , x2 , y2): 
        return math.hypot(x2 - x1, y2 - y1)

  
    def getdronelist(self):
        dq=droneQueue()
    
    # ENTER DRONES COORDINATES HERE
        dq.insert((4,9)) 
        dq.insert((7,2))

        self.drones = dq.getQueue()
    
    def getitemlist(self):
        iq = itemQueue()

    # ENTER ITEM COODRINATES HERE
        iq.insert((2,5)) 
        iq.insert((10,5)) 
        iq.insert((10,3))
        iq.insert((6,3)) 
        self.items = iq.getQueue()


    def getdestinationlist(self):
        desq = itemQueue()

    # ENTER ITEM DESTINATION COODRINATES HERE
        desq.insert((10,10)) 
        desq.insert((1,1)) 
        desq.insert((3,8))
        desq.insert((8,3)) 
        self.destinations = desq.getQueue()

    def createList(self,no):

        if no == 1:
            for i in range(len(self.drones)):
                self.droneToItem.append(self.distance(self.drones[i][0],self.drones[i][1],self.items[0][0],self.items[0][1]))

        elif no == 2:
            for i in range(len(self.items)):
                self.itemToDestination.append(self.distance(self.items[i][0],self.items[i][1],self.destinations[i][0],self.destinations[i][1]))

    

    def schedule(self):

        try:

            self.getdronelist()
            self.getitemlist()
            self.getdestinationlist()
            self.createList(1)
            self.createList(2)
            li=[]

            for i in range(len(self.droneToItem)):
                li.append( self.droneToItem[i] + self.itemToDestination[0] )    

            while len(self.items)!=0:
                    print('droneToItem',self.droneToItem)
                    print('itemToDestination',self.itemToDestination)
                    print('li',li)     

                    droneNo = li.index(min(li))
                    print('Drone',droneNo,' =>Coordinates ',self.items[0] )
                    
                    li.clear()
                    self.droneToItem.clear()
                    self.itemToDestination.clear()
                    self.maplist.append(droneNo)
                    del self.items[0]
                    pos = self.destinations.popleft()
                    self.drones[droneNo] = pos
                    if len(self.items) != 0:
                        self.createList(1)
                        self.createList(2)
                        for i in range(len(self.droneToItem)):
                            li.append( self.droneToItem[i] + self.itemToDestination[0] )
                    print('==============')
        
        except:
            print('Check if both item and destination position is available')


obj = droneScheduler()
obj.schedule()
