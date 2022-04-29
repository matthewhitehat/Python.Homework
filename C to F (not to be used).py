print ('Hello my friend,')
print ('Today I will help you to convert Fahrenheit into Celsius and vice-versa.')
try:
    far = float(input('Please enter your temperature here: '))
    cel = (far - 32) * 5/9 #Formula to convert F to C
    rounda = round (cel, 1)
    print('You made it!')
    print(f'This is your converted temperature in celsius {rounda}')
    print('Thank you for using my program!')
except:
     print('Please insert a number')



   



