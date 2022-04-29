# Write a program that prompts the user to enter a length in feet and inches and outputs the equivalent length
# in centimeters.  If the user enters a negative number or a nondigit number,
# throw and handle an appropriate exception and prompt the user to enter another set of numbers.
# Use ANY language with which you are familiar to complete this assignment.
while True:
    try:
        user_length_feet = int(input('Insert your length in feet: \n'))
        if user_length_feet <= 0:
            print('Insert a number greater than 0!')
        else:
            break
    except:
        print('You must insert an integer number!')


while True:
    try:
        user_length_inches = int(input('Insert your length in inches: \n'))
        if user_length_inches <= 0:
            print('Insert a number greater than 0!')
        else:
            break

    except:
        print('You must insert an integer number!')

print(f'This is your length in feet and inches: {user_length_feet}.{user_length_inches}')
centimeters1 = user_length_feet * 30.48
centimeters2 = user_length_inches * 2.54
total_centimeters = centimeters1 + centimeters2
print(f'{user_length_feet}.{user_length_inches} = {total_centimeters} centimeters.')



