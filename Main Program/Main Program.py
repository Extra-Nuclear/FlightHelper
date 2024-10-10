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
            CALLSIGN = input("CALLSIGN = ").upper()
            STAND = input("STAND = ").upper()
            DEPARTURE = input("DEPARTURE = ").upper()
            ARRIVAL = input("ARRIVAL = ").upper()
            INFO = input("ATIS INFO = ").upper()
            print(f"\n")
            print("F̲r̲e̲q̲u̲e̲n̲c̲i̲e̲s̲: ")
            GROUNDFRQ = input("GROUND FREQUENCY").upper()


        elif choice == 2:
            print(f"{DEPARTURE} Delivery, good day, {CALLSIGN} at stand {STAND}, with information {INFO}, requesting clearance to {ARRIVAL}")
            SID = input("DEPARTURE SID = ")
            RUNWAY = int(input("RUNWAY = "))
            SQUAWK = int(input("SQUAWK = "))
            input("---PRESS--ENTER--TO--CONTINUE---")
            print(f"Cleared to {ARRIVAL}, {SID} departure, runway {RUNWAY}, squawk {SQUAWK}, {CALLSIGN}")
            print("(1) Readback Correct")
            print("(2) Change Something")
            mini_choice = int(input("= "))
            print(f"Report when ready, {CALLSIGN}")


        elif choice == 3:
            stage = "Push & Start"
    while stage == "Push & Start":

        print (f"{CALLSIGN} Information {INFO} Contact Ground on {GROUNDFRQ} ")








    run = False


