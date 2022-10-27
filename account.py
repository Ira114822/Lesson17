class Account:
    #constructor with params
    def __init__(self, id, balance, name, cofficient=0.01):
        self.id = id
        self.balance = balance
        self.name = name
        self.cofficient = cofficient

    def __del__(self):
        pass

    def get_info(self):
        return (f"{id}: "
                f"balance = {self.balance},"
                f"name = {self.name},"
                f"cofficient = {self.cofficient}")