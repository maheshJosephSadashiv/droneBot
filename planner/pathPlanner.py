# from tello_commands import TelloClass



class pathPanner:

    def __init__(self):

        self.direction = 0 
        '''
        0-> North
        1-> East
        2->South
        3->West
        '''
    def start(self):
        # TelloClass.create_tello_object(self)
        # TelloClass.tello_connect(self)
        # TelloClass.tello_takeoff(self)
        print('Took off')

    def end(self):
        # TelloClass.tello_land(self)
        # TelloClass.tello_end(self)
        print('landed')

    def updateDirection(self, turn):
        if turn=='r':
            #TelloClass.tello_rotate_clockwise(90)
            print('Turned Right')
            self.direction = (self.direction+1)%4
        elif turn=='l':
            print('Turned Left')
            self.direction = (self.direction+3)%4

    def firstQuadrant(self, resx=20, resy=20):
        self.start()
        while(self.direction!=0):
            self.updateDirection('r')
        # TelloClass.tello_forward_cm(self,resy)
        print('Forward'+ str(resy))
        # TelloClass.tello_right_cm(self,resx)
        print('Right'+ str(resx))        
        self.end()

    def secondQuadrant(self, resx=20, resy=20):
        self.start()
        while(self.direction!=0):
            self.updateDirection('r')
        # TelloClass.tello_forward_cm(self,resy)
        print('Forward'+ str(resy))
        # TelloClass.tello_left_cm(self,resx)  
        print('Left'+ str(resx))      
        self.end()
        
    def thirdQuadrant(self, resx=20, resy=20):
        self.start()
        while(self.direction!=2):
            self.updateDirection('r')
        # TelloClass.tello_forward_cm(self,resy)
        print('Forward'+ str(resy))
        # TelloClass.tello_right_cm(self,resx) 
        print('Right'+ str(resx))       
        self.end()

    def fourthQuadrant(self, resx=20, resy=20):
        self.start()
        while(self.direction!=2):
            self.updateDirection('r')
        # TelloClass.tello_forward_cm(self,resy)
        print('Forward'+ str(resy))
        # TelloClass.tello_left_cm(self,resx)  
        print('Left'+ str(resx))      
        self.end()


    def plan(self, src, dst):
        x1, y1 = src[0], src[1]
        x2, y2 = dst[0], dst[1]
        resx, resy = x2-x1, y2-y1
        print(resx, resy)
        if resx>0 and resy>0:
            self.firstQuadrant(resx, resy)
        elif resx<0 and resy>0:
            self.secondQuadrant(resx*-1, resy)
        elif resx<0 and resy<0:
            self.thirdQuadrant(resx*-1, resy*-1)
        elif resx>0 and resy<0:
            self.fourthQuadrant(resx, resy*-1)


obj = pathPanner()
src = tuple(map(int,input('Enter src coordinates: ').split()))
dst = tuple(map(int,input('Enter dst coordinates: ').split()))
print(src, dst)
obj.plan(src, dst)
