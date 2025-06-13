    def calculator():
     while True:
     try:
     num1 = float(input('Enter the first number: '))
     num2 = float(input('Enter the second number: '))
     except ValueError:
     print('Invalid input. Please enter a number.')
     continue
     op = input('Enter an operator (+, -, , /): ')
     if op == '+':
     print(num1 + num2)
     elif op == '-':
     print(num1 - num2)
     elif op == '':
     print(num1 * num2)
     elif op == '/':
     if num2 == 0:
     print('Cannot divide by zero')
     else:
     print(num1 / num2)
     else:
     print('Invalid operator. Please enter one of the following: +, -, *, /')
     again = input('Do you want to perform another calculation? (y/n)')
     if again.lower() == 'n':
     break