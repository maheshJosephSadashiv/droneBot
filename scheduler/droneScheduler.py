from collections import deque 
from droneQueue import droneQueue
from itemQueue import itemQueue  
from destinationQueue import destinationQueue
import math

class droneScheduler():

    dronelist = []
    itemlist = []
    distlist = []
    maplist= []
    destlist = []
    droneToItem= []
    itemToDestination= []
    def distance(self,x1 , y1 , x2 , y2): 
        return math.hypot(x2 - x1, y2 - y1)

  
    def getdronelist(self):
        dq=droneQueue()
# ENTER DRONES COORDINATES HERE

        dq.insert((4,9)) 
        dq.insert((7,2))

        drones=dq.getQueue()
        for i in range(0,len(drones)):
            self.dronelist.append(drones[i])
    
    def getitemlist(self):
        iq = itemQueue()

# ENTER ITEM COODRINATES HERE
        iq.insert((2,5)) 
        iq.insert((10,5)) 
        iq.insert((10,3))
        #iq.insert((7,3)) 
        items = iq.getQueue()
        for i in range(0, len(items)):
            self.itemlist.append(items[i])

    def getdestinationlist(self):
        desq = itemQueue()

# ENTER ITEM DESTINATION COODRINATES HERE
        desq.insert((10,10)) 
        desq.insert((1,1)) 
        desq.insert((3,8))
       # desq.insert((8,3)) 
        items = desq.getQueue()
        for i in range(0, len(items)):
            self.destlist.append(items[i])
    
    def createList(self,no):
        if no == 1:
            for i in self.dronelist:
                self.distlist.append(self.distance(i[0],i[1],self.itemlist[0][0],self.itemlist[0][1]))
            return self.distlist
        elif no == 2:
            for i in range(len(self.itemlist)):
                self.itemToDestination.append(self.distance(self.itemlist[i][0],self.itemlist[i][1],self.destlist[i][0],self.destlist[i][1]))
            return self.itemToDestination
    

    def newCheck(self):

        self.getdronelist()
        self.getitemlist()
        self.getdestinationlist()
        self.droneToItem = self.createList(1)
        self.itemToDestination = self.createList(2)
        li=[]
        for i in range(len(self.droneToItem)):
            li.append( self.droneToItem[i] + self.itemToDestination[0] )    

        while len(self.itemlist)!=0:
                print('droneToItem',self.droneToItem)
                print('itemToDestination',self.itemToDestination)
                print('li',li)     

                droneNo = li.index(min(li))
                print('Drone',droneNo,' =>Coordinates ',self.itemlist[0] )
                
                li.clear()
                self.droneToItem.clear()
                self.itemToDestination.clear()
                self.maplist.append(droneNo)
                del self.itemlist[0]
                pos = self.destlist.pop(0)
                self.dronelist[droneNo] = pos
                if len(self.itemlist) != 0:
                    self.droneToItem = self.createList(1)
                    self.itemToDestination = self.createList(2)
                    for i in range(len(self.droneToItem)):
                        li.append( self.droneToItem[i] + self.itemToDestination[0] )
                print('==============')



    def dispatcher(self):
        self.newCheck()
        #print(self.maplist)



obj = droneScheduler()
obj.dispatcher()
