print("Vans & More Depot is an organization that provides van's service.")
print('In order to get a van, it needs to reach its full capacity: 10 people.')
while True:
    try:
        people = int(input('Please, tell us the number of people who need a van: '))
        print(f'This is the number you asked for: {people}.')
        if people <= 0:  # The number must be positive!
            print('Please, insert a number >= 1.')
        elif 1 <= people <= 9:  # if the number does not satisfy the requirement (10 people)
            print(f'Unfortunately, {people} does not satisfy the number of people requested to rent a van.')
            print('You will need to find another way to reach the location.')
            break
        elif people % 10 == 0:  # If the rest equals 0, calculate the number of vans needed.
            van = people // 10
            print(f'You guys will take {van} van/s.')
            break
        elif people % 10 != 0:  # if the rest is NOT equal to 0, calculate the people who will take the van/s and who
            # won't.
            rest = people % 10
            print(f'{rest} person/s need to find another way to reach the location.')
            people_van = people - rest
            number_van = people_van / 10
            print(f'The rest of the group {people_van} people can use {number_van} van/s.')
            break
    except:
        print('Error! Restart the program. You must insert an integer number!')
        # An integer must be entered (no float or str)
print('Well done you made it!')
