VAT = 0.19

def calculate_vat(price: float):
    return price * VAT


def calculate_total(price):
    return price + calculate_vat(price)


def calculate_discount(price, percentage):
    return price * percentage / 100


def calculate_final_price(price, percentage):
    return price - calculate_discount(price, percentage)
    