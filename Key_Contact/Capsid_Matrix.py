import numpy as np
class Capsid_Matrix:
    Cmatrix = []
    valMatrix = []
    def __init__(self):
        self.Cmatrix = np.matrix((180,360),dtype=str)
        self.valMatrix = np.zeros(180)
        self.init_val_Matrix()

    def init_val_Matrix(self):
        for i in enumerate(self.valMatrix):
            self.valMatrix[i] = 0.0056*(i+1)

    def generate_Key_Contact_Matrix(self,virusList):

        for virus in virusList:
            print ""

    def add_Virus_To_Matrix(self):
        print ""