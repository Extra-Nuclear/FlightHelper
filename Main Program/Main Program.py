#Import
import os

#Variables:
run = True
stage = "Clearance"


#Start

print("""
███████╗██╗░░░░░██╗░██████╗░██╗░░██╗████████╗██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
██╔════╝██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
█████╗░░██║░░░░░██║██║░░██╗░███████║░░░██║░░░███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
██╔══╝░░██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
██║░░░░░███████╗██║╚██████╔╝██║░░██║░░░██║░░░██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝""")
print("-"*93)


while run == True:
    while stage == "Clearance":
        print("Stage : C̲l̲e̲a̲r̲a̲n̲c̲e̲ ")
        print("Select an option below:")
        print("(1) Input Values")
        print("(2) Generate Text")
        print("(3) Next Stage")
        choice = int(input("= "))
        os.system("cls")

        if choice == 1:
            CALLSIGN = input("CALLSIGN = ")
            STAND = input("STAND = ")
            DEPARTURE = input("DEPARTURE = ")
            ARRIVAL = input("ARRIVAL = ")
            INFO = input("ATIS INFO = ")


        elif choice == 2:
            pass

        elif choice == 3:
            stage = "Push & Start"
        elif choice ==3:
    run = False

