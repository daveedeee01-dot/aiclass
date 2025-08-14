user_input= input('Enter your name to login:')
user_name=['Dave','ruth','john','santana']
valid =''
for i in user_name:
    if user_input in user_name:
        valid += f'you are mostly welcomed:{user_input}'
        break
    else:
        valid += f'sorry fam! you are not recognized:{user_input}'
        break
print(valid)