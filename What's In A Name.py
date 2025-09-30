#Molly Zeitlin
#Asks user for their full name, and provides 12 different options to the user to manipulate their orignal entry.
#9/30/2025
#build a menu, remove titles ("Dr.", "Sir", etc.), clear screen, pause during code (using time.sleep)

import random                                                                                       #import random library
import os                                                                                           #import os library
import time                                                                                         #import time library
titles = ['Dr.', 'Mrs.', 'Ms.', 'Mr.', 'Sir', 'Esq', 'Ph.d']                                        #create titles list

name = input('Hello! What is your full name?')                                                      #set variable name to user response
print(f'Welcome {name}!')                                                                           #display message

def split_name(name):                                                                               #create function
    names = []                                                                                      #create list
    current = ''                                                                                    #set current to ''
    for char in name:                                                                               #create for loop
        if char == ' ':                                                                             #if char is the same as ' '
            if len(current) > 0:                                                                    #if length of current is greater than 0
                names.append(current)                                                               #add current to names
                current = ''                                                                        #set current to ''
        else:                                                                                       #else
            current += char                                                                         #add char to current
    if len(current) > 0:                                                                            #if the length of curent is greater than 0
        names.append(current)                                                                       #add current to names
    return names                                                                                    #return names

def remove_title(name):                                                                             #create function
    parts = split_name(name)                                                                        #set parts to result of function split_name
    if parts[0] in titles:                                                                          #if parts at index 0 is present in titles
        del parts[0]                                                                                #remove parts at index 0 from parts
    new_name = ' '.join(parts)                                                                      #join parts with a space between elements and set to new_name
    return new_name                                                                                 #return new_name

def reverse_and_display(name):                                                                      #create function
    reversed_string = name[::-1]                                                                    #set variable reserved_string to last element of list name
    return reversed_string                                                                          #return reversed_string

def vowel_count(name):                                                                              #create function
    vc = 0                                                                                          #set vc equal to 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']                                     #create list
    for letter in name:                                                                             #create for loop
        if letter in vowels:                                                                        #if letter is present in vowel list
            vc +=1                                                                                  #add 1 to vc
    return vc                                                                                       #return vc

def consonant_frequency(name):                                                                      #create function
    cc = 0                                                                                          #set cc equal to 0
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']                                     #create list
    for letter in name:                                                                             #create for loop
        if letter not in vowels:                                                                    #if letter is not present in vowel list
            cc +=1                                                                                  #add 1 to cc
    return cc                                                                                       #return cc

def return_first_name(name):                                                                        #create function
    space = 0                                                                                       #set space equal to 0
    output = ''                                                                                     #set output to ''
    for char in name:                                                                               #create for loop
        if char == ' ':                                                                             #if the character is ' '
           space +=1                                                                                #add 1 to space
    if space < 1:                                                                                   #if space is less than 1
        output = name                                                                               #set output to name
    new_name = remove_title(name)                                                                   #set new_name to result of function remove_title
    for letter in new_name:                                                                         #create for loop
        if letter == ' ':                                                                           #if character is ' '
            break                                                                                   #end for loop
        else:                                                                                       #else
            output = output + letter                                                                #output is equal to current output plus character
    return output                                                                                   #return output

def return_last_name(name):                                                                         #create function
    space = 0                                                                                       #set space equal to 0
    output = ''                                                                                     #set output to ''
    for char in name:                                                                               #create for loop
        if char == ' ':                                                                             #if character is ' '
           space +=1                                                                                #add 1 to space
    if space < 1:                                                                                   #if space is less than 1
        output ='NO LAST NAME'                                                                      #set output to 'NO LAST NAME'
    else:                                                                                           #else
        for i in range(len(name)-1, -1, -1):                                                        #create for loop
            if name[i] == ' ':                                                                      #get last found space
                break                                                                               #end for loop
            else:                                                                                   #else
                output = output + name[i]                                                           #output is equal to current output plus character
        output = reverse_and_display(output)                                                        #set output equal to the reverse_and_display of currnet output
    return output                                                                                   #return output

def return_middle_name(name):                                                                       #create function
    space = 0                                                                                       #set space equal to 0
    for char in name:                                                                               #create for loop
        if char == ' ':                                                                             #if character is ' '
           space +=1                                                                                #add 1 to space
    if space <= 1:                                                                                  #if space is less than or equal to 1
        middle = 'NO MIDDLE NAME'                                                                   #set middle to 'NO MIDDLE NAME'
    else:                                                                                           #else
        new_name = remove_title(name)                                                               #set new_name to result of function remove_title
        beg = 0                                                                                     #set beg equal to 0
        end = len(new_name)-1                                                                       #set end equal to length of namee minus 1
        for i in range(0, len(new_name)):                                                           #create for loop
            if new_name[i] == ' ':                                                                  #get first found space
                beg +=1                                                                             #add 1 to beg
                break                                                                               #end for loop
            else:                                                                                   #else
                beg +=1                                                                             #add 1 to beg
        for i in range(len(new_name)-1, -1, -1):                                                    #create for loop
            if new_name[i] == ' ':                                                                  #get last found space
                break                                                                               #end for loop
            else:                                                                                   #else
                end-=1                                                                              #subtract 1 from end
        middle = new_name[beg:end]                                                                  #set middle equal to name from first space to last space
    return middle                                                                                   #return middle

def check_hyphen(name):                                                                             #create function
    if '-' in name:                                                                                 #if hyphen is present in name
        return True                                                                                 #return boolean True
    else:                                                                                           #else
        return False                                                                                #return boolean False

