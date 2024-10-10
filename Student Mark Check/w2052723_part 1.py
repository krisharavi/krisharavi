# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
    
# Student ID: w2052723/ 20220849

# Date: 10.12.2023

#Includes part 1 student progress and menu selection

#import part 2 file for staff progress
from w2052723_part1C_3 import staff_process

#declare variables
position = ['student','staff']
selection = [1,2,3]
mark_range = [0,20,40,60,80,100,120]
role = 0
menu = True

#defining function to print instructions to enter position and end the loop
def start_design():
    print("*"*20, "Welcome to Progression Outcome check", "*"*20)
    print()
    print("Enter 1 - Visit the Student Site\
    \nEnter 2 - Visit the Staff Site\
    \nEnter 3 - End the Site")
    print()

#checks the user beginning start input is valid (1/2) or not  
def fail_begin(message):
    while(True):
        try:
            start = int(input(message))
            while start not in selection:
                print("Invalid input...Enter 1 / 2 / 3")
                print()
                start = int(input(message))
            break

        except ValueError:
            print("Invalid input...Enter 1 / 2 / 3")
            print()
    
    return start

#checks the student input marks 
def checking_marks(message):
    '''
    This function helps to identify whether the entered marks is in range.
    if not it displays "out of range" else if type of the variable differs from
    integer it prints "Integer required"
    '''
    while(True):
        try:
            userInput = int(input(message))
            while userInput not in mark_range:
                print("Out of range")
                print()
                userInput = int(input(message))
            break

        except ValueError:
            print("Integer required")
            print()

    return userInput

#function that inputs users credits
def input_marks():
    
    global pass_marks, defer_marks, fail_marks, total
    
    pass_marks = checking_marks("Please enter your credits at pass: ")
    defer_marks = checking_marks("Please enter your credit at defer: ")
    fail_marks = checking_marks("Please enter your credit at fail: ")
    
    total = pass_marks + defer_marks + fail_marks

#Start of the menu
while menu == True:

    #menu start commands
    start_design()
    role = fail_begin("Enter 1/2/3 to enter your position(1-student, 2-staff, 3-end_site) : ")
    
    #checks Process of the user as a student 
    if role == 1:            
        print()
        print("-"*25, position[0],"page", "-"*25)
        print()
        
        # Gets the pass, defer and fail marks from the user.
        input_marks()

        #checks whether the total of all three marks is above 120.
        if total != 120:       
            print("Total incorrect")
            print()
            input_marks()

        print()
        #prints the relevant progress outcome for the students
        if total == 120:
            if pass_marks == 120:
                print("Your Progression outcome is: Progress")
                print()
         
            elif pass_marks == 100: 
                print("Your Progression outcome is: Progress(Module trailer)")
                print()
            
            elif fail_marks >= 80: 
                print("Your Progression outcome is: Exclude")
                print()
        
            elif pass_marks <= 80 and fail_marks < 80: 
                print("Your Progression outcome is: Module retriever")
                print()
            print()
            
    #Process of the user as a staff            
    elif role == 2:
        print()
        print("-"*25, position[1],"page", "-"*25)
        print()
        
        # imports the functions from the part 2 file and get inputs and prints relevant outputs for staff
        print()
        staff_process()
        print()

    #Process if the user wishes to end the site
    elif role == 3:
        menu = False
        print()
        print("...Site...Ended...")
        break           
            
