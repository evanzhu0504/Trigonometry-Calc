import math
import sys
import functools
from functools import partial
import pwinput
import tkinter
from tkinter import *
from math import *
import sys
import matplotlib.pyplot as plt
import numpy as np
import ctypes
from ctypes import windll
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import simpledialog
import easygui
import json 

input("If a line of code gets stuck like this one, try hitting the \"Enter\" key on your keyboard!!!")
print("You will have to login in order to continue")

user_credentials = {}


def load_credentials():
    try:
        with open('credentials.json', 'r') as file:
            user_credentials = json.load(file)
    except FileNotFoundError:
        user_credentials = {}  
    return user_credentials

if __name__ == '__main__':
    user_credentials = load_credentials()

def update_credentials(username, password):
    user_credentials = load_credentials()
    user_credentials[username] = password

    with open('credentials.json', 'w') as file:
        json.dump(user_credentials, file)



def authenticate():
    username_input = username.get()
    password_input = password.get()

    if username_input in user_credentials and user_credentials[username_input] == password_input:
        login_successful()
    else:
        login_failed()


def login_successful():
    tkinter.messagebox.showinfo(title="Success!", message="Success! Check back your terminal after clicking OK")
    tkWindow.destroy()
    

def login_failed():
    tkinter.messagebox.showinfo(title="Failed", message="Retry after clicking OK")
    username.set("")  # Clear the username input field
    password.set("")  # Clear the password input field


def forget():
    tkinter.messagebox.showinfo(title="Forgot your password?", message="email me @ bbis.de")
    pass


def on_closing():
    tkWindow.destroy()
    sys.exit()


def need():
    tkinter.messagebox.showinfo(title="Need a Password?", message="email me @ bbis.de")

def create():
    font1 = "Arial"
    newusername = easygui.enterbox("What would you like your username to be?")
    newpassword = easygui.enterbox("What would you like your new password to be")
    if newusername == "":
        easygui.textbox("Your username cannot be blank")
    elif newpassword == "":
        easygui.textbox("Your password connot be blank")
    if newusername and newpassword != "":
        user_credentials.update({newusername: newpassword})
        update_credentials(newusername, newpassword) 


ctypes.windll.shcore.SetProcessDpiAwareness(1)
tkWindow = Tk()
tkWindow.geometry('800x500')
tkWindow.title('Login')

message = StringVar()
message_label = Label(tkWindow, textvariable=message)
message_label.grid(row=3, column=0, columnspan=2)

usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.grid(row=0, column=1, columnspan=5)

path1 = "logo.jpg"

original_image = Image.open(path1)
scaled_image = original_image.resize((360, 200))
img1 = ImageTk.PhotoImage(scaled_image)

label1 = Label(tkWindow, image=img1)
label1.place(x=400, y=0)

path2 = "triglol.jpg"
original_image = Image.open(path2)
scaled_image = original_image.resize((466, 200))
img2 = ImageTk.PhotoImage(scaled_image)

label2 = Label(tkWindow, image=img2)
label2.place(x=250, y=250)

