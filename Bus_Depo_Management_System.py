#Greetings
print("\n||---Welcome To City Buses---||\n")

#inputs from user
start = input("Please enter leaving location: ")
end = input("Please enter destination location: ")
date = input("Please enter date of journey (DD-MM-YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

#data storage
travel_data = [
    {"bus_number": "BUS1061", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "14:00", "seats": 20},
    {"bus_number": "BUS1072", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "15:00", "seats": 20},
    {"bus_number": "BUS1063", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "14:00", "seats": 20},
    {"bus_number": "BUS1509", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "19:00", "seats": 20},
    {"bus_number": "BUS1910", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "20:00", "seats": 20},
    {"bus_number": "BUS1840", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "17:00", "seats": 20},
    {"bus_number": "BUS1560", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "16:00", "seats": 20},
    {"bus_number": "BUS1140", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "17:30", "seats": 20},
    {"bus_number": "BUS1238", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "13:30", "seats": 20},
    {"bus_number": "BUS1380", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "19:30", "seats": 20},
    {"bus_number": "BUS1989", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "21:30", "seats": 20},
    {"bus_number": "BUS1970", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "23:30", "seats": 20},
    {"bus_number": "BUS1067", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "23:15", "seats": 20},
    {"bus_number": "BUS1896", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "13:15", "seats": 20},
    {"bus_number": "BUS1904", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "24:00", "seats": 20},
    {"bus_number": "BUS1450", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "15:30", "seats": 20}    
]

#logic for search
matches = []
for journey in travel_data:
    if (journey['start'] == start and
        journey['end'] == end and
        journey['date'] == date):
        matches.append(journey)

#display Available Buses List
if matches:
    print("\n--Available Buses List:--")
    for m in matches:
       print("Bus Number: "+m['bus_number']+" | Route: "+ m['start']+" to "+ m['end']+" | Time: "+m['time']+" | Available seats: "+str(m['seats'])) 
else:
    print("No journeys match your criteria.")

#Bus selection and ticket fare logic
bus_selection = input("\nPlease select desired bus by entering bus number: ")

for bus in travel_data: 
    if bus_selection == bus['bus_number']:
        seat_selection = int(input("Please enter number of seats you want to book: "))

        if seat_selection <= bus['seats']:

            ticket = 50*seat_selection
            print("\n|  Your bill is ₹",ticket,"  |")
            #ticket confirmation logic
            a = 1
            while a == 1:
                confirmation = input("Please enter 'Confirm'/'Cancel' for booking: ").strip().lower()
                if confirmation == 'confirm':
                    print("\nYOUR SEAT IS BOOKED")
                    bus['seats'] -= seat_selection
                    #a-=1
                    break
                elif confirmation == 'cancel':
                    print("\nCancellation Successful")
                    #a-=1
                    break

        #print("Available seats: "+ str(bus['seats']))

        else:
            print("Sorry! These many seats are not available.")