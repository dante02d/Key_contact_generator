class VirusData:
    vdb=""
    entryKey=""
    SIC=""
    subunits = []

    def __init__(self):
        self.subunits = []

class SubUnit:
    virus = ""
    subunitName = ""
    residues = []
    def __init__(self,parentObj):
        self.residues = []
        self.virus = parentObj


class Residues:
    subUnit = ""

    def __init__(self,parentObj):
        self.subUnit = parentObj

    x = 0.0
    y = 0.0
    z = 0.0

    r=0.0
    phi=0.0
    psi= 0.0

    res= ""
    rid=0
    num_int =0

    def toCMatrix_format(self):
        return "{}:{}:{}:{}:{};".format(self.subUnit.virus.vdb,self.subUnit.subunitName,
                                       self.r,self.phi,self.psi)
    #def __str__(self):
