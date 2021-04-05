import os

class FileSystemManager():
    def users_folder(self,id_u):
        path_user = "app/data/users/{}".format(id_u)
        create = os.mkdir(path_user)
        return create
    
    def actas_folder(self, id_a,id_u):
        path_acta = "app/data/users/{}/{}/anexos".format(id_u, id_a)
        create = os.mkdir(path_acta)
        return create
