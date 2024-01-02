#Math Flash Cards Game
#Name: Nikhil Doal, id - 876021
#Description: This program is a math flash card game created using the Tkinter
#             library in Python. It helps users practice basic arithmetic
#             operations such as addition, subtraction, multiplication, 
#             division, and remainder. The game consists of four levels, each 
#             with a different range of numbers, getting more difficult.
#             There are 5 pages in the game: the start screen, the level
#             selection screen, the level screen, a settings screen and a
#             question log

#             The main features of the program include:
#                - Level selection screen allowing users to choose their desired
#                  difficulty level
#                - Progress tracking with correct, incorrect, and total number
#                  of answers
#                - Previous question and user answer display for reference
#                - Log to record and view previous questions and user answers
#                - Reset functionality to start a level from scratch
#                - Settings screen to customize the operators and option to
#                  include negative numbers
#                - A progress bar and text with percentage of total correct
#                  answers
#                - Valid input checking to ensure the user enters a valid answer
#                - Ability to submit answers using the Enter key

#             The program utilizes various Tkinter components, including labels,
#             buttons, frames, and images for the user interface. It also makes
#             use of random number generation to generate questions based on the
#             selected level and operator preferences.

#             To play the game, the user selects a level, answers the displayed
#             math questions by entering the answer in the input box, and
#             submits the answer. The program provides immediate feedback on the
#             correctness of the answer and updates the progress bar
#             accordingly. The user can also view the question log to review
#             their previous answers and track their progress.

#             Topics that have been used outside of the provided booklet like:
#             .tkraise() and .place() have been explained in the attached
#             document 
#import statements
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import ttk
from tkinter import*
from random import*

#----------------------------------Functions------------------------------------
#This function raises the level frame and changes the level_num to 1. It then
#generates the first question and resets the level to prevent switching to a
#different level with the same progress
def show_level1():
    global level_num
    level_frame.tkraise()
    level_name.configure(text="Level: 1")
    level_num = 1
    generate_question()
    reset_level()

#This function raises the level frame and changes the level_num to 2. It then
#generates the first question and resets the level to prevent switching to a
#different level with the same progress
def show_level2():
    global level_num
    level_frame.tkraise()
    level_name.configure(text="Level: 2")
    level_num = 2
    generate_question()
    reset_level()

#This function raises the level frame and changes the level_num to 3. It then
#generates the first question and resets the level to prevent switching to a
#different level with the same progress
def show_level3():
    global level_num
    level_frame.tkraise()
    level_name.configure(text="Level: 3")
    level_num = 3
    generate_question()
    reset_level()

#This function raises the level frame and changes the level_num to 4. It then
#generates the first question and resets the level to prevent switching to a
#different level with the same progress
def show_level4():
    global level_num
    level_frame.tkraise()
    level_name.configure(text="Level: 4")
    level_num = 4
    generate_question()
    reset_level()

#This function raises the level select frame
def show_menu():
    level_select_frame.tkraise()

#This function raises the start screen frame
def show_start_screen():
    start_screen.tkraise()

def show_settings():
    settings_frame.tkraise()
    
#This function raises the question log frame
def show_question_log():
    question_log_screen.tkraise()

#This function raises the level frame without performing any other functions
def show_level():
    level_frame.tkraise()

