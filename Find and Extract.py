print('Exercise 1: Take the following Python code that stores a string: \n'
      'str = ’X-DSPAM-Confidence: 0.8475 \n'
      'Use find and string slicing to extract the portion of the string after the colon \n'
      'character and then use the float function to convert the extracted string into a \n'
      'floating point number.\n')


str = 'X-DSPAM-Confidence: 0.8475'
print(str)
find_column = str.find(':')
number = str[find_column + 1:]
float_number = float(number)
print(f'The float number is: {float_number}')
