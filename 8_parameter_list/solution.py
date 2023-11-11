class Order:
    def __init__(self, quantity, price, tax_rate, discount, shipping, handling):
        self.quantity = quantity
        self.price = price
        self.tax_rate = tax_rate
        self.discount = discount
        self.shipping = shipping
        self.handling = handling
    
    def calculate_subtotal(self):
        return self.quantity * self.price
    
    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate
    
    def calculate_discount(self):
        return self.calculate_subtotal() * self.discount
    
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        total = subtotal + tax - discount + self.shipping + self.handling
        return total

order = Order(10, 100, 0.1, 0.05, 10, 5)
total = order.calculate_total()