print('Hello! This programm allows you to calculate your net pay.')
print('The system requires hours worked and rate of pay.')
print('You cannot insert an amount that excess 40 hours!')
while True:
    try:
        hours_worked = float(input('Please, enter your hours worked: '))
        if hours_worked < 1:
            print('Please the number needs to be positive and different than 0!')
        elif hours_worked > 40:
            print('You cannot insert an amount that excesses 40 hours!')
        elif hours_worked <= 40:
            print(f'Hours worked inserted: {hours_worked}')
            break
    except:
        print('You must insert an integer or float number!')

while True:
    try:
        rate_of_pay = float(input('Please, enter your rate of pay: '))
        print(f'This is the rate of pay inserted:{rate_of_pay}')
        if rate_of_pay <= 0:
            print('Please the number needs to be positive and different than 0!')
        elif rate_of_pay > 0:
            gross_pay = hours_worked * rate_of_pay
            print(f'This is your gross pay: {gross_pay}')
            print('This program will calculate: FWT =  20%, FICA = 8%, and the state income tax = 2% of the gross '
                  'pay.')
            FWT = (gross_pay * 0.20)
            print(f'The FWT is = {FWT}')
            FICA = (gross_pay * 0.08)
            print(f'This is the value of FICA = {FICA}')
            state_income_tax = (gross_pay * 0.02)
            print(f'This is the state income tax = {state_income_tax}')
            net_pay = gross_pay - (FWT + FICA + state_income_tax)
            print(f'In conclusion, this is your Net Pay: {net_pay}')
            break
    except:
        print('You must insert an integer or float number!')
