#from PDB_Operations import key_contact_list_generator as kgen
from PDB_Operations import Viper_Site_Downloader as vsd, ViperDic_to_Object as vparse
#kgen.KeyContact_ListGen().generate_list_of_genus()
#kgen.KeyContact_ListGen().generate_List_Virus_Genus()

data= vsd.ViperDBDownloader().downloadInterfaceResidues("2bbv")
print data
vpobj= vparse.ViperToObject().parse(data)
print "tt"