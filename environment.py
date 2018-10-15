from plot import *

class Environment:

    def __init__(self,gravity=10,time=10,moveup=3,discountFactorPoints=100,speedPlotsAppearing=500,speedPlotsMoving=1):
        self.gravity=gravity
        self.time=time
        self.moveup=moveup
        self.discountFactorPoints=discountFactorPoints
        self.plotWidthMax=1/10
        self.plotHeightMax=0.75
        self.plotHole=0.3 #0.9 * la hauteur restante
        self.speedPlotsAppearing=speedPlotsAppearing
        self.speedPlotsMoving=speedPlotsMoving
        self.plots=[]
        self.cont=1
        self.points=0

        
    def makePlotRandom(self,width,height):
        xMin=width-random.randrange(1,int(width*self.plotWidthMax))
        xMax=width
        yMin=random.randrange(int(height*self.plotHeightMax))
        yMax=yMin + height*self.plotHole
        self.plots.append(Plot(xMin,xMax,yMin,yMax))


    def movePlots(self):
        if self.plots !=[]:
            for plot in self.plots:
                plot.xMin-=1
                plot.xMax-=1
            
            if self.plots[0].xMax==0:
                self.plots=self.plots[1:]

    def computeCont(self,x,y,h):
        if(y<0 or y>h):
            self.cont=0
            
        if self.plots !=[]:
            if (x>self.plots[0].xMin) and (x<self.plots[0].xMax):
                if (y<self.plots[0].yMin) or (y>self.plots[0].yMax):
                    self.cont=0

        
