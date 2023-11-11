def calculate_discount(customer_type, bill_amount):
    discount_rate = 0
    if customer_type == 'regular':
        discount_rate = 0.1
    elif customer_type == 'prime':
        discount_rate = 0.2
    elif customer_type == 'vip':
        discount_rate = 0.3
    else:
        print("Invalid customer type")
        return

    final_amount = bill_amount - (bill_amount * discount_rate)
    print(f"Final amount after discount: {final_amount}")

calculate_discount('regular', 1000)
calculate_discount('prime', 2000)
calculate_discount('vip', 3000)
