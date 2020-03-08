from collections import deque 
from droneQueue import droneQueue
from itemQueue import itemQueue  
import math

class droneScheduler():

    dronelist = []
    itemlist = []
    distlist = []
    maplist= []

    def distance(self,x1 , y1 , x2 , y2): 
        return math.hypot(x2 - x1, y2 - y1)
    
    def getdronelist(self):
        dq=droneQueue()
# ENTER DRONES COORDINATES HERE

        dq.insert((5,5)) 
        dq.insert((2,9))
        drones=dq.getQueue()
        for i in range(0,len(drones)):
            self.dronelist.append(drones[i])
    
    def getitemlist(self):
        iq = itemQueue()

# ENTER ITEM COODRINATES HERE
        iq.insert((1,2)) 
        iq.insert((2,4)) 
        iq.insert((5,7))
        iq.insert((7,3)) 
        items = iq.getQueue()
        for i in range(0, len(items)):
            self.itemlist.append(items[i])
    
    def createList(self,dlist,ilist):
       # print(self.itemlist)
        for i in self.dronelist:
            for j in self.itemlist:
                self.distlist.append(self.distance(i[0],i[1],j[0],j[1]))
        return self.distlist
    
    def check(self):
        li = self.createList(self.getdronelist(),self.getitemlist())
        while len(self.itemlist)!=0:
                itemNo = li.index(min(li)) %  len(self.itemlist)
                #print(min(li),itemNo,self.itemlist,li)
                print('GOTO Coordinates ')
                print(self.itemlist[itemNo])
                li.clear()
                self.maplist.append(itemNo)
                del self.itemlist[itemNo]
                if len(self.dronelist)!=1:
                    lastdrone = self.dronelist.pop(0)
                    li = self.createList(self.dronelist, self.itemlist)
                    self.dronelist.append(lastdrone)
                else :
                    li = self.createList(self.dronelist, self.itemlist)
                print('==============')

                

    
    
    # def getMapping(self):
    #     li = self.createList()
    #     print(li)
    #     c=0
    #     m = len(li)
    #     n =  len(self.itemlist)
    #     print(m,n)
    #     for i in range(0,m,n):
    #         print('i '+str(i) + ' '+ str(min(li[i:i+n])))
    #         itemNo = li.index(min(li[i:i+n])) % n
    #         #print('Drone '+str(int(i/len(self.itemlist))+1) +'--> item '+str(itemNo+1))
    #         self.maplist.append(itemNo)
    #         print(itemNo)
    #         del self.itemlist[itemNo]
    #         print(self.itemlist, len(self.itemlist))
    #         print(c,self.dronelist)
    #         if len(self.dronelist)==0:
    #             break
    #         else:
    #             del self.dronelist[c]
    #             c=c+1
    #         print(self.dronelist)
    #         print('-----------')


    def dispatcher(self):
        self.check()
        # print(self.maplist)



obj = droneScheduler()
#print(obj.createList())
obj.dispatcher()
