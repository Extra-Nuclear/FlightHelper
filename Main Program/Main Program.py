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
            input("---PRESS--ENTER--TO--CONTINUE---")
            os.system("cls")
            print(f"{DEPARTURE} Delivery, good day, {CALLSIGN} at stand {STAND}, with information {INFO}, requesting clearance to {ARRIVAL}")
            SID = input("DEPARTURE SID = ")
            RUNWAY = (input("RUNWAY = ")).upper()
            SQUAWK = int(input("SQUAWK = "))
            print(f"Cleared to {ARRIVAL}, {SID} departure, runway {RUNWAY}, squawk {SQUAWK}, {CALLSIGN}")
            mini_choice = input("---PRESS--ENTER--TO--CONTINUE---")
            while mini_choice != 1:
                print("(1) Readback Correct")
                print("(2) Change Something")
                mini_choice = int(input("-> "))
                if mini_choice == 2:
                    SID = input("DEPARTURE SID = ").upper()
                    RUNWAY = (input("RUNWAY = ")).upper()
                    SQUAWK = int(input("SQUAWK = ")).upper()
            print(f"Report when ready, {CALLSIGN}")
            input("--PRESS--ENTER--FOR--NEXT--STAGE---")
            stage = "Push & Start"
        
        elif choice == 2:
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
        print("(Switch to Ground Frequency)")
        input("---PRESS--ENTER--TO--CONTINUE---")
        print (f"{DEPARTURE} Ground, Good day, {CALLSIGN} at stand {STAND}, ready for pushback and startup")
        while push_done != True:
            print("(1) No Push Direction")
            print("(2) Yes Push Direction")  
            mini_choice = int(input("= "))
            if mini_choice == 2:
                PSH_DREC = input("PUSH DIRECTION = ").upper()
                print (f"Startup and pushback approved, facing {PSH_DREC}, {CALLSIGN}")
                push_done = True
            if mini_choice == 1:
                print (f"Startup and pushback approved, {CALLSIGN}")
                push_done = True
        input("---PRESS--ENTER--TO--CONTINUE---")
        stage = "Taxi"


    while stage == "Taxi":
        print(f"{CALLSIGN}, Request Taxi")
        ROUTE = input("ROUTE: ").upper()
        HOLDINGPOINT = input("HOLDING POINT = ").upper()
        print (f" Taxi, Holding point {HOLDINGPOINT}, Runway {RUNWAY}, {ROUTE}, {CALLSIGN}") 
        input("---PRESS--ENTER--TO--CONTINUE---")
        stage = "Line up and Takeoff"

    while stage == "Line up and Takeoff":
        TOWERFRQ = input("TOWER FREQUENCY = ").upper()
        print(F"Contact Tower on {TOWERFRQ}, {CALLSIGN}, Bye Bye!")
        print(f"(Switch to {TOWERFRQ})")

        input("---PRESS--ENTER--TO--CONTINUE---")

        print(f"{DEPARTURE} Tower, Good day, {CALLSIGN} at {HOLDINGPOINT}")
        print(f"Line up and wait Runway {RUNWAY}, {CALLSIGN}")
        input("---PRESS--ENTER--TO--CONTINUE---")
        print(f"Cleared For take of, Runway {RUNWAY}, {CALLSIGN}")

        input("---PRESS--ENTER--TO--CONTINUE---")

        stage = "Depature and climbing on the SID"


    while stage == "Depature and climbing on the SID":
        os.system ("cls")
        FL = ("Flight level = ").upper()
        print(f"{DEPARTURE} Aporoch, Good day, {CALLSIGN}, {SID}, passing FL{FL}")
        TARGETFL = ("TARGET FL")
        print (f"Climb FL{TARGETFL}, {CALLSIGN}")
        RADARST = input("REGION RADAR = ").upper()
        RADARFRQ = input("RADAR FREQUENCY = ").upper()
        input("---PRESS--ENTER--TO--CONTINUE---")


    

    run = False


