print('Hello, here you can calculate your school grade!')
try:
    grade = float(input('Insert here your grade between 0 and 1: '))
    if 1 < grade:
        print('Error! Your grade should be between 0 and 1.')
    elif grade < 0:
        print('Error your grade should be between 0 and 1.')
    elif 0.6 >= grade >= 0:
        print(' Your grade is F')
    elif grade == 0.7:
        print('Your grade is C')
    elif grade == 0.8:
        print('Your grade is B')
    elif grade == 0.9:
        print('Your grade is A')
    elif grade == 1:
        print('Your grade is A+')
except:
    print('Error, you must insert a number. Restart the program!')




