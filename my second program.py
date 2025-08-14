print('WELCOME TO MY NB ACCOUNT')
name='David'
age=17
balance=380000084348
billionaire='true'
print('what is your name')
print(name)
print('how old are u')
print(age)
print('money in the account')
print(balance)
print('are u a billionaire')
print(billionaire)



def multiply(num,num2):
    return num * num2
#invoke the function
result=multiply(100,20)
print(f'the multiplication of 100 and 20 is:{result}')













#BMI CALCULATOR FUNCTION
def calcute_bmi(weight,height):
    bmi=weight,height**2
    return round(bmi,2)
 #user input
w=float(input('enter your weight'))
h=float(input('enter your height in meters'))
#invoke your function
result=calcute_bmi(60,3)
print(f'your bmi is:{result}')