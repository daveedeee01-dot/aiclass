# creating a dict
student_grade= {'dave':74,'huncho':83,'p prime':89,'santana':98,'dee':87,'zip':4,'rachel':97,'denise':85,'cench':73,'notorious':81}
average_grade=sum(student_grade.values())/len(student_grade)
print(f'the average_grade is: {average_grade}')

#highest_score
highest_score= max(student_grade.values())
for student, score in student_grade.items():
    if score == highest_score:
       print(f'highest score:{student}:with:{highest_score}')

#updating_grade
student_grade['denise']=66
print(student_grade)
#students with score above 80
print(f'students with score above 80')
for name,score in student_grade.items():
    if score >80:
        print(f'{name}: {score}')  