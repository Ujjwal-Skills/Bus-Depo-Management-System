#inputs from user
start = input("Enter leaving location: ")
end = input("Enter destination location: ")
date = input("Enter date of journey (DD-MM-YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

#data storage
travel_data = [
    {"bus_number": "BUS1061", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "14:00"},
    {"bus_number": "BUS1072", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "15:00"},
    {"bus_number": "BUS1063", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "14:00"},
    {"bus_number": "BUS1509", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "19:00"},
    {"bus_number": "BUS1910", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "20:00"},
    {"bus_number": "BUS1840", "start": "CityA", "end": "CityC", "date": "12/05/2026", "time": "17:00"},
    {"bus_number": "BUS1560", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "16:00"},
    {"bus_number": "BUS1140", "start": "CityA", "end": "CityB", "date": "12/05/2026", "time": "17:30"},
    {"bus_number": "BUS1238", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "13:30"},
    {"bus_number": "BUS1380", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "19:30"},
    {"bus_number": "BUS1989", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "21:30"},
    {"bus_number": "BUS1970", "start": "CityA", "end": "CityD", "date": "12/05/2026", "time": "23:30"},
    {"bus_number": "BUS1067", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "23:15"},
    {"bus_number": "BUS1896", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "13:15"},
    {"bus_number": "BUS1904", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "24:00"},
    {"bus_number": "BUS1450", "start": "CityB", "end": "CityC", "date": "12/05/2026", "time": "15:30"}    
]

#logic for search
matches = []
for journey in travel_data:
    if (journey['start'] == start and
        journey['end'] == end and
        journey['date'] == date):
        matches.append(journey)

#display result
if matches:
    for m in matches:
       #print("Time: "+{m['time']}+" | Route: "+ {m['start']}+" to "+ {m['end']})
       #print()
       #print("Available Buses List:")
       print(f"Time: {m['time']} | Route: {m['start']} to {m['end']} | Bus Number: {m['bus_number']}")
else:
    print("No journeys match your criteria.")