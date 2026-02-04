#inputs from user
start = input("Enter leaving location: ")
end = input("Enter destination location: ")
date = input("Enter date of journey (DD-MM-YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

'''bus_list = [{"bus_number": "BUS101",}]
print(bus_list)
 #"bus_number": "BUS101", "from": "CityA", "to": "CityB", "date": "15-09-2023", "time": "10:00"},

routes = {
    "CityA-to-CityB":[
        {"date": "12-05-2024", "time": "14:00"},
        {"date": "12-05-2024", "time": "14:30"}
        {"date": "12-05-2024", "time": "15:00"},
        {"date": "12-05-2024", "time": "15:30"}
        {"date": "12-05-2024", "time": "16:00"},
        {"date": "12-05-2024", "time": "16:30"}
    ]
}'''

#data storage
travel_data = [
    {"bus_number": "BUS101", "start": "CityA", "end": "CityB", "date": "12-05-2026", "time": "14:00"},
    {"bus_number": "BUS102", "start": "CityA", "end": "CityB", "date": "12-05-2026", "time": "15:00"},
    {"bus_number": "BUS103","start": "CityA", "end": "CityC", "date": "12-05-2026", "time": "14:00"}
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