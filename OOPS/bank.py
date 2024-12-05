class Bankaccount:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter the deposit amount: "))
        self.balance+=amount
        print("deposit amount: ",amount)
    def withdraw(self):
        amount=float(input("Enter withdraw amount: "))
        if self.balance>=amount:
            self.balance-=amount
            print("Withdraw",amount)
        else:
            print("no balance")
    def display(self):
        print("Your balance is: ",self.balance)
        
s=Bankaccount()
while True:
    print("1.deposit\n2.withdraw\n3.balance\n4.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        s.deposit()
    elif choice==2: 
        s.withdraw()
    elif choice==3:    
        s.display()
    elif choice==4:
        break
    else:
        print("you press invalid choice")
            