def calculate_vat(price):
    # Calculated the VAT (Value Added Tax) for the given price
    return price * 0.19 # <-- Magic Number


def calc(p):
    # Calculates the final price after VAT
    return p + calculate_vat(p)

def calculateDiscount(finalPrice, percentage):
    # Calculates the discount for the given final price and percentage
    return finalPrice * percentage / 100

# order of parameters are inconsistent
def calculateFinalPrice(percentage, price):
    # Calculates the final price after discount
    
    # percentage = 10
    # disount = calculateDiscount(price, percentage)

    return price - calculateDiscount(price, percentage)
    