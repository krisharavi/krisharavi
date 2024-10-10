# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
    #histogram : Graphics Reference (graphics.py v5). (n.d.). Available at: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf.
    #color code: www.w3schools.com. (n.d.). Colors - X11. [online] Available at: https://www.w3schools.com/colors/colors_x11.asp.
    #read file: GeeksforGeeks. (2019). How to read from a file in Python. [online] Available at: https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/.

# Student ID: w2052723/ 20220849

# Date: 13.12.2023

#includes part1_c and part2 and part3

#import graphics module
from graphics import *

#creating function to export the process to part 1 file
def staff_process():
    #declare variables
    recordfile = True
    #user input marks variable
    pass_m =0
    defer_m =0
    fail_m =0
    total_marks= 0
    student_count = 0

    #list to check range of & input marks store marks
    mark_range = [0,20,40,60,80,100,120]
    marks = []

    #Progress outcomes count & lists
    progress_count = 0
    progress = []

    trailer_count = 0
    trailer = []

    exclude_count = 0
    exclude = []

    retriever_count = 0
    retriever = []

    #user's desire to continue the loop and exit
    desire_choice = ''
    choice = ['y', 'q']

    #Histogram rectangle coordinates variables
    height1 = 0
    height2 = 0
    height3 = 0
    height4 = 0


    def checkMarks(prompt):
        '''
        This function helps to identify whether the entered marks is in range.
        if not it displays "out of range" else if type of the variable differs from
        integer it prints "Integer required"
        '''
        while(True):
            try:
                userInput = int(input(prompt))
                while userInput not in mark_range:
                    print("Out of range")
                    print()
                    userInput = int(input(prompt))
                break

            except ValueError:
                print("Integer required")
                print()

        return userInput

    def marksWriting(outcome_list,Message):
        '''
        Two arguments are used to print the list and to write in the text file
        of the marks and the progression outcome.
        '''
        for mark_value in outcome_list:
            '''List printing command'''
            print(Message, end=' ')
            print(mark_value[0],",",mark_value[1],",",mark_value[2])

            '''Text file write '''
            fo.write(Message)
            fo.write(str(mark_value[0]))
            fo.write(", ")
            fo.write(str(mark_value[1]))
            fo.write(", ")
            fo.write(str(mark_value[2]))
            fo.write("\n")
        
        

    def rectangle(rectangle_name,color):
        '''
        Two arguments are used to get the bar name of the relevant outcome and the
        fill in color of the bar in the histogram
        '''
        rectangle_name.setOutline("Light Slate Gray")
        rectangle_name.setFill(color)
        rectangle_name.draw(win)

    def histogram_text(text,font_size,text_color):
        '''
        Three arguments are used to print the relevant text in histogram
        (progression outcome, title, relevant count) and it's relevant font size
        and the text color
        '''
        text.setFace('helvetica')
        text.setSize(font_size)
        text.setStyle("bold")
        text.setTextColor(text_color)
        text.draw(win)    


    while recordfile == True:
        # Gets the pass, defer and fail marks from the user. 
        pass_m = checkMarks("Please enter your credits at pass: ")
        defer_m = checkMarks("Please enter your credit at defer: ")
        fail_m = checkMarks("Please enter your credit at fail: ")        

        total_marks = pass_m + defer_m + fail_m
        
        if total_marks != 120:       #checks whether the total of all three marks is above 120.
            print("Total incorrect")
            print()
            continue
        
        #if the total_marks == 120 then,
        else:
            marks = [pass_m , defer_m , fail_m]    #The input taken from the user is assigned to marks list. 
            student_count += 1                     #Total of the student count gets increased.

                
        #The conditions to check if the student's progression outcome is (Progress/ Progress(Module Trailer)/ Exclude/ Module Retriever) 
        if pass_m == 120:
            print("Progress")
            print()
            progress_count += 1
            progress.append(marks)
     
        elif pass_m == 100: 
            print("Progress(Module trailer)")
            print()
            trailer_count += 1
            trailer.append(marks)
        
        elif fail_m >= 80: 
            print("Exclude")
            print()
            exclude_count += 1
            exclude.append(marks)
     
        elif pass_m <= 80 and fail_m < 80: 
            print("Module retriever")
            print()
            retriever_count += 1
            retriever.append(marks)

        #Get to choose if the user wish to input more entries else to quit and display the histogram
        print("Would you like to enter another set of data?")
        desire_choice = input("Enter 'y' for yes or 'q' to quit and view results: ")
        desire_choice = desire_choice.lower()

        while desire_choice not in choice:
            print("Invalid input")
            desire_choice = input("Enter 'y' for yes or 'q' to quit and view results: ")
            desire_choice = desire_choice.lower()

        if desire_choice == 'y':  #User can enter more entries
            print()
            continue
        if desire_choice == 'q':  #User can quit the program and helps to display Histogram, List of Progress Outcome and Text file
            recordfile = False
            break
        break

    while recordfile == False: #Histogram display condition
        
        base = 10  #No.of pixels in one block of a bar
        
        height1 = 300 -(base * progress_count)
        height2 = 300 -(base * trailer_count)
        height3 = 300 -(base * retriever_count)
        height4 = 300 -(base * exclude_count)
        
        win = GraphWin("Histogram", 600, 500)  #Creating histogram window
        win.setBackground("honeydew1")
        
        title = Text(Point(120,50),"Histogram Results")
        histogram_text(title, 14, "black")
           
        #rectangle bars of histogram
        rectangle1 = Rectangle(Point(50,300), Point(120,height1))  #progress_bar
        rectangle(rectangle1,"palegreen")
        
        rectangle2 = Rectangle(Point(130,300), Point(200,height2)) #progress(Module Trailer)_bar
        rectangle(rectangle2,"palegreen3")

        rectangle3 = Rectangle(Point(210,300), Point(280,height3)) #module_retriever_bar
        rectangle(rectangle3,"yellowgreen")

        rectangle4 = Rectangle(Point(290,300), Point(360,height4)) #exclude_bar
        rectangle(rectangle4,"rosybrown2")
            
        aline = Line(Point(20,300), Point(400,300)) # x-axis of the histogram
        aline.setFill("Light Slate Gray")
        aline.draw(win)

        #top text - student count text of progression outcomes
        position_1 = Text(Point(85,(height1 - base)),f"{progress_count}")
        histogram_text(position_1, 12, "Light Slate Gray")

        position_2 = Text(Point(165,(height2 - base)),f"{trailer_count}")
        histogram_text(position_2, 12, "Light Slate Gray")

        position_3 = Text(Point(245,(height3 - base)),f"{retriever_count}")
        histogram_text(position_3, 12, "Light Slate Gray")

        position_4 = Text(Point(325,(height4 - base)),f"{exclude_count}")
        histogram_text(position_4, 12, "Light Slate Gray")

        #bottom text - description of progression outcome
        progress_text = Text(Point(85,310),"Progress")
        histogram_text(progress_text, 10, "Light Slate Gray")

        trailer_text = Text(Point(165,310),"Trailer")
        histogram_text(trailer_text, 10, "Light Slate Gray")

        retriever_text = Text(Point(245,310),"Retriever")
        histogram_text(retriever_text, 10, "Light Slate Gray")

        excluded_text = Text(Point(325,310),"Exclude")
        histogram_text(excluded_text, 10, "Light Slate Gray")

        total_count = Text(Point(120,335),f"{student_count} outcomes in total.")
        histogram_text(total_count, 11, "Light Slate Gray")
        
        #close the histogram window
        try:
            win.getMouse()
            win.close()
        except:
            win.close()
        break

    #Part - 2 (nested list print) & write in the text file
     
    print("\n")
    print("-"*60)
    print("Part - 2: Printing progress outcome from nested lists.")
    print()    
    with open("20220849.txt", "w") as fo:
        marksWriting(progress,"Progress - ")
        marksWriting(trailer,"Progress (Module Trailer) - ")
        marksWriting(retriever,"Module Retriever - ")
        marksWriting(exclude,"Excluded - ")

    #Part - 3 (read the text file)
    print("\n")
    print("-"*60)
    print("Part -3: Printed progress outcome from text file")
    print()
    with open("20220849.txt","r") as fo:
        print(fo.read())
                

