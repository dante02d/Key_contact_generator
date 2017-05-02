#from PDB_Operations import key_contact_list_generator as kgen
from PDB_Operations import Viper_Site_Downloader as vsd
#kgen.KeyContact_ListGen().generate_list_of_genus()
#kgen.KeyContact_ListGen().generate_List_Virus_Genus()

data= vsd.ViperDBDownloader().downloadInterfaceResidues("2bbv")
print data
print "tt"