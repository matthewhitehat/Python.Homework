print('Hello,')
print('Today I will help you to convert Fahrenheit into Celsius and vice-versa.')
print('Do you want to convert Fahrenheit or Celsius?')
answer = input('Enter f for converting Fahrenheit or c for Celsius: ')
if answer == 'f':
    F = float(input('Please enter your temperature here: '))
    cel = (F - 32) * 5 / 9 # Formula to convert F to C
    roundA = round(cel, 1)
    print(f'This is your converted temperature in celsius {roundA}')
    print('Thank you for using my program!')
elif answer == 'c':
    C = float(input('Please enter your temperature here: '))
    far = (C * 9/5) + 32  # Formula to convert C to F
    roundB = round(far, 1)
    print(f'This is your converted temperature in fahrenheit {roundB}')
    print('Thank you for using my program!')





   
