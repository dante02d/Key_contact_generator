import json
import viperDB_data.viper_VirusData as vdata
from Storage import Pahts,file_io
class KeyContact_ListGen:

    def generate_list_of_genus(self):
        list_of_genus= vdata.viperData().get_existing_genus_HighRes()
        string_file = json.dumps(list_of_genus,separators=('\n',':'))
        file_io.file_operations().save_file(string_file,Pahts.paht_genus_file)

    def read_genus_list_file(self):
        file_content = file_io.file_operations().read_file(Pahts.paht_genus_file)
        file_content = file_content.replace('\n',',')
        return json.loads(file_content)

    def generate_List_Virus_Genus(self):
        genus = self.read_genus_list_file()
        for gen in genus:
            self.generate_Genus_List_Virus(gen["genus"])

    def generate_Genus_List_Virus(self,genusName):
        virusList = vdata.viperData().get_virusData_From_Genus_HighRes(genusName)
        if(len( virusList)> 2):
            string_file = json.dumps(virusList)
            file_io.file_operations().save_file(string_file, Pahts.setup_path_virusList_file(genusName))
        else:
            print "Genus with lees than 2 entries :"+genusName

    def read_genus_virus_list(self,genusName):
        file_content = file_io.file_operations().read_file(Pahts.setup_path_virusList_file(genusName))
        #file_content = file_content.replace('\n',',')
        return json.loads(file_content)