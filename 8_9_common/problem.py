def calculate_price(quantity, price, tax_rate, discount, shipping, handling):
    
    subtotal = quantity * price
    tax = subtotal * tax_rate
    discount = subtotal * discount
    total = subtotal + tax - discount + shipping + handling
    
    return total

print(calculate_price(10, 100, 0.19, 0.1, 5, 10))