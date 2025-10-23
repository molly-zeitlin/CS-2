#Author: Molly Zeitlin
#Description: determines the cost of the shipment of a package
#Date: 10/22/2025
#Bugs: must have 5 inputs separated by a comma, accounts for letters and special characters
#Log: 1.0 MZ

def get_size(l, w, t):                                                                                      #create function
    if 4.25 >= l >= 3.5 and 6 >= w >= 3.5 and .016 >= t >= .007:                                            #if variables match the specified parameters
        return "Regular Post Card"                                                                          #return Regular Post Card
    elif 6 >= l >= 4.25 and 11.5 >= w >= 6 and 0.15 >= t >= .007:                                           #if variables match the specified parameters
        return "Large Post Card"                                                                            #return Large Post Card
    elif 6.125 >= l >= 3.5 and 11.5 >= w >= 5 and .25 >= t >= .016:                                         #if variables match the specified parameters
        return "Regular Envelope"                                                                           #return Regular Envelope
    elif 24 >= l >= 6.125 and 18 >= w >= 11 and .5 >= t >= .25:                                             #if variables match the specified parameters
        return "Large Envelope"                                                                             #return Large Envelope
    elif l > 24 or w > 18 or t > .5:                                                                        #if variables match the specified parameters
        if l + 2*(w+t) <= 84:                                                                               #if variables match the specified parameters
            return "Regular Package"                                                                        #reutrn Regular Package
        elif 130 >= l + 2*(w+t) > 84:                                                                       #if variables match the specified parameters
            return "Large Package"                                                                          #return Large Package
        else:                                                                                               #else
            return "UNMAILABLE"                                                                             #return UNMAILABLE
    else:                                                                                                   #else
        return "UNMAILABLE"                                                                                 #return UNMAILABLE

def get_zip(zip):                                                                                           #create function
    if zip >= 1 and zip <= 6999:                                                                            #if variable match the specified parameters
        output = 1                                                                                          #set output to 1
    elif zip >= 7000 and zip <= 19999:                                                                      #if variable match the specified parameters
        output = 2                                                                                          #set output to 2
    elif zip >= 20000 and zip <= 25999:                                                                     #if variable match the specified parameters
        output = 3                                                                                          #set output to 3
    elif zip >= 26000 and zip <= 62999:                                                                     #if variable match the specified parameters
        output = 4                                                                                          #set output to 4
    elif zip >= 63000 and zip <= 84999:                                                                     #if variable match the specified parameters
        output = 5                                                                                          #set output to 5
    elif zip >= 85000 and zip <= 99999:                                                                     #if variable match the specified parameters
        output = 6                                                                                          #set output to 6
    else:                                                                                                   #else
        output  = "INVALID RESPONSE"                                                                        #set output to INVALID RESPONSE
    return output                                                                                           #return output

def get_cost(mail_type, distance):                                                                          #create function
    if mail_type == "Regular Post Card":                                                                    #if variable is "Regular Post Card"
        total_cost = .2 + distance*.03                                                                      #set total_cost to .2 plus (.03 multiplied by the distance)
    elif mail_type == "Large Post Card":                                                                    #if variable is "Large Post Card"
        total_cost = .37 + distance*.03                                                                     #set total_cost to .37 plus (.03 multiplied by the distance)
    elif mail_type == "Regular Envelope":                                                                   #if variable is "Regular Envelope
        total_cost = .37 + distance*.04                                                                     #set total_cost to .37 plus (.04 multiplied by the distance)
    elif mail_type == "Large Envelope":                                                                     #if variable is "Large Envelope
        total_cost = .6 + distance*.05                                                                      #set total_cost to .6 plus (.05 multiplied by the distance)
    elif mail_type == "Regular Package":                                                                    #if variable is "Regular Package
        total_cost = 2.95 + distance*.25                                                                    #set total_cost to 2.95 plus (.25 multiplied by the distance)
    elif mail_type == "Large Package":                                                                      #if variable is "Large Package
        total_cost = 3.95 + distance*.35                                                                    #set total_cost to 3.95 plus (.35 multiplied by the distance)
    else:                                                                                                   #else
        total_cost = "UNMAILABLE"                                                                           #set total_cost to "UNMAILABLE"
    return total_cost                                                                                       #return total_cost

def main():                                                                                                 #create function
    counter = 0                                                                                             #set variable to 0
    while counter < 5:                                                                                      #while variable coutner is less than 5
        data = input("Enter mail length, width, thickness, zipcode of origin, zipcode of destination: ")    #set data to user input
        data = data.split(",")                                                                              #set data to data split where a "," is present
        l = float(data[0])                                                                                  #set l to float of data at index 0
        w = float(data[1])                                                                                  #set w to float of data at index 1
        t = float(data[2])                                                                                  #set t to float of data at index 2
        zip1 = int(data[3])                                                                                 #set zip1 to integer of data at index 3
        zip2 = int(data[4])                                                                                 #set zip2 to integer of data at index 4
        mail_type = get_size(l, w, t)                                                                       #call function and set output to data
        origin = get_zip(zip1)                                                                              #call function and set output to origin
        destination = get_zip(zip2)                                                                         #call function and set output to destination
        distance = abs(origin - destination)                                                                #set distance to absolute value of variable origin minus variable destination                                                                                    #DELETE THIS - only here for debugging
        total_cost = get_cost(mail_type, distance)                                                          #call function and set output to total_cost
        if total_cost == "UNMAILABLE":                                                                      #if total_cost is "UNMAILABLE"
            print("UNMAILABLE")                                                                             #display message
        else:                                                                                               #else
            print(f"{total_cost:.2f}".lstrip("0"))                                                          #display total_cost, including the two values to the right of the decimal, and no leading zero
        counter +=1                                                                                         #add 1 to counter

main()                                                                                                      #call function