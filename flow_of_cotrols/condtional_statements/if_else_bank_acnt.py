
fixed_amount=100000
withdraw=int(input("enter the amount to withdraw: "))
if withdraw<fixed_amount:
    balance=fixed_amount-withdraw
    print("your balance amount ", balance)
else:
    print("insufficient balance")
