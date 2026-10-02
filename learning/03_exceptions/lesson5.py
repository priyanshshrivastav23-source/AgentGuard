def delete_customer(role: str, customer_id: int):

    try:
        if role != "admin":
            raise PermissionError("This User is not allowed to delete customer")

        return "customer deleted"

    except PermissionError:
        return "permission denied"

print(delete_customer("admin",101))
print(delete_customer("analyst",103))