#The generate_question function is responsible for generating a question. Using
#the random module it generates two numbers and an operator depending on the
#checkboxes. If the question involves division, it is first rearranged into
#multiplication, and the bigger number is taken as the first number to prevent
#decimals. This function also records the previous answer and user answer and
#records them to the question log
def generate_question():
    global user_ans
    global ans
    global counter_total
    global statement
    
    #Choosing the minimum question range
    if (negative_numbers_state.get() == True):
        if level_num == 1 or level_num == 0:
            question_range_min = -3
        elif level_num == 2:
            question_range_min = -6
        elif level_num == 3:
            question_range_min = -9
        elif level_num == 4:
            question_range_min = -12
        else:
            question_range_min = 0
    else:
        question_range_min = 1
    #Choosing the maximum question range
    if level_num == 1 or level_num == 0:
        question_range_max = 3
    elif level_num == 2:
        question_range_max = 6
    elif level_num == 3:
        question_range_max = 9
    elif level_num == 4:
        question_range_max = 12
    else:
        question_range_max = 0

    #generating a random number between the 2 ranges
    num1 = randint(question_range_min, question_range_max)
    num2 = randint(question_range_min, question_range_max)
    
    #choosing which operators to choose from depending on the checkboxes on 
    #the settings page
    possible_operators=[]
    if (multiplication_state.get() == True):
        possible_operators.append("x")
    if (division_state.get() == True):
        possible_operators.append("/")
    if (addition_state.get() == True):
        possible_operators.append("+")
    if (subtraction_state.get() == True):
        possible_operators.append("-")
    if (remainder_state.get() == True):
        possible_operators.append("%")
    
    #choosing an operator
    #if no operator is chosen, giving an error box and turning on the default
    #operators
    operator = ""
    if possible_operators == []:
        messagebox.showerror("ERROR", "Please choose an operator")
        settings_frame.tkraise()
        multiplication_state.set(True)
        addition_state.set(True)
        subtraction_state.set(True)
        division_state.set(True)
    else:
        operator = choice(possible_operators)

    #Recording the previous question and user answer
    if counter_total == 0:
        previous_question.configure(text="Previous Question: ")
        previous_user_answer.configure(text="Your Answer: ")
    else:
        previous = "Previous Question: " + statement + str(ans)
        previous_question.configure(text=previous)
        previous_log = "Question: " + statement + str(ans) +"\n"
        log.configure(state="normal") #turning log editing on
        log.insert(INSERT, previous_log)
        user_answer = "Your Answer: " + statement + str(user_ans)
        previous_user_answer.configure(text=user_answer)
        user_answer_log = "Your Answer: " + statement + str(user_ans) + "\n\n"
        log.insert(INSERT, user_answer_log)
        log.configure(state="disabled") #turning log editing off 

    #choosing the operator and calculating the answer
    if operator == "x":
        ans = num1 * num2
    elif operator == "+":
        ans = num1 + num2
    elif operator == "-":
        ans = num1 - num2
    elif operator == "%":
        ans = num1 % num2
    #if we have division we switch the answer and first number to prevent 
    #decimals
    if operator == "/":
        #in division we want to prevent the second number from being a zero
        while num2 == 0:
            #so we can generate a new number
            num2 = randint(question_range_min, question_range_max)
        ans = num1 * num2
        num1, ans = ans, num1
    
    
    #converting the integers to strings
    num1_str = str(num1)
    num2_str = str(num2)
    
    #if the numbers are negative, we put brackets around them
    if num1 < 0:
        num1_str = "(" + num1_str + ")"
    if num2 < 0:
        num2_str = "(" + num2_str + ")"
    
    #creating the question statement
    statement = num1_str + " " + operator + " " + num2_str + " = "
    question_text.configure(text=statement)

#The refresh_question function generates a new question and sets the user answer
#to SKIPPED, the answer to the actual question still shows on the log and
#previous question
def refresh_question():
    global user_ans
    user_ans = "SKIPPED"
    generate_question()
    
#The check_answer function checks the answer in the given in the entry box after
#the submit button is clicked. It also checks if the input is valid, and does
#not generate a new question until valid input is entered. It also allows the
#answer to be submitted using the Enter key
def check_answer(event=None):
    global counter_correct
    global counter_incorrect
    global counter_total
    global user_ans
    user_ans = answer.get()
    #getting the valid input
    try:
        user_ans = int(user_ans)
        if user_ans == ans:
            correct_text.configure(text="CORRECT", fg="green")
            counter_correct += 1
        else:
            correct_text.configure(text="INCORRECT", fg="red")
            counter_incorrect += 1
        counter_total += 1
        #updating the counters 
        correctText = "Correct: " + str(counter_correct)
        correct_num.configure(text=correctText)
        incorrectText = "Incorrect: " + str(counter_incorrect)
        incorrect_num.configure(text=incorrectText)
        totalText = "Total: " + str(counter_total)
        total_num.configure(text=totalText)
        #generating percentage for bar and text
        percent_correct = round((counter_correct/counter_total) * 100)
        bar["value"] = percent_correct
        percent_correct_text.configure(text=str(percent_correct) + "%")
        #clearing entry box
        answer.delete(0, END)
        #generating a new question
        generate_question()
    except:
        correct_text.configure(text="ENTER VALID INPUT", fg="red")
        
