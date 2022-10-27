from account import Account



class Bank:
    def sum_balance(accounts):
        if isinstance(accounts, (list, tuple)):
            total = 0
            for account in accounts:
                if isinstance(account, Account):
                    total += account.balance

            return total


    def show_all_account(accounts):
        if isinstance(accounts, (list, tuple)):
            msg = "Account:\n"
            for account in accounts:
                if isinstance(account, Account):
                    msg += account.get_info()

            return msg

    def calc_sum_after_month(accounts):
        if isinstance(accounts, (list, tuple)):
            total = 0
            for account in accounts:
                if isinstance(account, Account):
                    total += account.balance * (1 + account.cofficient)

            return round(total, 2)