def get_initials(name):                                                                             #create function
    new_name = remove_title(name)                                                                   #set new_name to output of function remove_title
    first = return_first_name(new_name)                                                             #set first to output of a function
    middle = return_middle_name(new_name)                                                           #set middle to output of a function
    last = return_last_name(new_name)                                                               #set last to output of a function
    first_initial = str(first[0])                                                                   #set first_initial to first at index 0
    last_initial = str(last[0])                                                                     #set last_initial to last at index 0
    if middle == 'NO MIDDLE NAME':                                                                  #if variable middle is equal to 'NO MIDDLE NAME'
        initials = first_initial + last_initial                                                     #set initials to first_initial plus last_initial
    else:                                                                                           #else
        midname = split_name(middle)                                                                #split middle with function and set to midname
        mid_initials = ''                                                                           #set mid_initials to ''
        for i in midname:                                                                           #create for loop
            mid_initials = mid_initials + (i[0])                                                    #set mid_initials to mid_initials plus i at index 0
        initials = first_initial + mid_initials + last_initial                                      #set initials to first_initials plus mid_initials plus last_initial
    initials = convert_to_uppercase(initials)                                                       #convert initials to all uppercase
    return initials                                                                                 #return initials
   
def convert_to_lowercase(name):                                                                     #create function
    output = ''                                                                                     #set output to ''
    for char in name:                                                                               #create for loop
        int_value = ord(char)                                                                       #set int_value to ordinal value of character
        if int_value < 91 and int_value > 64 :                                                      #if int_value is less than 91 and int_value is greater than 65
            int_value = int_value + 32                                                              #set int_value to current int_value plus 32
            char2 = chr(int_value)                                                                  #set char2 to character of int_value
            output = output + char2                                                                 #set output to current output plus char2
        else:                                                                                       #else
            output = output + char                                                                  #set output to currenct output plus char
    return output                                                                                   #return output

def convert_to_uppercase(name):                                                                     #create function
    output = ''                                                                                     #set output to ''
    for char in name:                                                                               #create for loop
        int_value = ord(char)                                                                       #set int_value to ordinal value of character
        if int_value > 91 and int_value < 123:                                                      #if int_value is greater than 91 and int_value is less than 123
            int_value = int_value - 32                                                              #set int_value to current int_value minus 32
            char2 = chr(int_value)                                                                  #set char2 to character of int_value
            output = output + char2                                                                 #set output to current output plus char2
        else:                                                                                       #else
            output = output + char                                                                  #set output to currenct output plus char
    return output                                                                                   #return output

def mix_up_name(name):                                                                              #create function
    output = ''                                                                                     #set output to ''
    n = list(name)                                                                                  #set variable n to list of name
    while len(n) > 0:                                                                               #while length of n is less than 0
        r = random.randint(0, len(n)-1)                                                             #set variable r to random integer between 0 and 1 less than length of n
        output = output + n[r]                                                                      #set output to current output plus n at index r
        del n[r]                                                                                    #remove n at index r from list n
    return output                                                                                   #return output

def check_palindrome(name):                                                                         #create function
    new_name = remove_title(name)                                                                   #set new_name to result of function remove_title
    lower_name = convert_to_lowercase(new_name)                                                     #set variable lower_name to result of function convert_to_lowercase
    rev_name = reverse_and_display(lower_name)                                                      #set variable rev_name to result of function reverse_and_display with lower_name as a parameter
    if rev_name == lower_name:                                                                      #if variable rev_name is equal to variable lower_name
        return True                                                                                 #return boolean True
    else:                                                                                           #else
        return False                                                                                #return boolean False

def main():                                                                                         #create function
    while True:                                                                                     #create while True loop
        time.sleep(3)                                                                               #wait 3 seconds before continuing
        os.system('cls')                                                                            #clear screen
        option = input('What would you like to do? \n 1. Reverse and Display your name \n 2. count the vowels in your name \n 3. count the number of consonants in your name \n 4. display your first name \n 5. display your last name \n 6. display your middle name \n 7. return boolean if name contains a hyphen \n 8. convert name to all lowercase \n 9. convert name to all uppercase \n 10. scramble the letters of your name \n 11. check if your first name is a palindrome \n 12. display your initials \n (Respond with the corresponding number or stop): ') #set option to user response
        if option == '1':                                                                           #if option is equal to 1
            print(reverse_and_display(name))                                                        #call function and print output
        elif option == '2':                                                                         #if option is equal to 2
            print(vowel_count(name))                                                                #call function and print output
        elif option == '3':                                                                         #if option is equal to 3
            print(consonant_frequency(name))                                                        #call function and print output
        elif option == '4':                                                                         #if option is equal to 4
            print(return_first_name(name))                                                          #call function and print output
        elif option == '5':                                                                         #if option is equal to 5
            print(return_last_name(name))                                                           #call function and print output
        elif option == '6':                                                                         #if option is equal to 6
            print(return_middle_name(name))                                                         #call function and print output
        elif option == '7':                                                                         #if option is equal to 7
            print(check_hyphen(name))                                                               #call function and print output
        elif option == '8':                                                                         #if option is equal to 8
            print(convert_to_lowercase(name))                                                       #call function and print output
        elif option == '9':                                                                         #if option is equal to 9
            print(convert_to_uppercase(name))                                                       #call function and print output
        elif option == '10':                                                                        #if option is equal to 10
            print(mix_up_name(name))                                                                #call function and print output
        elif option == '11':                                                                        #if option is equal to 11
            print(check_palindrome(name))                                                           #call function and print output
        elif option == '12':                                                                        #if option is equal to 12
            print(get_initials(name))                                                               #call function and print output
        elif option == 'stop':                                                                      #if option is equal to stop
            break                                                                                   #end loop
        else:                                                                                       #else
            print('INVALID RESPONSE!!')                                                             #display message


main()                                                                                              #call function