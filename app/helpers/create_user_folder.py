import os

class FileSystemManager():
    def users_folder(self,id_u):
        path_user = "app/data/users/{}".format(id_u)
        create = os.mkdir(path_user)
        return create
