import re
from customer import Customer

class CustomerImp(Customer):
    def __init__(self, name, age, nid, address,accNo:int,deposit :int):
        super(CustomerImp, self).__init__(name=name, age=age, nid=nid, address=address)
        self.__accNo=accNo
        self.__deposit=deposit
        
    def createAccount(self):
    
        self.__accNo=int(input('Enter the account no :'))
        self.__name = input('Enter the account holder name :')
        self.__deposit = int(input('Enter The Initial amount(>=500 for Saving and >=1000 for current'))
        
        print('Account Created')
        return self.__deposit
    
    def showAccount(self):

       print('Account Number : ',self.__accNo)

       print('Account Holder Name : ', self.__name)

       print('Balance : ',self.__deposit)
    def __str__(self):
        return f"{self.get_name()} is a new costomer,her deposit amount: {self.createAccount()},and blance: {self.__deposit}"
    
''' customerImp=CustomerImp('hafiz','20','1234','dhaka',50,100)
print(customerImp) '''