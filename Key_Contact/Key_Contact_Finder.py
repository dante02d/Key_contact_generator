import numpy as np
class Key_contac_finder:
    windowSize = 3
    matrixXLimit =360
    matrixYLimit = 180

    def __init__(self):
        print ("xx")

    def getWindowIndexs(self,i,j):
        indexArray = np.array([self.windowSize*self.windowSize])
        indexArray.fill(-1)
