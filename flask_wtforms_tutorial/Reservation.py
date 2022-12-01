from .DataFile import DataFile


# EXAMPLE
# -------
# reservation = Reservation(name, row, column)
# saved = reservation.save()
# -------
# reservations = Reservation.get_all()
# -------

class Reservation:

    __data_filename = 'reservations.txt'
    e_ticket_num = None

    def __init__(self, name, row, column):
        self.name = name
        self.row = int(row)
        self.column = int(column)

    def __gen_e_ticket_num(self):
        # TODO
        self.e_ticket_num = 'placeholder'

    def __is_available(self, data_file):
        reserved = [(r.row, r.column) for r in data_file.read()]
        requested = (self.row, self.column)
        return all(requested != r for r in reserved)

    def save(self):
        data_file = DataFile(self.__data_filename, obj=Reservation)
        if self.__is_available(data_file):
            self.__gen_e_ticket_num()
            data_file.write(self)
            return True
        return False

    @staticmethod
    def get_all():
        data_file = DataFile(Reservation.__data_filename, obj=Reservation)
        return [[r.row, r.column] for r in data_file.read()]

    def __repr__(self):
        return f'{self.name}, {self.row}, {self.column}, {self.e_ticket_num}'
