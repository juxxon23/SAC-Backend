from os import scandir, getcwd
from os.path import abspath
import os

class FileSystemManager():
    
    def users_folder(self, id_u):
        path_user = "app/data/users/{}".format(id_u)
        os.makedirs(path_user)

    
    def actas_folder(self, id_a,id_u):
        path_acta = "app/data/users/{}/{}".format(id_u, id_a)
        os.makedirs(path_acta)


    def ls(self, ruta):
        return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
