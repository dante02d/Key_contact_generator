#from PDB_Operations import key_contact_list_generator as kgen
from PDB_Operations import Viper_Site_Downloader as vsd, ViperDic_to_Object as vparse
from Key_Contact import Capsid_Matrix
#kgen.KeyContact_ListGen().generate_list_of_genus()
#kgen.KeyContact_ListGen().generate_List_Virus_Genus()

print "Geting data from viper"
data= vsd.ViperDBDownloader().downloadInterfaceResidues("2bbv")
#print data
print "Parse data"
vpobj= vparse.ViperToObject().parse(data)
vdbList =[]
vdbList.append(vpobj)
print "Generating CMatrix"
cmatrixGenerator = Capsid_Matrix.Capsid_Matrix()
cmatrixres = cmatrixGenerator.generate_Key_Contact_Matrix(vdbList)
#print cmatrixres
print "tt"

#from viperDB_data import Download_VDB_Viper as dvv
#dvv.Download_VDB_Files_From_Viper().generate_SCP_statement("Cucumovirus")