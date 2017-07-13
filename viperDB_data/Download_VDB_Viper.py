from PDB_Operations import key_contact_list_generator as kgen
"""
Code developed to download vdb entrys in batch mode by genus
"""
class Download_VDB_Files_From_Viper:
    def generate_SCP_statement(self,genus):
        data = kgen.KeyContact_ListGen().read_genus_virus_list(genus)
        for d in data:
            print "http://viperdb.scripps.edu/VDB/{}.vdb.gz".format(d['entry_id'])