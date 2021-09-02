class Bank:
    bank_name="Federal Bank"
    def account_create(self,account_no,name):
        self.account_no=account_no
        self.name=name
        self.minimum_balance=1000
        self.balance=self.minimum_balance
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("Your",Bank.bank_name,"account has been credited with amount",self.amount)
        print("your current balance is: ",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amount)
            self.balance-=self.amount
            print("available balance is: ",self.balance)
obj=Bank()
num=int(input("enter account number: "))
obj.account_create(num,'rincy')
obj.deposit(15000)
obj.withdraw(1500)
