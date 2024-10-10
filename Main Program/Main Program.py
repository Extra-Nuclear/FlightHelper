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
            #I have put freqencys in when the ACT gives them to the pilot O
           


        elif choice == 2:
            print(f"{DEPARTURE} Delivery, good day, {CALLSIGN} at stand {STAND}, with information {INFO}, requesting clearance to {ARRIVAL}")
            SID = input("DEPARTURE SID = ")
            RUNWAY = (input("RUNWAY = ")).upper()
            SQUAWK = int(input("SQUAWK = "))
            #does this need to be an int? or would it work better as a string? O
            input("---PRESS--ENTER--TO--CONTINUE---")
            print(f"Cleared to {ARRIVAL}, {SID} departure, runway {RUNWAY}, squawk {SQUAWK}, {CALLSIGN}")
            print("(1) Readback Correct")
            print("(2) Change Something")
            mini_choice = int(input("= "))
            print(f"Report when ready, {CALLSIGN}")


        elif choice == 3:
            stage = "Push & Start"


    while stage == "Push & Start":
        os.system("cls")
        print (f"Runway = {RUNWAY}  Squawk = {SQUAWK} SID = {SID}")
        print("/n")
        print (f"{CALLSIGN}, Fully ready")
        GROUNDFRQ = input("GROUND FREQUENCY = ")
        print("(Switch to Ground Frequency)")
        input("---PRESS--ENTER--TO--CONTINUE---")
        print (f"{DEPARTURE} Ground, Good day, {CALLSIGN} ready for pushback and startup")
        print (f"Startup and pushback approved {CALLSIGN}")
        input("---PRESS--ENTER--TO--CONTINUE---")
        stage = "Taxi"


    while stage == "Taxi":
        print(f"{CALLSIGN}, Request Taxi")
        ROUTE = input("ROUTE: ")
        print (f" Taxi Holding point Runway {RUNWAY} {ROUTE} {CALLSIGN}") # what is the S7 in the Guide? O
        input("---PRESS--ENTER--TO--CONTINUE---")
        stage = "Line up and Takeoff"


    while stage == "Line up and Takeoff":
        TOWERFRQ = input("TOWER FREQUENCY = ")
        print(F"Contact Tower on {TOWERFRQ} {CALLSIGN} Bye Bye!")
        #switch to tower O
        print(f"Switch to {TOWERFRQ}")
        input("---PRESS--ENTER--TO--CONTINUE---")
        #give them time to chaange O
        print(f"{DEPARTURE} Tower, Good day {CALLSIGN} at {RUNWAY}")

        
    

 









    run = False