#The reset_level function resets the level by setting all counters to zero and
#restoring the original text on the level screens. It also clears the log
def reset_level():
    global counter_correct
    global counter_incorrect
    global counter_total
    #resetting counters
    counter_correct = 0
    counter_incorrect = 0
    counter_total = 0
    correct_num.configure(text="Correct: 0")
    incorrect_num.configure(text="Incorrect: 0")
    total_num.configure(text="Total: 0")
    correct_text.configure(text="")
    #resetting progress bar
    bar["value"] = 100
    percent_correct_text.configure(text="100%")
    #clearing previous question and user answer
    previous_question.configure(text="Previous Question: ")
    previous_user_answer.configure(text="Your Answer: ")
    #clearing question log
    log.configure(state="normal")
    log.delete(0.0,END)
    log.configure(state="disabled")
    
#-------------------------------Main Program------------------------------------

#setting the window geometry and title
window = Tk()
window.title("Math Flash Cards Game")
window.geometry("1024x768")

#initializing global variables
ans = 0
user_ans = 0
level_num = 0
counter_correct = 0
counter_incorrect = 0
counter_total = 0
statement = ""

#----------------------------creating all Frames--------------------------------
#images used as backgrounds
start_screen_img = PhotoImage(file="title_screen.png")
level_select_img = PhotoImage(file="level_select_bg.png")
settings_img = PhotoImage(file="settings_bg.png")
level_img = PhotoImage(file="level_bg.png")
#Frames
start_screen = Frame(window, width=1024, height=768, bg="black")
start_screen.place(x=0, y=0)
#Each image is used as a label and put on its respective frame and aligned to
#0,0. Each image is the same size as the frame.
start_screen_bg = Label(start_screen, image=start_screen_img)
start_screen_bg.place(x=0, y=0)

level_select_frame = Frame(window, width=1024, height=768, bg="black")
level_select_frame.place(x=0, y=0)
level_select_bg = Label(level_select_frame, image=level_select_img)
level_select_bg.place(x=0, y=0)

level_frame = Frame(window, width=1024, height=768, bg="black")
level_frame.place(x=0, y=0)
level_bg = Label(level_frame, image=level_img)
level_bg.place(x=0, y=0)

settings_frame = Frame(window, width=1024, height=768, bg="black")
settings_frame.place(x=0, y=0)
settings_bg = Label(settings_frame, image=settings_img)
settings_bg.place(x=0, y=0)

question_log_screen = Frame(window, width=1024, height=768, bg="black")
question_log_screen.place(x=0, y=0)

#styles - for progressbar
style = ttk.Style() 
style.configure("Horizontal.TProgressbar", background = "green")


#------------------------------level select page--------------------------------
#creating widgets
#images
lvl1_img = PhotoImage(file="lvl1.png")
lvl2_img = PhotoImage(file="lvl2.png")
lvl3_img = PhotoImage(file="lvl3.png")
lvl4_img = PhotoImage(file="lvl4.png")

#labels
title = Label(level_select_frame, text="Nikhil's Math Game", \
              font=("Courier New", 60), bg="#5c93ff", fg="white")
instruction_lvl1= Label(level_select_frame, \
                        text="Level 1 - Numbers between 1 and 3", \
                        font=("Consolas", 20), fg="black", bg="#5c93ff")
instruction_lvl2= Label(level_select_frame, \
                        text="Level 2 - Numbers between 1 and 6", \
                        font=("Consolas", 20), fg="black", bg="#5c93ff")
instruction_lvl3= Label(level_select_frame, \
                        text="Level 3 - Numbers between 1 and 9", \
                        font=("Consolas", 20), fg="black", bg="#5c93ff")
instruction_lvl4= Label(level_select_frame, \
                        text="Level 4 - Numbers between 1 and 12", \
                        font=("Consolas", 20), fg="black", bg="#5c93ff")

#buttons
level1 = Button(level_select_frame, text="Level 1", font=("Impact", 30), \
                image=lvl1_img, command=show_level1)
