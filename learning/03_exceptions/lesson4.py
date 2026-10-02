def get_customer(customer_id: int) -> dict:

    customers = {
        101 : "Priyansh",
        102 : "Amogh",
        103 : "Pratyush"
    }

    try:
        name = customers[customer_id]
    except KeyError:
        return {"Error":"This customer doesn't exist"}  
    else:
        return {"Name": name}

print(get_customer(101))
print(get_customer(105))