print('Hello, you can use this program to convert dollar in different values.')
while True:
    try:
        dollar_value = float(input('Please enter the dollar amount you want to convert: '))
        if dollar_value <= 0:
            print('PLease enter an amount greater than 0!')
        elif dollar_value > 0:
            print('You can convert the dollar into: Canadian dollar (1), Euro (2), Indian rupee (3), Japanese yen (4),'
                  'Mexican peso (5), South African rand (6), and British pound (7)')
            break
    except:
        print('Error! You must insert a float number!')

while True:
    try:
        value = int(input('Please, insert the value you would to get based on the number listed above: '))

        if value > 7 or value <= 0:
            print("This number is not listed above! Insert another number!")
        elif value == 1:
            canadian_dollar = dollar_value * 1.21
            round1 = round(canadian_dollar, 3)
            print(f'This is your dollar amount converted into canadian dollar: {round1}')
            break
        elif value == 2:
            euro = dollar_value * 0.82
            round2 = round(euro, 3)
            print(f'This is your dollar amount converted into euro: {round2} ')
            break
        elif value == 3:
            indian_rupee = dollar_value * 73.21
            round3 = round(indian_rupee, 3)
            print(f'This is your dollar amount converted into Indian Rupee: {round3}')
            break
        elif value == 4:
            japanese_yen = dollar_value * 109.22
            round4 = round(japanese_yen, 3)
            print(f'This is your dollar amount converted into Japanese Yen: {round4} ')
            break
        elif value == 5:
            mexican_peso = dollar_value * 19.88
            round5 = round(mexican_peso, 3)
            print(f'This is your dollar amount converted into Mexican Peso: {round5}')
            break
        elif value == 6:
            south_african_rand = dollar_value * 14.14
            round6 = round(south_african_rand, 3)
            print(f'This is your dollar amount converted into South African Rand: {round6}')
            break
        elif value == 7:
            british_pound = dollar_value * 0.71
            round7 = round(british_pound, 3)
            print(f'This is your dollar amount converted into British Pound: {round7}')
            break
    except:
        print('Error! You must insert a float number!')
