# login system
user_input= input('enter your name to login:')
user_name= ['david','mak','p prime','erasto','rachel']

valid=''
for i in user_name:
    if user_input in user_name:
        valid += f"welcome:{user_input}"
        break
    else:
        valid += f"sorry! not recognised:{user_input}"
        break
print(valid)