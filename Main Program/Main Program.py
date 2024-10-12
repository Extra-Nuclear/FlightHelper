#Import
import os
import time
import sys


#Formating:

BOLD = "\033[1m"
RESET = "\033[0m"
ITALIC = "\033[3m"
FAINT = "\033[2m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"


#Variables:

run = True
stage = "Clearance"
FLIGHT_PLAN = ["","","","","","","","","","","","","","",""]
FLIGHT_PLAN_INDEX = 0
GLOBAL_FLIGHT_PLAN_INDEX = 0
FLIGHT_PLAN_MAX = 1
NUMBER = 0
FLIGHT_PLAN_TEMP = ""

#Start

print(f"""{CYAN}
{CYAN}███████╗██╗░░░░░██╗░██████╗░██╗░░██╗████████╗{BLUE}██╗░░██╗███████╗██╗░░░░░██████╗░███████╗██████╗░
{CYAN}██╔════╝██║░░░░░██║██╔════╝░██║░░██║╚══██╔══╝{BLUE}██║░░██║██╔════╝██║░░░░░██╔══██╗██╔════╝██╔══██╗
{CYAN}█████╗░░██║░░░░░██║██║░░██╗░███████║░░░██║░░░{BLUE}███████║█████╗░░██║░░░░░██████╔╝█████╗░░██████╔╝
{CYAN}██╔══╝░░██║░░░░░██║██║░░╚██╗██╔══██║░░░██║░░░{BLUE}██╔══██║██╔══╝░░██║░░░░░██╔═══╝░██╔══╝░░██╔══██╗
{CYAN}██║░░░░░███████╗██║╚██████╔╝██║░░██║░░░██║░░░{BLUE}██║░░██║███████╗███████╗██║░░░░░███████╗██║░░██║
{CYAN}╚═╝░░░░░╚══════╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░{BLUE}╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝{RESET}""")
print("-"*93)


while run == True:
    while stage == "END PROGRAM":
        os. _exit()
    while stage == "Clearance":
        print(f"{BOLD}Stage : C̲l̲e̲a̲r̲a̲n̲c̲e̲{RESET} ")
        print("Select an option below:")
        print("(1) Start - Input Values")
        print("(2) Quit - Exit the Program")
        choice = int(input("= "))
        os.system("cls")

        if choice == 1:
            FLIGHT_PLAN_MAX = int(input("FLIGHT PLAN MAX VALUES = "))
            for i in range(FLIGHT_PLAN_MAX):
                FLIGHT_PLAN_TEMP = input(f"FLIGHT PLAN VALUE {NUMBER} = ").upper()
                FLIGHT_PLAN[NUMBER] = FLIGHT_PLAN_TEMP
                NUMBER = NUMBER + 1
            print(FLIGHT_PLAN)
            print(FLIGHT_PLAN_TEMP)
            print(FLIGHT_PLAN_INDEX)
            time.sleep(3)
            os.system("cls")
            CALLSIGN = input("CALLSIGN = ").upper()
            STAND = input("STAND = ").upper()
            DEPARTURE = input("DEPARTURE = ").upper()
            ARRIVAL = input("ARRIVAL = ").upper()
            INFO = input("ATIS INFO = ").upper()
            PLANE = input("PLANE TYPE (eg. A32N) = ").upper()
            print("")
            input("---PRESS--ENTER--TO--CONTINUE---")
            os.system("cls")

            print("")
            print(f"{DEPARTURE} Delivery, good day, {CALLSIGN} at stand {STAND}, with information {INFO}, {PLANE}, requesting clearance to {ARRIVAL}")
            
            print("")
            SID = input("DEPARTURE SID = ")
            RUNWAY = (input("RUNWAY = ")).upper()
            SQUAWK = int(input("SQUAWK = "))
            print("")
            print(f"Cleared to {ARRIVAL}, {SID} departure, runway {RUNWAY}, squawk {SQUAWK}, {CALLSIGN}")
            print("")
            mini_choice = input("---PRESS--ENTER--TO--CONTINUE---")
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
        FL = int(input("Flight level = "))
        print("")
        print(f"{DEPARTURE} Aproach, Good day, {CALLSIGN}, {SID} departure, passing FL{FL}")
        print("")
        TARGETFL = int(input("CLIMB TO FL = "))
        print("")
        print (f"Climb FL{TARGETFL}, {CALLSIGN}")
        print("")
        RADARNM = input("REGION RADAR NAME = ").upper()
        RADARFRQ = input("RADAR FREQUENCY = ").upper()
        print("")
        
        stage == "Radar"
        os.system("cls")
    while stage == "Radar":
        FLIGHT_PLAN_INBOUND = FLIGHT_PLAN[GLOBAL_FLIGHT_PLAN_INDEX + 1]
        choice = input("--PRESS--ENTER--TO--CONTINUE---")
        while choice != 2:
                print(f"Current = {FLIGHT_PLAN[GLOBAL_FLIGHT_PLAN_INDEX]}")
                print(f"Inbound = {FLIGHT_PLAN_INBOUND}")
                print("")
                print("(1) Next Waypoint")
                print("(2) Continue")
                choice = int(input("= "))
                if choice == 1:
                    GLOBAL_FLIGHT_PLAN_INDEX = GLOBAL_FLIGHT_PLAN_INDEX + 1
                    choice = 0
        print(f"{RADARNM} Radar, good day, {CALLSIGN}, passing FL{FL} for {TARGETFL}, inbound {FLIGHT_PLAN_INBOUND}")

        
    

    


    

    run = False


