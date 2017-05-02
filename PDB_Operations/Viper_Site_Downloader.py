import urllib2
import xmltodict

class ViperDBDownloader:
    def downloadInterfaceResidues(self,vdb):
        strDataURL = "http://viperdb.scripps.edu/API2/testapi2.php?VDB="+vdb
        raw_data= urllib2.urlopen(strDataURL)
        rawxml_data = raw_data.read()
        raw_data.close()
        data = xmltodict.parse(rawxml_data)
        return data