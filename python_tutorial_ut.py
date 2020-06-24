"""
function

requirements
"""


def get_name_and_age():
    name = input("enter your name: ")
    age = input("enter your age ")
    if name[0].upper() == "M":
        print("Your name starts with " + name[0])
    elif name[0].upper() == "S":
        print("your name starts with", name[0])
    else:
        print("your name does not start with W or F ", name)


def got_a_bill():
    keepgoing = False
    answer = input("\nChristy did you get a bill? ")

    if answer == "yes" or answer == "yea":
        print(answer)
        keepgoing = True
        print("Fucking Sweet")
    elif answer == "no" or answer == "nah":
        keepgoing = False
        print("Its alright you will get em next time")
    return keepgoing


def run_bill_app():
    loop = True
    while loop:
        loop = got_a_bill()

run_bill_app()