passwordLabel = Label(tkWindow, text="Password")
passwordLabel.grid(row=2, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.grid(row=2, column=1)

loginButton = Button(tkWindow, text="Login", command=authenticate)
loginButton.grid(row=3, column=0, columnspan=2)

forgetpassword = Button(tkWindow, text="Forgot Password?", command=forget)
forgetpassword.grid(row=4, column=0, columnspan=2)

needpassword = Button(tkWindow, text="Need Password? ", command=need)
needpassword.grid(row=5, column=0, columnspan=2)

createaccount = Button(tkWindow, text="Create a account", command = create)
createaccount.grid(row=6, column=0, columnspan=2)
tkWindow.protocol("WM_DELETE_WINDOW", on_closing)
tkWindow.mainloop()


def trigcal():
    notfinished = True
    while notfinished:
        print()
        print("Welcome to the Trig Calculator created by a Standard math student")
        print()
        print("Which of the following do you need help with?")
        print("1. The easiest: The Pythagoras Theorem! On a right-angled triangle, of course")
        print("2. Sin, Cos, Tan for an unknown side")
        print("3. Sin, Cos, Tan for an unknown angle")
        print("4. Rule of Sines, while you know two sides")
        print("5. Rule of Cosines while you have two sides and an angle or you know all three sides")
        print("6. Area of the triangle while you have two sides and an angle")
        print("7. Use the graphing calculator")
        print("Enter 'exit' to exit the program")
        print()

        user_choice = input("Please select a mode based on the prompts, or type 'exit' to exit the program: ")

        if user_choice.lower() == "exit":
            print("Thank you for using this Calculator")
            sys.exit(0)

        try:
            mode = int(user_choice)
            if 1 <= mode <= 7:
                if mode == 1:
                    pythagoras()
                elif mode == 2:
                    rightangledtrig()
                elif mode == 3:
                    rightangledtriangle()
                elif mode == 4:
                    sinrule()
                elif mode == 5:
                    cosrule()
                elif mode == 6:
                    areatriangle()
                elif mode == 7:
                    graphing()

            else:
                print("You did not enter a valid mode (1-7).")
        except ValueError:
            print("Please enter a valid mode (1-7) or 'exit' to exit the program.")


def pythagoras():
    print("a^2 + b^2 = c^2 calculator")
    a = ""
    b = ""
    c = ""

    ask = input("What variable do you want to solve for? C for the hypotenuse and A/B for the two sides ")
    if any(ask.lower() == f for f in ["a", "1"]):
        b = input("Type In B: ")
        while not b.isdigit():
            print("That isnt a number! Retype it please!")
            b = input("Type In B: ")
        b = int(b)
        c = input("Type In c: ")
        while not c.isdigit():
            print("That isnt a number! Retype it please!")
            c = input("Type In c: ")
        c = int(c)
        a = math.sqrt(c ** 2 - b ** 2)
        print("A = " + str(a))
    if any(ask.lower() == f for f in ["b", "2"]):
        a = input("Type In A: ")
        while not a.isdigit():
            print("That isnt a number! Retype it please!")
            a = input("Type In A: ")
        c = input("Type In c: ")
        while not c.isdigit():
            print("That isnt a number! Retype it please!")
            c = input("Type In c: ")
        c = int(c)
        b = math.sqrt(int(c) ** 2 - int(a) ** 2)
        print("B = " + str(b))
    if any(ask.lower() == f for f in ["c", "3"]):
        a = input("Type In A: ")
        while not a.isdigit():
            print("That isnt a number! Retype it please!")
            a = input("Type In A: ")
        b = input("Type In B: ")
        while not b.isdigit():
            print("That isnt a number! Retype it please!")
            b = input("Type In B: ")
        c = int(a) ** 2 + int(b) ** 2
        if math.sqrt(c).is_integer():
            c = int(math.sqrt(c))
            print("C^2 = " + str(c))
            c = int(c)
        else:
            print("C = " + "√" + str(c))
            c = math.sqrt(c)
            print("(Decimal) c = " + str(c))
            c = "√" + str(int(a) ** 2 + int(b) ** 2)

    a = int(a)
    b = int(b)

    X = np.array([[0 + int(a), 0], [0 + a, 0 + b], [0, 0]])
    Y = ['red', 'red', 'red']

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s=170, color=Y[:])
    plt.grid()
    t1 = plt.Polygon(X[:3, :], color=Y[0])
    plt.gca().add_patch(t1)
    plt.title("Triangle Grapher")
    plt.text(a / 2, b / 2 + b / 8, 'Hypotenuse = ' + str(c), fontsize=10, bbox=dict(facecolor='red', alpha=0.5),
             rotation=35)
    plt.show()


def sinrule():
    notfinished = True
    while notfinished:
        try:
            mode = int(input("Choose your mode: 1 for finding a side and 2 for finding an angle: "))
            if mode in [1, 2]:
                if mode == 1:
                    side1 = float(input("Type in the length of side 1: "))
                    angle1 = float(input(
                        "Angle 1 (The Angle corresponding to your 1 side in degrees, do not put the degree sign haha): "))
                    angle2 = float(input(
                        "Tell me the other angle that you know that corresponds to the side you want to find out: "))
                    print("According to the great Sines rule, the third")
                    print(f"Unknown side / sin({angle2}) = {side1} / sin({angle1})")
                    print("So...")
                    print(f"Unknown side = {side1} * {angle2} / sin({angle1})")
                    result = (side1 * math.sin(math.radians(angle1))) / math.sin(math.radians(angle2))
                    print()
                    print(f"The unknown side is: {round(result, 3)} long (Don't forget the 3 significant figures rule)")
                    print()
                    notfinished = False
                elif mode == 2:
                    side1 = float(input("Tell me your first side that corresponds to the known angle: "))
                    side2 = float(input("Tell me your second side that corresponds to the unknown angle: "))
                    angle1 = float(input("Tell me now the angle that corresponds to side 1: "))
                    print()
                    print("According to the Rule of Sines, the third")
                    print(f"sin(The unknown angle) / {side2} = sin({angle1}) / {side1}")
                    print("Therefore...")
                    print(f"Unknown angle = sin({side2} * sin({angle1})) / {side1}")
                    result = math.degrees(math.asin((side2 * math.sin(math.radians(angle1))) / side1))
                    print()
                    print(f"The angle is: {round(result, 3)} degrees wide (Don't forget the 3 significant figure rule)")
                    print()
                    notfinished = False
            else:
                print()
                print("You must enter either 1 or 2")
                print()
        except ValueError:
            print()
            print("Please try again.")
            print()


