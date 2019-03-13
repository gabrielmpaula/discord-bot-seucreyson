from os import chdir, listdir
from os.path import isdir, isfile, join


class FilesManagement:

    @staticmethod
    def get_sorted_folders_list(path_):
        chdir(path_)
        _files_list = [f for f in listdir(path_) if isdir(f)]
        _sorted_list = sorted(_files_list)
        return _sorted_list

    @staticmethod
    def get_sorted_files_list(path_):
        chdir(path_)
        _files_list = [join(path_,f) for f in listdir(path_) if isfile(f)]
        _sorted_list = sorted(_files_list)
        return _sorted_list
