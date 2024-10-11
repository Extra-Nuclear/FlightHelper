#Import
import os

#Variables:
run = True
stage = "Clearance"
FLIGHT_PLAN = []
FLIGHT_PLAN_INDEX = 1

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
    while stage == "END PROGRAM":
        os. _exit()
    while stage == "Clearance":
        print("Stage : C̲l̲e̲a̲r̲a̲n̲c̲e̲ ")
        print("Select an option below:")
        print("(1) Start - Input Values")
        print("(2) Quit - Exit the Program")
        choice = int(input("= "))
        os.system("cls")

        if choice == 1:
            CALLSIGN = input("CALLSIGN = ").upper()
            STAND = input("STAND = ").upper()
            DEPARTURE = input("DEPARTURE = ").upper()
            ARRIVAL = input("ARRIVAL = ").upper()
            INFO = input("ATIS INFO = ").upper()
            print("")
            input("---PRESS--ENTER--TO--CONTINUE---")
            os.system("cls")
            print(f"{DEPARTURE} Delivery, good day, {CALLSIGN} at stand {STAND}, with information {INFO}, requesting clearance to {ARRIVAL}")
            print("")
            SID = input("DEPARTURE SID = ")
            RUNWAY = (input("RUNWAY = ")).upper()
            SQUAWK = int(input("SQUAWK = "))
            print("")
            print(f"Cleared to {ARRIVAL}, {SID} departure, runway {RUNWAY}, squawk {SQUAWK}, {CALLSIGN}")
            print("")
            mini_choice = input("---PRESS--ENTER--TO--CONTINUE---")
            while mini_choice != 1:
                print("")
                print("(1) Readback Correct")
                print("(2) Change Something")
                mini_choice = int(input("= "))
                if mini_choice == 2:
                    print("")
                    SID = input("DEPARTURE SID = ").upper()
                    RUNWAY = (input("RUNWAY = ")).upper()
                    SQUAWK = int(input("SQUAWK = ")).upper()
            print("")
            print(f"Report when ready, {CALLSIGN}")
            print("")
            input("--PRESS--ENTER--FOR--NEXT--STAGE---")
            stage = "Push & Start"
        
        elif choice == 2:
            print("")
            input("--PRESS--ENTER--TO--QUIT---")
            stage = "END PROGRAM"


    while stage == "Push & Start":
        push_done = False
        os.system("cls")
        print (f"Runway = {RUNWAY} | Squawk = {SQUAWK} | SID = {SID}")
        print("")
        print (f"{CALLSIGN}, Fully ready")
        QNH = input("QNH = ").upper()
        GROUNDFRQ = input("GROUND FREQUENCY = ").upper()
        print(f"QNH {QNH}, information {INFO}, Ground on {GROUNDFRQ}, {CALLSIGN}")
        print("")
        print("(Switch to Ground Frequency)")
        print("")
        input("---PRESS--ENTER--TO--CONTINUE---")
        os.system("cls")
        print (f"{DEPARTURE} Ground, Good day, {CALLSIGN} at stand {STAND}, ready for pushback and startup")
        while push_done != True:
            print("")
            print("(1) No Push Direction")
            print("(2) Yes Push Direction")  
            mini_choice = int(input("= "))
            if mini_choice == 2:
                print("")
                PSH_DREC = input("PUSH DIRECTION = ").upper()
                print("")
                print (f"Startup and pushback approved, facing {PSH_DREC}, {CALLSIGN}")
                push_done = True
            if mini_choice == 1:
                print("")
                print (f"Startup and pushback approved, {CALLSIGN}")
                push_done = True
        print("")
        input("--PRESS--ENTER--FOR--NEXT--STAGE---")
        stage = "Taxi"


    while stage == "Taxi":
        print(f"{CALLSIGN}, Request Taxi")
        print("")
        ROUTE = input("ROUTE: ").upper()
        HOLDINGPOINT = input("HOLDING POINT = ").upper()
        print("")
        print (f" Taxi, Holding point {HOLDINGPOINT}, Runway {RUNWAY}, {ROUTE}, {CALLSIGN}") 
        print("")
        input("--PRESS--ENTER--FOR--NEXT--STAGE---")

        stage = "Line up and Takeoff"

    while stage == "Line up and Takeoff":
        os.system("cls")
        print (f"ROUTE = {ROUTE} | HOLDING POINT = {HOLDINGPOINT} | RUNWAY = {RUNWAY}")
        print("")
        TOWERFRQ = input("TOWER FREQUENCY = ").upper()
        print("")
        print(F"Contact Tower on {TOWERFRQ}, {CALLSIGN}, Bye Bye!")
        print("")
        print(f"(Switch to {TOWERFRQ})")
        print("")
        input("---PRESS--ENTER--TO--CONTINUE---")
        os.system("cls")
        print(f"{DEPARTURE} Tower, Good day, {CALLSIGN} at {HOLDINGPOINT}")
        print("")
        print(f"Line up and wait, Runway {RUNWAY}, {HOLDINGPOINT}, {CALLSIGN}")
        print("")
        input("---PRESS--ENTER--TO--CONTINUE---")
        print("")
        print(f"Cleared For take of, Runway {RUNWAY}, {CALLSIGN}")
        print("")
        input("--PRESS--ENTER--FOR--NEXT--STAGE---")

        stage = "Depature and climbing on the SID"


    while stage == "Depature and climbing on the SID":
        os.system ("cls")
        FL = ("Flight level = ").upper()
        print("")
        print(f"{DEPARTURE} Aporoch, Good day, {CALLSIGN}, {SID} departure, passing FL{FL}")
        print("")
        TARGETFL = ("CLIMB TO FL = ")
        print("")
        print (f"Climb FL{TARGETFL}, {CALLSIGN}")
        print("")
        RADARNM = input("REGION RADAR NAME = ").upper()
        RADARFRQ = input("RADAR FREQUENCY = ").upper()
        print("")
        input("--PRESS--ENTER--TO--CONTINUE---")
        os.system("cls")

        print(f"{RADARNM} Radar, good day, {CALLSIGN}, passing FL{FL} for {TARGETFL}")

        
    

    


    

    run = False