def cosrule():
    notfinished = True
    while notfinished:
        try:
            mode = int(
                input("Please choose the mode, 1 for finding a missing side and 2 for finding a missing angle: "))
            if mode in [1, 2]:
                if mode == 1:
                    side1 = float(input("Please tell me your first side length: "))
                    side2 = float(input("Please tell me your second side length: "))
                    angle1 = float(input(
                        "Please tell me your angle which is not included with the two sides that you inputted earlier: "))
                    print("The cosine rule states that")
                    print(f"{side1}^2 + {side2}^2 - (2 * {side1} * {side2} * cos({angle1})")
                    calc = side1 ** 2 + side2 ** 2 - (2 * side1 * side2 * math.cos(math.radians(angle1)))
                    result = math.sqrt(calc)
                    print()
                    print(f"The side is {round(result, 3)} long (3 significant figure rule")
                    print()
                    notfinished = False
                elif mode == 2:
                    a = float(input("Please Tell me the length of the First side: "))
                    b = float(input("Please Tell me the length of the Second side: "))
                    c = float(input("Please Tell me the length of the Third side: "))
                    print("According to the cosine rule")
                    print(f"Angle A = inv cos( ({b}^2 + {c}^2 - {a}^2 / (2*{b}*{c}) )")
                    print(f"Angle A = inv cos( ({a}^2 + {c}^2 - {b}^2 / (2*{a}*{c}) )")
                    print(f"Angle A = inv cos( ({a}^2 + {b}^2 - {c}^2 / (2*{a}*{b}) )")
                    print("Angles That is Calculated:")
                    calc1 = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
                    calc2 = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
                    calc3 = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
                    calcs = [calc1, calc2, calc3]
                    for calc in calcs:
                        if -1 <= calc <= 1:
                            result = math.degrees(math.acos(calc))
                            print(round(result, 3))
                    print("These are your angles")
                    notfinished = False
            else:
                print()
                print("You must enter either 1 or 2")
                print()
        except ValueError:
            print()
            print("The calculator didn't understand one of your inputs.")
            print()


def rightangledtrig():
    notfinished = True
    while notfinished:
        try:
            unknown = input(
                "Which unknown side is relative to your angle REF? h for the hypotenuse, a for adjacent, and o for the opposite side: ")
            known = input(
                "Which known side is relative to your angle REF? h for hypotenuse, a for adjacent, and o for the opposite side: ")
            if unknown.lower() in ["h", "a", "o"] and known.lower() in ["h", "a", "o"] and unknown != known:
                angle = float(input("Tell me the angle that you know in degrees, do not type the angle sign: "))
                known1 = float(input("Enter the length of the side that you know: "))
                notfinished = False
                if unknown == "h":
                    print("The hypotenuse is unknown")
                    if known == "a":
                        print("Adjacent side known, using the cosine.")
                        print("since cos() = adj / hyp")
                        print(f"unknown side = {known1} / cos({angle})")
                        result = known1 / math.cos(math.radians(angle))
                        print()
                        print(f"The side is {round(result, 3)} long")
                        print()
                    elif known == "o":
                        print("Opposite side is known, using sinus")
                        print("Since sin = opp / hyp")
                        print(f"unknown side = {known1} / sin({angle})")
                        result = known1 / math.sin(math.radians(angle))
                        print()
                        print(f"The side calculated is {round(result, 3)} long")
                        print()
                elif unknown == "a":
                    print("Adjacent side is unknown")
                    if known == "h":
                        print("Hypotenuse known, using cosine")
                        print("Since cos() = adj / hyp,")
                        print(f"Unknown side = {known1} * cos ({angle})")
                        result = math.cos(math.radians(angle) * known1)
                        print()
                        print(f"The side is {round(result, 3)} long")
                        print()
                    elif known == "o":
                        print("Opposite side known, using tan")
                        print("Since tan() = opp / adj,")
                        print(f"unknown side = {known1} / tan({angle})")
                        result = known1 / math.tan(math.radians(angle))
                        print()
                        print(f"The side is {round(result, 3)} long")
                        print()
                elif unknown == "o":
                    print("Opposite side is unknown")
                    if known == "h":
                        print("Hypotenuse is known, using sin")
                        print("since sin() = opp / hyp,")
                        print(f"unknown side = {known1} * sin({angle})")
                        result = math.sin(math.radians(angle)) * known1
                        print()
                        print(f"The side is {round(result, 3)} long")
                        print()
                    elif known == "a":
                        print("Adjacent side known, using tan()")
                        print("Since tan() = opp / adj,")
                        print(f"Unknown side = {known1} * tan({angle})")
                        result = known1 * math.tan(math.radians(angle))
                        print()
                        print(f"The side calculated is {round(result, 3)} long")
                        print()
            else:
                print("Please say either 'h', 'a', or 'o'")
        except ValueError:
            print()
            print("You didn't put in a correct letter, try again")
            print()


