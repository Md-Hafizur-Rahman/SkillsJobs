from unicodedata import name

class Customer: #name, age, nid, address
    def __init__(self, name:str,age:str,nid,address:str):
        self.__name=name
        self.__age=age
        self.__nid=nid
        self.__address=address
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
    def set_nid(self,nid):
        self.__nid=nid
    def set_address(self,address):
        self.__address=address
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_nid(self):
        return self.__nid
    def get_address(self):
        return self.__address
    def __str__(self):
        return f"{self.__name} is a customar .zer age is: {self.__age} , nid no: {self.get_nid()} and address is: {self.__address}  "
''' customer=Customer('Hafiz','25','5432987','Dhaka')
#print(customer) '''
        