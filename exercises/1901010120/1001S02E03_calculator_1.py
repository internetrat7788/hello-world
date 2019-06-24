print("Welcome to the calculator. ")

# define the function
# use input function to limit only run operation at time, if * then *
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('enter the first number: '))
    number_2 = int(input('enter the second number: '))

    # for + addition
    if operation == '+':
       print('{} + {} = '.format(number_1, number_2))
       print(number_1 + number_2)

    # for subtration
    if operation == '-':
       print('{} - {} = '.format(number_1, number_2))
       print(number_1 - number_2)

    # for multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # for division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("you are typing worng, please run the program again. ")

#call calculator outside the function
calculate()