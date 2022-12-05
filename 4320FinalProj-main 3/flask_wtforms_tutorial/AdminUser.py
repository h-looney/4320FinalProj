from .DataFile import DataFile


# EXAMPLE
# -------
# user = AdminUser(username, password)
# is_admin = user.is_registered()
# -------

class AdminUser:

    __data_filename = 'passcodes.txt'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_registered(self):
        data_file = DataFile(self.__data_filename, obj=AdminUser)
        admins = [(a.username, a.password) for a in data_file.read()]
        user = (self.username, self.password)
        return any(user == admin for admin in admins)
