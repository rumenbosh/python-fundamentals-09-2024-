print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice = input("Enter the number of your choice (1-4): ")
if choice == '1':
    the_string = input("Enter a string: ")
    substring = input("Pick a word to extract: ")
    word_list = the_string.split(" ")
    print(f'The extracted word is: {substring}')
<<<<<<< HEAD
    print(the_string.replace(substring, ' '))
    entry = input('Printing the string to uppercase format, enter 1 for upper and 2 for lower: ')
    if entry == '1':
        print(the_string.upper())
    if entry == '2':
        print(the_string.lower())
=======
    print('Printing the string to uppercase format: ')
    print(the_string.upper())
>>>>>>> 4888f64e2a59c7bd21c80957ecd4f5f2e9eef563
    replace_this = input("Choose a word to replace: ")
    replacement = input(f"What would you like to replace {replace_this} with?: ")
    word_list[word_list.index(replace_this)] = replacement
    the_string = " ".join(word_list)
    print(the_string)
<<<<<<< HEAD
elif choice == '2':
=======
elif choice == 2:
>>>>>>> 4888f64e2a59c7bd21c80957ecd4f5f2e9eef563
    num1 = float(input('Input number 1: num1 = '))
    num2 = float(input('Input number 2: num2 = '))
    operator = ''
    while operator != 'stop':
        operator = input('Input operation: (+, -, *, /, power or STOP to exit): ')
        if operator == '+':
<<<<<<< HEAD
            print(f'{num1} + {num2} = {num1 + num2}')
        elif operator == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif operator == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
=======
            print(f'num1 + num2 = {num1 + num2}')
        elif operator == '-':
            print(f'num1 - num2 = {num1 - num2}')
        elif operator == '*':
            print(f'num1 * num2 = {num1 * num2}')
>>>>>>> 4888f64e2a59c7bd21c80957ecd4f5f2e9eef563
        elif operator == '/':
            if num2 == 0:
                print('Invalid number 2')
                num2 = float(input('Input valid number 2: num2 = '))
<<<<<<< HEAD
            print(f'{num1} / {num2} = {num1 / num2}')
        elif operator == 'power':
            print(f'{num1} on power {num2} = {num1 ** num2}')
        else:
            print('Invalid operator')
# elif choice == '3':
=======
            print(f'num1 / num2 = {num1 / num2}')
        elif operator == 'power':
            print(f'num1 on power num2 = {num1 ** num2}')
        else:
            print('Invalid operator')
elif choice == 3:
    pass
>>>>>>> 4888f64e2a59c7bd21c80957ecd4f5f2e9eef563
