import Data_Objects
import math
class ViperToObject:
    def parse(self, viperdic):
        viperobj = Data_Objects.VirusData()
        viperobj.vdb = viperdic['viperdb']['@entry_id']
        viperobj.entryKey = viperdic['viperdb']['@entry_key']
        viperobj.SIC = viperdic['viperdb']['@SIC']
        viperobj.subunits = self.parse_subunits(  viperdic['viperdb']['subunit'],viperobj)

        return viperobj

    def parse_subunits(self,subunitData,objvirus):
        subunitArray = []
        for subunit in subunitData:
            objSubunit= Data_Objects.SubUnit(objvirus)

            objSubunit.subunitName = subunit['@n']
            objSubunit.residues= self.parce_residues(subunit,objSubunit)
            subunitArray.append(objSubunit)
        return subunitArray

    def parce_residues(self, subunitRes,objSubunit):
        residuesArray =[]
        for res in subunitRes['datamarker']:
            objRes = Data_Objects.Residues(objSubunit)
            objRes.x = int(res['@x'])
            objRes.y = int(res['@y'])

            objRes.res = res['@res']
            objRes.rid = int( res['@rid'])

            objRes.r = int(res['@r'])
            objRes.phi = int(res['@phi'])
            objRes.psi = int(res['@psi'])
            objRes.num_int = int(res['@num_int'])
            # x,y,z parametros calculados
            objRes.x = (objRes.r*math.sin(objRes.phi)*math.cos(objRes.psi))
            objRes.y = (objRes.r*math.sin(objRes.phi)*math.sin(objRes.psi))
            objRes.z = (objRes.r*math.cos(objRes.phi))
            residuesArray.append(objRes)
        return residuesArray