level2 = Button(level_select_frame, text="Level 2", font=("Impact", 30), \
                image=lvl2_img, command=show_level2)
level3 = Button(level_select_frame, text="Level 3", font=("Impact", 30), \
                image=lvl3_img, command=show_level3)
level4 = Button(level_select_frame, text="Level 4", font=("Impact", 30), \
                image=lvl4_img, command=show_level4)
home_button = Button(level_select_frame, text="Home Screen", \
                     font=("impact", 30), fg="white", bg="#5c93ff", \
                     command=show_start_screen)

#placing all widgets
#placing labels
title.place(x=512, y=100, anchor="center")
instruction_lvl1.place(x=512, y=200, anchor="center")
instruction_lvl2.place(x=512, y=230, anchor="center")
instruction_lvl3.place(x=512, y=260, anchor="center")
instruction_lvl4.place(x=512, y=290, anchor="center")

#placing buttons
level1.place(x=204.8, y=384, anchor="center", height="50", width="150")
level2.place(x=409.6, y=384, anchor="center", height="50", width="150")
level3.place(x=614.4, y=384, anchor="center", height="50", width="150")
level4.place(x=819.2, y=384, anchor="center", height="50", width="150")
home_button.place(x=512, y=450, anchor="center", width=400, height=60)


#--------------------------------level page-------------------------------------
#creating widgets
#images
menu_img=PhotoImage(file="menu.png")
refresh_img=PhotoImage(file="new_question.png")
reset_img=PhotoImage(file="reset.png")
submit_img=PhotoImage(file="submit.png")

#labels
level_name = Label(level_frame, text="", font=("courier new", 30), bg ="black",\
                   fg="orange")
question_text = Label(level_frame, text="", font=("courier new", 30), \
                      bg ="black", fg="orange")
correct_text = Label(level_frame, text="", font=("impact", 30), \
                     bg="black", fg="red")
correct_num = Label(level_frame, text="Correct: 0", font=("courier new", 25), \
                    bg="black", fg="white")
incorrect_num = Label(level_frame, text="Incorrect: 0", \
                      font=("courier new", 25), bg="black", fg="white")
total_num = Label(level_frame, text="Total: 0", font=("courier new", 25), \
                  bg="black", fg="white")
previous_question = Label(level_frame, text="Previous Question: ", \
                          font=("courier new", 18), bg="black", fg="yellow")
previous_user_answer = Label(level_frame, text="Your Answer: ", \
                             font=("courier new", 18), bg="black", fg="yellow")
percent_correct_text = Label(level_frame, text="100%", font=("courier new", 30)\
                             , bg="black", fg="light green")

#buttons
menu = Button(level_frame, image=menu_img, command=show_menu)
refresh = Button(level_frame, image=refresh_img, command=refresh_question)
reset = Button(level_frame, image=reset_img, command=reset_level)
submit = Button(level_frame, image=submit_img, command=check_answer)
show_log = Button(level_frame, text="Show Question Log", \
                  font=("courier new", 30), fg="black", bg="#008088", \
                  command=show_question_log)

#entry box
answer = Entry(level_frame, font=("courier new", 30), bg="black", fg="white")
answer.focus()
answer.bind('<Return>', check_answer)

#progress bar
bar = Progressbar( level_frame, length = 500, style="Horizontal.TProgressbar")
bar["value"] = 100

#placing all widgets
#labels
level_name.place(x=512, y=40, anchor="center")
percent_correct_text.place(x=850, y=150, anchor="center")
question_text.place(x=508, y=250, anchor="e")
correct_text.place(x=512, y=100, anchor="center")
correct_num.place(x=70, y=400, anchor="w")
incorrect_num.place(x=70, y=500, anchor="w")
total_num.place(x=70, y=600, anchor="w")
previous_question.place(x=370, y=500, anchor="w")
previous_user_answer.place(x=370, y=600, anchor="w")

#buttons
menu.place(x=63, y=0, anchor="nw", height="50", width="150")
refresh.place(x=512, y=335, anchor="center", height="50", width="300")
reset.place(x=512, y=390, anchor="center", height="50", width="150")
submit.place(x=616, y=250, anchor="w", width=150, height=50)
show_log.place(x=512, y=710, anchor="center", width=500, height=100)

