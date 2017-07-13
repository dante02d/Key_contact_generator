import numpy as np
from PDB_Operations.Data_Objects import VirusData
import math
class Capsid_Matrix:
    Cmatrix = []
    valMatrix = []
    def __init__(self):
        self.Cmatrix = np.matrix(np.empty([180,360]),dtype=np.str)
        self.Cmatrix[...] = ""
        self.valMatrix = np.zeros(180,dtype=np.float32)
        self.init_val_Matrix()

    def init_val_Matrix(self):
        for i,_ in enumerate(self.valMatrix):
            self.valMatrix[i] = 0.0056*(i+1)

#   Gets the index psi position in the Cmatrix
    def get_psi_Capsid_Matrix_Location(self,psi):
        psi =  (psi*3.1416)/180
        psi = math.cos(psi)
        for i,_ in enumerate(self.valMatrix):
            if((i+1)< self.valMatrix.size):
                if(self.valMatrix[i] < psi and self.valMatrix[i+1]>psi ):
                    return i
        return -1

    def generate_Key_Contact_Matrix(self,virusList):
        for virus in virusList:
            self.add_Virus_To_Matrix(virus)
        return self.Cmatrix

    def add_Virus_To_Matrix(self,vData=VirusData()):
        for subUnit in vData.subunits:
            for res in subUnit.residues:
                self.Cmatrix[self.get_psi_Capsid_Matrix_Location(res.psi),res.phi] += res.toCMatrix_format()