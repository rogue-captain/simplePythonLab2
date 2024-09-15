# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:49:16 2024

@author: Sully
"""

# -*- coding: utf-8 -*
##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab #2

# Due Date: 09/17/2024
#
# Program Description:  
#
# Inputs: 3 variables: name, num_Input[0,2](Array)
#
# Outputs: console calculates and prints users 3 number inputs, min, max, 
#average, range and letter grade based on inputs from user. 
#
##############################################################################

################################ VARIABLES ####################################
name = input("enter your name please ") #collects string for user name

#array variable to collect and store 3 number grade inputs as string then we convert to integer, 
#first there is a message to enter 3 number grades, 
#[Int] specifies data type of array,.split() function uses space as delimiter to differentiate the 3 numbers
#"[int(num) for num in" this code snippet is a list comprehension that loops through elements in array and 
#converts the string elements into integers

while True: #while loop to ensure checks are run and user re-prompted

    num_Input = [int(num) for num in input
                 ("please enter 3 number grades (0-100) seperated by spaces ").split()] 
    
    #this is a if else check to verify user has inputted exactly 3 numbers
    if len(num_Input) != 3:
        print("ERROR: enter EXACTLY 3 number grades ranging from 0-100 and seperated by a space")
        
    elif not all(0 <= num <= 100 for num in num_Input):
        print("ERROR: Enter grades ranging from 0-100 only.")
        
    else:
                
            print("you entered: ", num_Input)
            
            gradeSum = sum(num_Input) # sum using array and sum function
            
            gradeAverage = (sum(num_Input)/len(num_Input))
            
            gradeMaximum = num_Input[0]
            
            gradeMinimum = num_Input[0]
            
            gradeRange = max(num_Input) - min(num_Input)
            
            for num in num_Input:
                
                if num > gradeMaximum:
                    gradeMaximum = num
                    
                if num < gradeMinimum:
                        gradeMinimum = num
                        
            
            
            ############################ END VARIABLES ####################################
            
            print(name, ", Your grade sum = ", gradeSum,
                  ", grade average = ", gradeAverage, 
                  ", grade range = ", gradeRange)
            
                
            # Output the results
            print("Maximum grade number is:", gradeMaximum)
            
            print("Minimum grade number is:", gradeMinimum)
            
            # Determine and print the letter grade based on the average
            if gradeAverage >= 90:
                print("Your grade is A")
                
            elif gradeAverage >= 80:
                print("Your grade is B")
                
            elif gradeAverage >= 70:
                print("Your grade is C")
                
            elif gradeAverage >= 60:
                print("Your grade is D")
                
            else:
                print("Your grade is F, you have FAILED")
            
            break




