from functools import reduce
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
        t = "INFOTC4320"
        name = self.name.replace(' ', '')
        y = 0 
        x = 0
        result = ""
        while x < len(name) and y < len(t):
            result += name[x] + t[y]
            x+=1
            y+=1
        while x < len(name):
            result += name[x]
            x += 1
        while y < len(t):
            result += t[y]
            y += 1
        self.e_ticket_num = result

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

    @staticmethod
    def get_cost_matrix():
        cost_matrix = [[100, 75, 50, 100] for _ in range(12)]
        return cost_matrix

    @staticmethod
    def get_total_sales():
        reserved = Reservation.get_all()
        cost_matrix = Reservation.get_cost_matrix()
        return reduce(lambda cost, r: cost + cost_matrix[r[0]][r[1]], reserved, 0)

    @staticmethod
    def get_seating_chart():
        reserved = Reservation.get_all()
        chart = [['O', 'O', 'O', 'O'] for _ in range(12)]
        for r in reserved:
            chart[r[0]][r[1]] = "X"
        return chart

    def __repr__(self):
        return f'{self.name}, {self.row}, {self.column}, {self.e_ticket_num}'
