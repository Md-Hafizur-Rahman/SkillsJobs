from customer import Customer
from customerImp import CustomerImp

# name, age, nid, address : account number, opening balance, deposit widthdraw
class Account(Customer):
    def __init__(self, name, age, nid, address,blance):
        super(Account, self).__init__(name=name, age=age, nid=nid, address=address)
        self.__balance=blance
        
        
    # Function to deposite amount

    def deposit(self):
        print("\n Your current amount:", self.__balance)
        YesNo=(str(input('Can you want to deposit amount (y/n): ')))
        if YesNo=='y': 
            amount = float(input("Enter amount to be deposited: "))
            self.__balance += amount
            print("\n Amount Deposited:", amount)
            return amount
        else:
            print('Nothing deposit.')
            
    # Function to withdraw the amount
    
    def withdraw(self):
        YesNo=(str(input('Can you want to withdraw amount (y/n): ')))
        if YesNo=='y':
            amount = float(input("Enter amount to be withdrawn: "))
            if self.__balance >= amount:
                self.__balance -= amount
                print("\n You Withdrew:", amount)
                return amount
            else:
                print("\n Insufficient balance ")
        else:
            print('Norhing withraw.')
    
    # Function to display the amount
        
    def display(self):
        print("\n Net Available Balance =", self.__balance)
        
    # Function to update the amount
       
    def update(self):
        YesNo=(str(input('Can you want to update amount (y/n): ')))
        if YesNo=='y':
            
            amount=float(input('Enter your amount to be updated: '))
            self.__balance+=amount
            print('courent amout is: ',self.__balance)
            return amount
        else:
            print('Nothing to updated.')
            print("\n Your current amount:", self.__balance)
            
        
    def __str__(self):
        return "{} is a customer.zer deposit money:{} , withraw money: {} , Zer updated amount:{} and current amount is:{} ".format(self.get_name(),self.deposit(),self.withdraw(),self.update(),self.__balance)


''' account=Account('hafiz','20','1234','dhaka')
print(account) '''