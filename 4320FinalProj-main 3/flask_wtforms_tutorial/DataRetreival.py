def calculate_total_sales():
    sales = 0
    with open('reservations.txt', 'r') as file:
        for line in file:
            if len(line.split(',')) == 4:
                sales += 1
    return str(sales) + " Sales"