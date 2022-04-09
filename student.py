from unicodedata import name
class Student():
    
    def __init__(self,name:str,dep:str,id:int,phone:str):
        self.__name=name
        self.__dep=dep
        self.__id=id
        self.__phone=phone
    
    def set_name(self,name):
        self.__name=name
    def set_dep(self,dep):
        self.__dep=dep
    def set_id(self,id):
        self.__id=id
    def set_phone(self,phone:str):
        self.__phone=phone
    
    def get_name(self):
        return self.__name
    def get_dep(self):
        return self.__dep
    def get_id(self):
        return self.__id
    def get_phone(self):
        return self.__phone
    def __str__(self):
        return f"{self.__name} is a student of {self.__dep}.Zer id is: {self.__id} and phone is:{self.__phone}"
        
''' student=Student('Hafiz','CSE',181,'01702345678')
print(student.set_phone('017234569'))
print(student.get_phone()) '''