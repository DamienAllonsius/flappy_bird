class Bird:
    def __init__(self,pathBirdImage="images/bird.png"):
        self.pathBirdImage=pathBirdImage
        self.x=150
        self.y=300
        self.weight=0.001

    def getPathBirdImage(self):
        return self.pathBirdImage
    
    def getPositionX(self):
        return self.x
    
    def getPositionY(self):
        return self.y
