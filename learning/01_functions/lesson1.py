def get_customer(customer_id : int) -> dict:
    customer = {
        "id" : customer_id,
        "name" : "Priyansh",
        "email" : "priyanshshrivastav8@gmail.com"
    }
    return customer

def calculate_order_total(price:float,quantity:int) -> float:
    total = price*quantity
    return total

def is_delete_allowed(role:str) -> bool:
    if role == "admin":
        return True
    else :
        return False

customer = get_customer(113)
total = calculate_order_total(100.23,20)
permission = is_delete_allowed("admin")

print(customer)
print(total)
print(permission)
    