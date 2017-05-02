import io

class file_operations:

    def save_file(self,content,path):
        f = open(path , "w")
        f.write(content)
        f.close()

    def read_file(self,path):
        f = open(path, "r")
        return f.read()