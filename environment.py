from pole import *

class Environment:

    def __init__(self,gravity=10,time=10,moveup=3,discountFactorPoints=100,speedPolesAppearing=500,speedPolesMoving=1):
        self.gravity=gravity
        self.time=time
        self.moveup=moveup
        self.discountFactorPoints=discountFactorPoints
        self.poleWidthMax=1/10
        self.poleHeightMax=0.75
        self.poleHole=0.3 #0.9 * la hauteur restante
        self.speedPolesAppearing=speedPolesAppearing
        self.speedPolesMoving=speedPolesMoving
        self.poles=[]
        self.cont=1
        self.points=0

        
    def makePoleRandom(self,width,height):
        xMin=width-random.randrange(1,int(width*self.poleWidthMax))
        xMax=width
        yMin=random.randrange(int(height*self.poleHeightMax))
        yMax=yMin + height*self.poleHole
        self.poles.append(Pole(xMin,xMax,yMin,yMax))


    def movePoles(self):
        if self.poles !=[]:
            for pole in self.poles:
                pole.xMin-=1
                pole.xMax-=1
            
            if self.poles[0].xMax==0:
                self.poles=self.poles[1:]

    def computeCont(self,x,y,h):
        if(y<0 or y>h):
            self.cont=0
            
        if self.poles !=[]:
            if (x>self.poles[0].xMin) and (x<self.poles[0].xMax):
                if (y<self.poles[0].yMin) or (y>self.poles[0].yMax):
                    self.cont=0

        
