#Greetings
print("\n||------------------------------Welcome To City Buses------------------------------||\n")

#inputs from user
start = input("Please enter the leaving location: ").strip().lower()
end = input("Please enter destination location: ").strip().lower()
#date logic
a = 1
while a == 1:
    date = input("Please enter date of journey (DD/MM/YYYY): ")

    if len(date) == 10 and date[2] == "/" and date[5] == "/":
        day = date[0:2]
        month = date[3:5]
        year = date[6:10]

        if day.isdigit() and month.isdigit() and year.isdigit():
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                break
            else:
                print("Invalid day or month!")
        else:
            print("Date must contain only numbers!")
    else:
        print("Invalid date format! Use DD/MM/YYYY")

#ate = input("Please enter date of journey (DD/MM/YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

#data storage
travel_data = []

routes = [
    #forward routes
    ["City A", "City B", 50],
    ["City A", "City C", 55],
    ["City A", "City D", 60],
    ["City A", "City E", 95],
    ["City B", "City C", 70],
    ["City B", "City D", 75],
    ["City B", "City E", 90],
    ["City C", "City D", 85],
    ["City C", "City E", 80],
    ["City D", "City E", 65],
    #back routes
    ["City B", "City A", 50],
    ["City C", "City A", 55],
    ["City D", "City A", 60],
    ["City E", "City A", 95],
    ["City C", "City B", 70],
    ["City D", "City B", 75],
    ["City E", "City B", 90],
    ["City D", "City C", 85],
    ["City E", "City C", 80],
    ["City E", "City D", 65]

]

times = ["06:00","08:00","10:00","12:00","13:00", "14:00", "15:00", "17:00", "19:00","21:00","22:00"]

bus_no = 1000

for r in routes:
    for t in times:
        bus_no += 1

        travel_data.append({
            "bus_number": "BUS" + str(bus_no),
            "start": r[0],
            "end": r[1],
            "date": date,
            "time": t,
            "price": r[2],  
            "seats": 20,
            "selected_seat": ["Available"] * 20
        })

#logic for search
matches = []
for journey in travel_data:
    if (journey['start'].strip().lower() == start and
        journey['end'].strip().lower() == end and
        journey['date'] == date):
        matches.append(journey)

#display Available Buses List
if matches:
    print("\n-------------Available Buses List:-------------")
    for m in matches:
       print("Bus Number: "+m['bus_number']+" | Route: "+ m['start']+" to "+ m['end']+" | Time: "+m['time']+" | Available seats: "+str(m['seats']))

    #Bus selection logic
    bus_selection = input("\nPlease select the desired bus by the entering bus number: ").strip().upper()

    for bus in matches: 
        if bus_selection == bus['bus_number']:
            
            #seat map and selection logic

            #display the visual map
            print("\n+---------------------------------+")
            print("|      Seat Map for",bus['bus_number'],"      |")
            print("+----------Front of Bus-----------+")
            for i in range(0,len(bus["selected_seat"]),4):
                row = ""
                for j in range(4):
                    #if seat booked show XX else show seat number
                    if bus["selected_seat"][i+j] == 'X':
                        row = row + ' [XX] '
                    else:
                        seat_no = i + j + 1
                        if seat_no < 10:
                            row = row + "  [S0" + str(seat_no) + "] "
                        else:
                            row = row + "  [S" + str(seat_no) + "] "
                        
                print("|" + row + " |")
            print("+------------Back of Bus----------+")
            
            #seat selection logic
            seat_count = int(input("\nPlease enter the number of seats you want to book: "))
            if seat_count <= bus['seats']:
                chosen = [] #store chosen seat number
                
                #loop until user selects required seats
                x = 0
                while x < seat_count:
                    seat = int(input("Please enter seat number: ")) - 1
                    if seat < 0 or seat >= len(bus["selected_seat"]): #check seat validity
                        print("Invalid seat number!")
                    elif seat in chosen: #check duplicate seat entry
                        print("You already selected this seat!")
                    elif bus["selected_seat"][seat] == "X": #check already booked seat
                        print("Seat is already booked!")
                    else:
                        chosen.append(seat)
                        x += 1

                #ticket fare logic    
                ticket = bus["price"]*seat_count
                print("\n|  Your bill is ₹",ticket,"  |")

                #ticket confirmation logic
                a = 1
                while a == 1:
                    confirmation = input("\nPlease enter 'Confirm'/'Cancel' for booking: ").strip().lower()
                    if confirmation == 'confirm':
                        for s in chosen:
                            bus["selected_seat"][s] = "X"
                        
                        #reduce available seat count
                        bus["seats"] = bus["seats"] - len(chosen)

                        print("\nYOUR SEAT IS BOOKED SUCCESSFULLY!")
                        a-=1
                        
                        #logic for adding seat number in ticket
                        seat_string = ""
                        for s in chosen:
                            if s+1 < 10:
                                seat_string = seat_string + "S0" + str(s+1) + " "
                            else:
                                seat_string = seat_string + "S" + str(s+1) + " "

                        #ticket id logic
                        ticket_id = (bus["bus_number"][3:7]+bus["start"][5]+bus["end"][5]+bus["date"][0:5]+seat_string[0:3])
                        #print(ticket_id)

                        #ticket Summary
                        print()
                        print("+-------------------------------------------------+")
                        print("|                Booking Summary                  |")
                        print("+-------------------------------------------------+")
                        print("| DATE: ",bus['date'],"  | Bus No.: ",bus['bus_number'],"        |")
                        print("| TIME: ",bus['time'],"       | Seat No.: ",seat_string,"      |")
                        print("| FROM: ",bus['start'],"      |                           |")
                        print("| TO:   ",bus['end'],"      | PRICE: ",ticket,"              |")
                        print("+-------------------------------------------------+")
                        print("| TICKET ID: ",ticket_id,"                     |")
                        print("+-------------------------------------------------+")

                        print("\n||--------------------Thanks for Traveling using City Buses--------------------||")


                    elif confirmation == 'cancel':
                        #chosen.clear()  #clear selected seats
                        print("\nCancellation Successful!")
                        a-=1

            else:
                print("Sorry! These many seats are not available.")
                #continue
else:
    print("No journeys match your criteria.")  