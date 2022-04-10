from decimal import DivisionByZero

''' 
try:
    n=int(input('enter number:\n'))
    p=10/n
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("finally it worked.") '''
    
# custome exceptional handaling

''' class DivisionByZero (Exception):
    pass

def calculator(number):
    try:
        if number>10:
            tn=number+10
            
        elif number<10:
            if number ==0:
                raise DivisionByZero
            tn=10/number
            print('the curent number is :',tn)
            
        else:
            print('nothing to print.')
            
    except DivisionByZero as e:
        print('Cannot divided by zero')
    

print(calculator(2)) '''


users={
    'user1':{
        "mail":'hafizur@gmail.com',
        'pass':'123321'
    },
    'user2':{
        "mail":'hafiz@gmail.com',
        'pass':'123322'
    },
    'user3':{
        "mail":'hafizar@gmail.com',
        'pass':'123323'
    },
}
class NotFountError(Exception):
    pass
def LogIn(user,password):
    try:
        if user=='hafizur@gmail.com' and password=='123321':
            print('login succesfull.')
        else:
            raise NotFountError
    except NotFountError as e:
        print('we can not found.') 
print(LogIn('hafizur@gmail.com','123322'))
    
    