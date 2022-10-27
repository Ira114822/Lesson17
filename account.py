class Account:
    def init(self, id, balance, name, cofficient=0.01):
        self.id = id
        self.balance = balance
        self.name = name
        self.cofficient = cofficient

    def get_info(self):
        return (f"{id}: "
                f"balance = {self.balance},"
                f"name = {self.name},"
                f"cofficient = {self.cofficient}")