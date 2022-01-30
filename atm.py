class Atm:
    def __init__(self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def check_balance(self):
        print("your balance is 50000")
    def withdrawal(self, amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
    card_number = input("enter your card number:")
    pin_number = input("enter your pin number:")
    new_user = Atm(card_number, pin_number)
    print("choose your activity")
    print("1.Balance Enquriy 2.withdrawl")
    activity = int(input("enter activity number:"))
    if (activity == 1):
        new_user.check_balance()
    elif(activity==2):
        amount = int(imput("enter amount:"))
        new_user.withdrawal(amount)
    else:
        print("enter a vaild number")
if __name__ == "__main__":
    main()
