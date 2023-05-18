# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution. 

# Student ID: w1902039
 
# Date: 04/17/2022 

def Vertical_Histogram():

    def numberNumeric(number):

        #to check whether the input is an integer
        if not number.isnumeric():
        
            print("Integer required")

            return True

        #to check whether the inputs are within the given range
        elif int(number) not in range(0,121,20):        

            print("Out of range.")

            return True
    
        else:

            #to save the input in the memory if the inputs are correct
            return int(number)

    #made this list to gather all the outcomes    
    outputs = []

    def data_inputs():

        #used dictionary to assign inputs for each topic easily
        marks = {"pass": "",
             "defer": "",
             "fail": ""
            }
    
        total = 0

        #for loop for call each topic(pass,defer,fail) separately
        for mark in marks:

            #if this is false then the program won't ask inputs again if it's wrong
            while marks[mark] == "":
            
                status = numberNumeric(input("Please enter your credits at " + mark + ": "))

                #this will return the correct value
                if status != True:

                    #assign value for each key values (pass,defer,fail)
                    marks[mark] = status
                
                    total += status
                
        if total != 120:

            print("Total incorrect.")

            #called the function again to ask inputs again if total is wrong
            data_inputs()

            #used to prevent printing two outputs. with this, the funtion will terminated rather than going forward
            return
    
        if int(marks["pass"]) == 120:
        
            print("Progress")

            outputs.append("Progress")

        elif int(marks["pass"]) == 100 and (int(marks["defer"]) == 20 or int(marks["fail"]) == 20):

            print("Progress (module trailer)")

            outputs.append("Trailer")

        elif int(marks["pass"]) in range(0,81,20) and int(marks["defer"]) in range(0,121,20) and int(marks["fail"]) in range(0,61,20):

            print("Module retriever")

            outputs.append("Retriever")

        elif int(marks["fail"]) in range(80,121,20):

            print("Exclude")

            outputs.append("Exclude") 

    #reference: https://linuxhint.com/counter-module-python/  (didn't know how to count specific values from a dictionary)
    from collections import Counter

    #outcomes = 1 here because collected inputs once so that when getting inputs again it can count from 2 
    outcomes = 1
  
    print("Staff Version with Histogram")

    #to get data
    data_inputs()

    again = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()

    #used while loop to excecution of the program to input data again or the termination if don't need to get data again
    while again == "y":

        outcomes += 1

        data_inputs()
    
        again = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()

    if again == "q":

        print("---------------------------------------------------------------")

        print("Horizontal Histogram ")

        print("Progress ","Trailer ","Retriever ","Exclude")

        #this is making a list of the count of each progression outcomes 
        outcome_val = [Counter(outputs)["Progress"],Counter(outputs)["Trailer"],Counter(outputs)["Retriever"],Counter(outputs)["Exclude"]]

        maxval = max(outcome_val)
    
        #For the output of Horizontal Histogram part
        for i in range (maxval):

            if Counter(outputs)["Progress"]>i:

                print("   *      ", end='')

            else:

                print(len("Progress  ")*" ",end='')

            if Counter(outputs)["Trailer"]>i:

                print("   *     ", end='')

            else:

                print(len("Trailer  ")*" ",end='')

            if Counter(outputs)["Retriever"]>i:

                print("    *      ", end='')

            else:

                print(len("Retriever  ")*" ",end='')

            if Counter(outputs)["Exclude"]>i:

                print("   *")

            else:

                print(len("Exclude  ")*" ")

        print(outcomes, "outcomes in total.")

        print("----------------------------------------------------------------")

