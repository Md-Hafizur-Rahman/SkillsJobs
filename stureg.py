from unicodedata import name
from student import Student

class Student_Reg(Student):
    def __init__(self,name,dep,id,phone,sem:str, credit:int):
        super(Student_Reg, self).__init__(name=name,dep=dep,id=id,phone=phone)
        self.__sem=sem
        self.__credit=credit
        self.__per_credit_fees = 5000
        self.__total_fees = self.__credit * self.__per_credit_fees
        self.__have_waiver = 0
        self.__waiver = 10
        self.__is_registered = 0

    def __get_waiver(self, waiver):
        if waiver == 1:
            self.__total_fees = self.__total_fees - (self.__total_fees*self.__waiver)/100
            self.__have_waiver = 1
            return self.__total_fees
        else:
            return self.__total_fees

    def first_installment(self, have_waiver=0):
        if have_waiver == 1:
            return (self.__get_waiver(1) * 35) / 100
        else:
            return (self.__get_waiver(0) * 35) / 100

    def get_registered(self, payment):
        amount1st = self.first_installment()
        print('afer waiver, due: amount'+ str (self.__total_fees))
        if payment >= amount1st:
            self.__is_registered = 1
            print("You are successfully registered")
            self.__total_fees = self.__total_fees - payment
            print("after register, Due amount: ", self.__total_fees)
        else:
            print("please give your minimum amount : ", amount1st)
    def __str__(self, ):
        return "Name: " + self.get_name() + "\nDept: " + self.get_dep() + "\nSem: " + self.__sem +"\nid:"+ str(self.get_id()) +"\nphone:"+ self.get_phone() + "\nCredit: " + str(
            self.__credit)