#entry box
answer.place(x=516, y=250, anchor="w", width=100, height=50)

#progress bar
bar.place(x=512, y=150, anchor="center")


#--------------------------------start screen-----------------------------------
#creating widgets
#images
play_button_img = PhotoImage(file="play_button.png")
settings_button_img = PhotoImage(file="options_button.png")

#label
title = Label(start_screen, text="Nikhil's Math Game", \
              font=("Courier New", 60), fg="black", bg ="#5c93ff")

#buttons
play_button = Button(start_screen, image=play_button_img, command=show_menu)
settings = Button(start_screen, image=settings_button_img,command=show_settings)

#placing widgets
#label
title.place(x=512, y=250, anchor="center")

#buttons
play_button.place(x=710, y=500, anchor="center", height="100", width="300")
settings.place(x=710, y=620, anchor="center", height="100", width="300")


#-----------------------------settings screen-----------------------------------
#creating widgets
#images
back_img=PhotoImage(file="back.png")

#labels
choose_operators = Label(settings_frame, text="Choose operators", \
                         font=("Impact", 30), bg="black", fg="light grey")

#buttons
back_settings = Button(settings_frame, image=back_img, \
                       command=show_start_screen)

#checkboxes
#checkboxes states
multiplication_state = BooleanVar()
multiplication_state.set(True) 
division_state = BooleanVar()
division_state.set(True) 
addition_state = BooleanVar()
addition_state.set(True) 
subtraction_state = BooleanVar()
subtraction_state.set(True)
remainder_state = BooleanVar()
remainder_state.set(False)
negative_numbers_state = BooleanVar()
negative_numbers_state.set(False)

#checkboxes
multiplication = Checkbutton (settings_frame, text="Multiplication",\
                              font=("Courier new", 20), bg="black", \
                              fg="hot pink", var=multiplication_state)
division = Checkbutton (settings_frame, text="Division",\
                        font=("Courier new", 20), bg="black", fg="hot pink", \
                        var=division_state)
addition = Checkbutton (settings_frame, text="Addition",\
                        font=("Courier new", 20), bg="black", fg="hot pink", \
                        var=addition_state)
subtraction = Checkbutton (settings_frame, text="Subtraction",\
                           font=("Courier new", 20), bg="black", fg="hot pink",\
                           var=subtraction_state)
remainder = Checkbutton (settings_frame, text="Remainder",\
                         font=("Courier new", 20), bg="black", fg="hot pink", \
                         var=remainder_state)
negative_numbers_checkbox = Checkbutton(settings_frame, \
                                        text="Negative numbers", \
                                        font=("Courier new", 20), bg="black", \
                                        fg="red", var=negative_numbers_state)

#placing widgets
#labels
choose_operators.place(x=512, y=100, anchor="center")

#buttons
back_settings.place(x=63, y=2, anchor="nw", height="30", width="100")

#checkboxes
multiplication.place(x=512, y=160, anchor="center")
division.place(x=512, y=210, anchor="center")
addition.place(x=512, y=260, anchor="center")
subtraction.place(x=512, y=310, anchor="center")
remainder.place(x=512, y=360, anchor="center")
negative_numbers_checkbox.place(x=512, y=470, anchor="center")


#------------------------------question Log-------------------------------------
#creating widgets
#labels
log_title = Label(question_log_screen, text="Question Log", \
                  font=("courier new", 40), bg="black", fg="white")

#buttons
back_level = Button(question_log_screen, image=back_img, command=show_level)

#scrolled text
log = scrolledtext.ScrolledText(question_log_screen, font=("Consolas", 30), \
                                fg="white", bg="black", state="disabled")

#placing widgets
#labels
log_title.place(x=512, y=10, anchor="n")

#buttons
back_level.place(x=0, y=0, anchor="nw", height="30", width="100")

#scrolled text
log.place(x=512, y=100, anchor="n", width = 800, height = 600)

#calling the show_start_screen function so the program starts at the
#start_screen
show_start_screen()
#calling the mainloop function to 
window.mainloop()
