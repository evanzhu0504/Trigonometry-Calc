import math
import sys
import discord
from discord.ext import commands


input("If a line of code gets stuck like this one, try hitting the \"Enter\" key on your keyboard!!!")
print("You will have to login in order to continue")

user_credentials = {
    "evantheboss": "1977",
    "username2": "password2",
    "username3": "password3",

}


def authenticate(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    return False


def mainauth():
    print("Welcome to the login page")

    while True:
        username = input("Enter your username:")
        password = input("Enter your password:")

        if authenticate(username, password):
            print("Authentication Success")
            print("Enjoy the calculator!")
            break
        else:
            print("Authentication Failed, please try again")


if __name__ == "__main__":
    mainauth()


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
        print("Enter 'exit' to exit the program")
        print()

        user_choice = input("Please select a mode based on the prompts, or type 'exit' to exit the program: ")

        if user_choice.lower() == "exit":
            print("Thank you for using this Calculator")
            sys.exit(0)

        try:
            mode = int(user_choice)
            if 1 <= mode <= 6:
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
            else:
                print("You did not enter a valid mode (1-6).")
        except ValueError:
            print("Please enter a valid mode (1-6) or 'exit' to exit the program.")


def pythagoras():
    notfinished = True
    while notfinished:
        try:
            mode = int(input(
                "Please choose the mode: 1 for finding the hypotenuse and 2 for finding one side when you have a hypotenuse and a side already: "))
            if mode in [1, 2]:
                if mode == 1:
                    side1 = float(input("Put in your first side: "))
                    side2 = float(input("Put in your second side: "))
                    result = math.hypot(side1, side2)
                    print(f"The hypotenuse = sqrt({side1} + {side2})")
                    print()
                    print(f"The hypotenuse is {result} long. (Remember The 3 significant figure rule)")
                    print()
                    notfinished = False
                elif mode == 2:
                    side1 = float(input("Tell me your hypotenuse: "))
                    side2 = float(input("Tell me the length of your other known side: "))
                    result = math.sqrt((side1 ** 2 - side2 ** 2))
                    print(f"Hypotenuse = sqrt({side1} - {side2})")
                    print()
                    print(f"The Hypotenuse is {result} long. (Don't forget the 3 significant figure rule)")
                    print()
                    notfinished = False
            else:
                print()
                print("How do you not type in 1 or 2?")
                print()
        except ValueError:
            print()
            print("Let's try that again:")
            print()


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
                    print(f"The unknown side is: {result} long (Don't forget the 3 significant figures rule)")
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
                    print(f"The angle is: {result} degrees wide (Don't forget the 3 significant figure rule)")
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
                    print(f"The side is {result} long (3 significant figure rule")
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
                        if calc >= -1 and calc <= 1:
                            result = math.degrees(math.acos(calc))
                            print(result)
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
                        print(f"The side is {result} long")
                        print()
                    elif known == "o":
                        print("Opposite side is known, using sinus")
                        print("Since sin = opp / hyp")
                        print(f"unknown side = {known1} / sin({angle})")
                        result = known1 / math.sin(math.radians(angle))
                        print()
                        print(f"The side calculated is {result} long")
                        print()
                elif unknown == "a":
                    print("Adjacent side is unknown")
                    if known == "h":
                        print("Hypotenuse known, using cosine")
                        print("Since cos() = adj / hyp,")
                        print(f"Unknown side = {known1} * cos ({angle})")
                        result = math.cos(math.radians(angle) * known1)
                        print()
                        print(f"The side is {result} long")
                        print()
                    elif known == "o":
                        print("Opposite side known, using tan")
                        print("Since tan() = opp / adj,")
                        print(f"unknown side = {known1} / tan({angle})")
                        result = known1 / math.tan(math.radians(angle))
                        print()
                        print(f"The side is {result} long")
                        print()
                elif unknown == "o":
                    print("Opposite side is unknown")
                    if known == "h":
                        print("Hypotenuse is known, using sin")
                        print("since sin() = opp / hyp,")
                        print(f"unknown side = {known1} * sin({angle})")
                        result = math.sin(math.radians(angle)) * known1
                        print()
                        print(f"The side is {result} long")
                        print()
                    elif known == "a":
                        print("Adjacent side known, using tan()")
                        print("Since tan() = opp / adj,")
                        print(f"Unknown side = {known1} * tan({angle})")
                        result = known1 * math.tan(math.radians(angle))
                        print()
                        print(f"The side calculated is {result} long")
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
                    print(f"Angle is {result} degrees")
                    print()
                elif known1 == "h" and known2 == "o":
                    print("Hypotenuse and opposite side known, using reverse sine")
                    print("since sin() = opp / hyp")
                    print(f"Unknown angle = inv sin({length2} / {length1})")
                    result = math.degrees(math.asin(length2 / length1))
                    print()
                    print(f"Angle is {result} degrees")
                    print()
                elif known1 == "a" and known2 == "h":
                    print("Hypotenuse and adjacent side known, using reverse cosine")
                    print("Since cos() adj / hyp,")
                    print(f"unknown angle = inv cos({length1} / {length2})")
                    result = math.degrees(math.acos(length1 / length2))
                    print()
                    print(f"Your angle is {result} degrees")
                    print()
                elif known1 == "o" and known2 == "a":
                    print("Opposite and adjacent side known, using reverse tangent")
                    print("Since tan() = opp / adj,")
                    print(f"unknown angle = inv tan ({length2} = {length1})")
                    result = math.degrees(math.atan(length2 / length1))
                    print()
                    print(f"Your angle is {result} degrees")
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
            print(f"The area of your Triangle is: {result}")
            print()
            notfinished = False
        except ValueError:
            print()
            print("You didn't put in the right number, try again.")
            print()


while True:
    trigcal()