def rightangledtriangle():
    notdone = True
    while notdone:
        try:
            known1 = input(
                "What is the first side you know Relative to your Angle REF. h for hypotenuse, a for adjacent, o for opposite: ")
            known2 = input(
                "What is the second side you know Relative to your Angle REF. h for hypotenuse, a for adjacent, o for opposite: ")
            if known2.lower() in ["h", "a", "o"] and known1.lower() in ["h", "a", "o"] and known1 != known2:
                length1 = float(input("Specify the length of the first known side: "))
                length2 = float(input("Specify the length of the second known side: "))
                if known1 == "h" and known2 == "a":
                    print("Hypotenuse and adjacent side known, using the reverse cosine")
                    print("since cos() = adj / hyp,")
                    print(f"unknown angle = inv cos ({length2} / {length1})")
                    result = math.degrees(math.acos(length2 / length1))
                    print()
                    print(f"Angle is {round(result, 3)} degrees")
                    print()
                elif known1 == "h" and known2 == "o":
                    print("Hypotenuse and opposite side known, using reverse sine")
                    print("since sin() = opp / hyp")
                    print(f"Unknown angle = inv sin({length2} / {length1})")
                    result = math.degrees(math.asin(length2 / length1))
                    print()
                    print(f"Angle is {round(result, 3)} degrees")
                    print()
                elif known1 == "a" and known2 == "h":
                    print("Hypotenuse and adjacent side known, using reverse cosine")
                    print("Since cos() adj / hyp,")
                    print(f"unknown angle = inv cos({length1} / {length2})")
                    result = math.degrees(math.acos(length1 / length2))
                    print()
                    print(f"Your angle is {round(result, 3)} degrees")
                    print()
                elif known1 == "o" and known2 == "a":
                    print("Opposite and adjacent side known, using reverse tangent")
                    print("Since tan() = opp / adj,")
                    print(f"unknown angle = inv tan ({length2} = {length1})")
                    result = math.degrees(math.atan(length2 / length1))
                    print()
                    print(f"Your angle is {round(result, 3)} degrees")
                    print()
                notdone = False
            else:
                print("Please type either 'h', 'a', or 'o'")
        except ValueError:
            print("One of the things you typed is incorrect, please try again")


def areatriangle():
    notfinished = True
    while notfinished:
        try:
            length1 = float(input("Tell me the length of side 1: "))
            length2 = float(input("Tell me the length of side 2: "))
            angle = float(input("Tell me the angle that is in between the two sides you gave me: "))
            print("Area of a triangle = 0.5(a*b*sin(c)),")
            print(f"area = 0.5({length1} * {length2} * sin ({angle}))")
            result = 0.5 * length1 * length2 * math.sin(math.radians(angle))
            print()
            print(f"The area of your Triangle is: {round(result, 3)}")
            print()
            notfinished = False
        except ValueError:
            print()
            print("You didn't put in the right number, try again.")
            print()


def graphing():
    notfinished = True
    add = 0
    s = str(input("Enter function, f(x) is already included inside the code : "))  # Inputs function
    temp = s
    s = s.replace('x', '(x)')
    ctr, x, y = -10, [], []  # Setting countert to starting values and x, y to empty lists
    while ctr <= 10:
        s1 = ''
        add = 0
        s1 = s.replace('x', str(ctr))  # Replaces variable with value at that point
        try:
            add = eval(s1)  # Tries to evaluate function at that point, if defined
            y.append(add)
            x.append(ctr)
        except:
            pass  # If beyond domain, pass
        ctr += 0.1

    plt.figure(num='Graphing Calculator')
    plt.plot(x, y, label='y = ' + temp, color='blue')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    ax = plt.gca()
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.1, 1.05))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.show()
    plt.close()
    notfinished = False


while True:
    trigcal()
