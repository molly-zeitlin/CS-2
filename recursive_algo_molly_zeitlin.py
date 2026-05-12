def factorial(n):
    '''
    Calculate the factorial of n
    Arguments:
        n (int): the number to calculatre the factorial of
    Returns:
        (int) the factorial of n
    '''
    if n==0:
        return 1
    return n*factorial(n-1)

def summation(n):
    '''
    Calculate the summation of n
    Arguments:
        n (int): the number to calculate the summation of
    Returns:
        (int) the summation of n
    '''
    if n == 0:
        return 0
    return n + summation(n-1)

def powers(a,n):
    '''
    Calcuate the value of a number to the power of another number
    Arguments:
        a (int): the base of the exponential function
        n (int): the exponent
    Returns:
        (int) a to the power of n
    '''
    if n == 0:
        return 1
    return a*powers(a,n-1)

def sum_of_digits(n):
    '''
    Calculate the sum of the digits of a number
    Arguements:
        n (int): the number to calculate the sum of its digits
    Returns:
        (int) the sum of the digits of n
    '''
    if n < 10:
        return n
    return sum_of_digits(n//10) + n%10 #n%10 find the remainder of n divided by 10

def fibonacci(n):
    '''
    Find the value of a number in Fibonacci's sequence based on its index
    Arguemnets:
        n (int): the index of a number in Fibonacci's sequence
    Returns:
        (int) a value in Fibonacci's sequence
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def gcd(x,y):
    '''
    Find the greatest common denominator of two numbers
    Arguments:
        x (int): a number
        y (int): another number
    Returns
        (int): the greatest common denominator of x and y
    '''
    if (y <= x) and (x%y == 0): #x%y find the remainder of x divided by y
        return y
    return gcd(y,x%y)

def main():
    name = input("Enter your name: ")
    print(f"Welcome {name}!")
    turns = 0
    while True:
        user_choice = input("1. Find the factorial of a number\n2. Find the summation of a number\n3. Find the value a number to the power of another number\n4. Find the sum of a number's digits\n5. Calculate a number in Fibonacci's sequence\n6. Find the greatest common demoninator of two numbers\n7. or quit!\nWhich of the option would you like to do?")
        if user_choice == "1":
            fac_number = input("Enter the number you want to find the factorial of: ")
            print(factorial(int(fac_number)))
            turns +=1
        elif user_choice == "2":
            sum_number = input("Enter the number you want to find the summation of: ")
            print(summation(int(sum_number)))
            turns +=1
        elif user_choice == "3":
            pow_number1 = input("Enter the number you want to start with: ")
            pow_number2 = input("Enter the exponent: ")
            print(powers(int(pow_number1), int(pow_number2)))
            turns +=1
        elif user_choice == "4":
            digits_number = input("Enter the number you want to find the sum of its digits: ")
            print(sum_of_digits(int(digits_number)))
            turns +=1
        elif user_choice == "5":
            fib_number = input("Enter the index of the number you want find in Fibonacci's seuqence: ")
            print(fibonacci(int(fib_number)))
            turns +=1
        elif user_choice == "6":
            gcd_number1 = input("Enter your first number: ")
            gcd_number2 = input("Enter your second number: ")
            print(gcd(int(gcd_number1), int(gcd_number2)))
            turns +=1
        elif user_choice == "7":
            break
        else:
            print("INVALID RESPONSE")

main()