def calculate_discount(customer_type, bill_amount):
    if customer_type == 'regular':
        discount = bill_amount * 0.1
        final_amount = bill_amount - discount
        print(f"Final amount after discount: {final_amount}")
    elif customer_type == 'prime':
        discount = bill_amount * 0.2
        final_amount = bill_amount - discount
        print(f"Final amount after discount: {final_amount}")
    elif customer_type == 'vip':
        discount = bill_amount * 0.3
        final_amount = bill_amount - discount
        print(f"Final amount after discount: {final_amount}")
    else:
        print("Invalid customer type")

calculate_discount('regular', 1000)
calculate_discount('prime', 2000)
calculate_discount('vip', 3000)
