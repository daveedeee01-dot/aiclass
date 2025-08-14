# program to check students points
def check_points(points):
    if points > 36:
        return'sorry, you have failed'
    else:
        return 'congrats, you have passed'   

user_points= int(input('enter your points'))
result_points= check_points(user_points)

print(result_points)