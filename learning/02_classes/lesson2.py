class Tool:

    def __init__(self,name:str,description:str,risk_level:str):
        self.name=name
        self.description=description
        self.risk_level=risk_level

    def is_destructive(self)->bool:
        return self.risk_level in ["HIGH","CRITICAL"]

get_customer = Tool("get_customer","This tool can gather info about customers","LOW")
update_customer = Tool("update_customer","This tool can update information of customers","LOW")
delete_customer = Tool("delete_customer","This tool can delete the info of customers","CRITICAL")

print(get_customer.is_destructive())
print(get_customer.name)
print(get_customer.description)
print(delete_customer.risk_level)