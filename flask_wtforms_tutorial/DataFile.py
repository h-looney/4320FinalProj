from os.path import exists
from inspect import signature


class DataFile:

    __param_count = 0

    def __set_param_count(self):
        self.__param_count = len(signature(self.__obj.__init__).parameters) - 1

    def __assign_to_obj(self, d):
        return self.__obj(*d[:self.__param_count])
    
    filename = 'reservations.txt'
    def __init__(self, filename, delimiter=', ', obj=None):
        self.__data = []
        self.__filename = filename
        self.__obj = obj
        if obj:
            self.__set_param_count()
        if exists(filename):
            with open(filename, 'r') as file:
                for line in file.readlines():
                    d = line.replace('\n', '').split(delimiter)
                    self.__data.append(self.__assign_to_obj(d) if obj else d)

    def read(self):
        return self.__data

    def write(self, data):
        self.__data.append(data)
        with open(self.__filename, 'a') as file:
            file.write(f'{repr(data)}\n')
