import viperDBConnection as viper


class viperData:

    def get_virusData_From_Family_HighRes(self,virusFam):
        sql= "select entry_key,entry_id,name,genus,family,generic_name,resolution "\
                "from viper where family='{}' and resolution > 0 and resolution < 3.8;".format(virusFam)
        return viper.getDataFromAQuerry(sql)

    def get_virusData_From_Genus_HighRes(self,virusGen):
        sql= "select v.entry_key,v.entry_id,name,v.genus,v.family,v.generic_name,cast( v.resolution as json) as resolution, l.tnumber "\
            "from viper as v " \
            "inner join layer as l on v.entry_key = l.entry_key " \
             "where v.genus='{}' and v.resolution > 0 and v.resolution < 3.8;".format(virusGen)
        return viper.getDataFromAQuerry(sql)

    def get_existing_families_HighRes(self):
        sql="select family "\
            "from viper "\
            "where resolution > 0 and resolution < 3.8 and family not in ('NA','','Unclassified')"\
            "group by family ;"
        return viper.getDataFromAQuerry(sql)

    def get_existing_genus_HighRes(self):
        sql =   "select genus "\
                "from viper "\
                "where resolution > 0 and resolution < 3.8 and " \
                "genus not in ('','N/A','Unclassified','P22virus','T7likevirus') " \
                "group by genus ;"
        return viper.getDataFromAQuerry(sql)