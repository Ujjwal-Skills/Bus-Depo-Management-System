#Greetings
print("\n||---Welcome To City Buses---||\n")

#inputs from user
start = input("Please enter leaving location: ").strip().lower()
end = input("Please enter destination location: ").strip().lower()
date = input("Please enter date of journey (DD/MM/YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

#data storage
travel_data = [
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "12/05/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "12/05/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "12/05/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "12/05/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "12/05/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "12/05/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "12/05/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "12/05/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1238", "start": "City A", "end": "City D", "date": "12/05/2026", "time": "13:30", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1380", "start": "City A", "end": "City D", "date": "12/05/2026", "time": "19:30", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1989", "start": "City A", "end": "City D", "date": "12/05/2026", "time": "21:30", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1970", "start": "City A", "end": "City D", "date": "12/05/2026", "time": "23:30", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "12/05/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "12/05/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "12/05/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "12/05/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20}    
]

#logic for search
matches = []
for journey in travel_data:
    if (journey['start'].strip().lower() == start and
        journey['end'].strip().lower() == end and
        journey['date'] == date):
        matches.append(journey)

#display Available Buses List
if matches:
    print("\n--Available Buses List:--")
    for m in matches:
       print("Bus Number: "+m['bus_number']+" | Route: "+ m['start']+" to "+ m['end']+" | Time: "+m['time']+" | Available seats: "+str(m['seats']))

    #Bus selection logic
    bus_selection = input("\nPlease select desired bus by entering bus number: ").strip().upper()

    for bus in travel_data: 
        if bus_selection == bus['bus_number']:

            '''#seat map and selection logic
            available_now = bus["selected_seat"].count("Available")
            booked_status = "XX"
            #display the visual map
            print("+---------Seat Map for ",bus['bus_number'],"---------+")
            print("|              Front of Bus              |")
            print("+----------------------------------------+")
            for i in range(0,len(bus["selected_seat"]),4):
                if bus["selected_seat"][i] == 'X':
                    s1 = booked_status
                else:
                    s1 = "S" + str(i+1)
                
                if bus["selected_seat"][i+1] == 'X':
                    s2 = booked_status
                else:
                    s2 = "S" + str(i+2)
                
                if bus["selected_seat"][i+2] == 'X':
                    s3 = booked_status
                else:
                    s3 = "S" + str(i+3)

                if bus["selected_seat"][i+3] == 'X':
                    s4 = booked_status
                else:
                    s4 = "S" + str(i+4)
                
                print("|"+ s1 + "|" + s2 + "|" + s3 + "|" + s4 +"|")
            print("+---------------Back of Bus---------------+")'''
        
            seat_selection = int(input("Please enter number of seats you want to book: "))

            if seat_selection <= bus['seats']:

                #ticket fare logic    
                ticket = 50*seat_selection
                print("\n|  Your bill is ₹",ticket,"  |")

                #ticket confirmation logic
                a = 1
                while a == 1:
                    confirmation = input("Please enter 'Confirm'/'Cancel' for booking: ").strip().lower()
                    if confirmation == 'confirm':
                        print("\nYOUR SEAT IS BOOKED SUCCESSFULLY!")
                        bus['seats'] -= seat_selection
                        a-=1

                        #ticket id logic
                        ticket_id = (bus["bus_number"][3:7]+bus["start"][5]+bus["end"][5]+bus["date"][0:5])
                        #print(ticket_id)

                        #ticket Summary
                        print()
                        print("+-------------------------------------------------+")
                        print("|                Booking Summary                  |")
                        print("+-------------------------------------------------+")
                        print("| DATE: ",bus['date'],"  | Bus No.: ",bus['bus_number'],"        |")
                        print("| TIME: ",bus['time'],"       | Seat No.: S00             |")
                        print("| FROM: ",bus['start'],"      |                           |")
                        print("| TO:   ",bus['end'],"      | PRICE: ",ticket,"              |")
                        print("+-------------------------------------------------+")
                        print("| TICKET ID: ",ticket_id,"                        |")
                        print("+-------------------------------------------------+")

                    elif confirmation == 'cancel':
                        print("\nCancellation Successful!")
                        a-=1

            #print("Available seats: "+ str(bus['seats']))

            else:
                print("Sorry! These many seats are not available.")

else:
    print("No journeys match your criteria.")

