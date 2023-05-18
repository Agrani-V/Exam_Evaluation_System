# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 

# Any code taken from other sources is referenced within my code solution. 

# Student ID: w1902039
 
# Date: 04/17/2022

from part01 import individual_student_data, validation, Multiple_Outcomes_Histogram

from part02 import Vertical_Histogram

from part03 import access_data_through_list

from part04 import text_version

print("Enter 1 for progression outcome for an individual student in Main Version \nEnter 2 for Main Version ( Validation )\nEnter 3 for Multiple Outcomes & Histogram in Main Version \nEnter 4 for Vertical Histogram (extension) \nEnter 5 for List/Tuple/Directory (extension) \nEnter 6 for Text File - Part 4 \n")

menu_no = int(input("Your preference: "))

if menu_no == 1:

    individual_student_data()

elif menu_no == 2:

    validation()

elif menu_no == 3:

    Multiple_Outcomes_Histogram()

elif menu_no == 4:

    Vertical_Histogram()

elif menu_no == 5:

    access_data_through_list()

elif menu_no == 6:

    text_version()
