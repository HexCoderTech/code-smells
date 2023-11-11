
order_total = 0

def add_to_order(price):
    order_total += price

def remove_from_order(price):
    order_total -= price

def print_order():
    print('Your order total is: ', order_total)


class DatabaseConnection:
    def get_user(self):
        # do some database stuff
        return 'user'

db_conn = DatabaseConnection()

def get_user():
    return db_conn.get_user()