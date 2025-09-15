import random

name = input('Hello! What is your full name?')
print(f'Welcome {name}!')

def reverse_and_display(name):
    '''
    Takes a string and reverses it
    Args:
        name (str): the string that will be reversed
    Returns:
        print: the reversed string
    '''
    reversed_string = name[::-1]
    print(reversed_string)

def vowel_count(name):
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        name (str): the string that its number of vowels are being determined 
    Returns:
        print: number of vowels in the string
    '''
    vc = 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for letter in name:
        if letter in vowels:
            vc +=1
    print(vc)

def consonant_frequency(name):
    '''
    Takes a string and returns the number of consonants in it 
    Args:
        name (str): the string that its number of consonants are being determined 
    Returns:
        print: number of consonants in the string
    '''
    cc = 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for letter in name:
        if letter not in vowels:
            cc +=1
    print(cc)

def return_first_name(name):
    '''
    Takes a full name and returns the first name
    Args:
        name (str): the original full name 
    Returns:
        the first name
    '''
    space = 0
    output = ''
    for char in name:
        if char == ' ':
           space +=1
    if space < 1:
        output = name
    else:
        for letter in name:
            if letter == ' ':
                break
            else:
                output = output + letter
    return output

def return_last_name(name):
    '''
    Takes a full name and returns the last name
    Args:
        name (str): the original full name 
    Returns:
        the last name
    '''
    space = 0
    output = ''
    for char in name:
        if char == ' ':
           space +=1
    if space < 1:
        output = "NO LAST NAME"
    
    else:
        for i in range(len(name)-1, -1, -1):
            if name[i] == ' ':
                break
            else:
                output = output + name[i]
    
    return output

#def reverse_string()

def return_middle_name(name):
    '''
    Takes a full name , determines if thers a middle name, and returns the possible middle name(s)
    Args:
        name (str): the original full name
    Returns:
        the middle name(s)
    '''
    space = 0
    for char in name:
        if char == ' ':
           space +=1
    if space <= 1:
        middle = "NO MIDDLE NAME"
    else:
        beg = 0
        end = len(name)-1
        for i in range(0, len(name)):               #get first found space
            if name[i] == ' ':
                beg +=1
                break
            else:
                beg +=1
        for i in range(len(name)-1, -1, -1):          #get last found space
            if name[i] == ' ':
                break
            else:
                end-=1
        middle = name[beg:end]
    return middle

def check_hyphen(name):
    hyphen = 0
    for char in name:
        if char == "-":
            hyphen +=1
            break
    if hyphen > 0:
        return True
    else:
        return False

def get_initials(First, Last):
    '''
    Takes a name, prints and returns the initials
    Args:
        First (str): the first name
        Last (str): the last name
    Returns:
        print: the initials of the name
        return: the initials of the name
    '''
    firstI = list(First)
    lastI = list(Last)
    return(firstI[0],lastI[0])

def convert_to_lowercase(name):
    output = ''
    for char in name:
        int_value = ord(char)
        if int_value < 91 and int_value > 65 :
            int_value = int_value + 32
            char2 = chr(int_value)
            output = output + char2
        else:
            output = output + char
    return output

def convert_to_uppercase(name):
    output = ''
    for char in name:
        int_value = ord(char)
        if int_value > 91 and int_value < 123:
            int_value = int_value - 32
            char2 = chr(int_value)
            output = output + char2
        else:
            output = output + char
    return output

def mix_up_name(name):
    letters = list(name)
    #scrambled = 
    #return scrambled

#def check_palindrome(name):


def main():
    while True:
        option = input('What would you like to do? \n 1. Reverse and Display your name, \n 2. count the vowels in your name, \n 3. count the number of consonants in your name, \n 4. display your first name, \n 5. display your last name, \n 6. display your middle name, \n 7. return boolean if name contains a hyphen, \n 8. convert name to all lowercase, \n 9. convert name to all uppercase, \n 10. scramble the letters of your name, \n 11. check if your first name is a palindrome, \n 14. display your first and last initials. \n (Respond with the corresponding number or stop): ')
        if option == '1':
            reverse_and_display(name)
        elif option == '2':
            vowel_count(name)
        elif option == '3':
            consonant_frequency(name)
        elif option == '4':
            print(return_first_name(name))
        elif option == '5':
            print(return_last_name(name))
        elif option == '6':
            print(return_middle_name(name))
        elif option == '7':
            print(check_hyphen)
        elif option == '8':
            print(convert_to_lowercase(name))
        elif option == '9':
            print(convert_to_uppercase(name))
        #elif option == '10':
            #print(mix_up_name(name))
        #elif option == '11':
            #print(check_palindrome(name))
        elif option == '14':
            print(get_initials(return_first_name(name), return_last_name(name)))
        elif option == 'stop':
            break
        else:
            print('INVALID RESPONSE!!')


main()