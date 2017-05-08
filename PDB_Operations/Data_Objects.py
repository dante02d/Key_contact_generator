class VirusData:
    vdb=""
    entryKey=""
    SIC=""
    subunits = []

    def __init__(self):
        self.subunits = []

class SubUnit:
    subunitName = ""
    residues = []
    def __init__(self):
        self.residues = []


class Residues:
    x = 0.0
    y = 0.0
    z = 0.0

    r=0.0
    phi=0.0
    psi= 0.0

    res= ""
    rid=0
    num_int =0