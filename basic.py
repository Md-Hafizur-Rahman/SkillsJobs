from unicodedata import name
from stureg import Student_Reg

reg = Student_Reg("Hafizur", "CSE", 1234,'23456','5',24)
# print(reg.get_name())
print(reg)
print("First Installment: "+str(reg.first_installment(0)))
reg.get_registered(45000)
# print(reg)