#Greetings
print("\n||------------------------------Welcome To City Buses------------------------------||\n")

#inputs from user
start = input("Please enter leaving location: ").strip().lower()
end = input("Please enter destination location: ").strip().lower()
date = input("Please enter date of journey (DD/MM/YYYY): ")
#time = input("Enter time of journey (HH:MM): ")

#data storage
travel_data = [
    #date 01/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "01/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "01/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "01/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "01/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "01/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "01/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "01/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "01/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "01/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "01/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "01/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "01/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "01/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "01/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "01/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "01/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "01/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "01/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "01/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "01/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "01/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "01/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "01/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "01/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 02/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "02/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "02/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "02/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "02/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "02/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "02/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "02/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "02/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "02/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "02/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "02/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "02/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "02/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "02/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "02/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "02/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "02/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "02/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "02/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "02/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "02/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "02/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "02/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "02/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 03/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "03/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "03/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "03/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "03/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "03/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "03/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "03/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "03/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "03/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "03/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "03/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "03/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "03/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "03/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "03/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "03/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "03/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "03/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "03/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "03/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "03/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "03/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "03/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "03/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 04/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "04/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "04/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "04/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "04/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "04/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "04/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "04/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "04/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "04/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "04/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "04/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "04/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "04/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "04/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "04/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "04/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "04/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "04/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "04/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "04/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "04/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "04/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "04/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "04/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 05/0/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "05/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "05/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "05/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "05/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "05/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "05/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "05/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "05/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "05/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "05/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "05/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "05/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "05/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "05/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "05/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "05/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "05/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "05/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "05/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "05/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "05/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "05/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "05/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "05/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 06/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "06/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "06/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "06/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "06/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "06/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "06/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "06/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "06/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "06/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "06/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "06/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "06/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "06/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "06/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "06/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "06/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "06/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "06/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "06/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "06/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "06/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "06/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "06/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "06/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},

    #date 07/04/2026
    #route a to b 
    {"bus_number": "BUS1061", "start": "City A", "end": "City B", "date": "07/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City A", "end": "City B", "date": "07/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City A", "end": "City B", "date": "07/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City A", "end": "City B", "date": "07/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route b to a
    {"bus_number": "BUS1061", "start": "City B", "end": "City A", "date": "07/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1072", "start": "City B", "end": "City A", "date": "07/04/2026", "time": "15:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1560", "start": "City B", "end": "City A", "date": "07/04/2026", "time": "16:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    {"bus_number": "BUS1140", "start": "City B", "end": "City A", "date": "07/04/2026", "time": "17:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 50},
    #route a to c
    {"bus_number": "BUS1063", "start": "City A", "end": "City C", "date": "07/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City A", "end": "City C", "date": "07/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City A", "end": "City C", "date": "07/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City A", "end": "City C", "date": "07/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route c to a
    {"bus_number": "BUS1063", "start": "City C", "end": "City A", "date": "07/04/2026", "time": "14:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1509", "start": "City C", "end": "City A", "date": "07/04/2026", "time": "19:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1910", "start": "City C", "end": "City A", "date": "07/04/2026", "time": "20:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    {"bus_number": "BUS1840", "start": "City C", "end": "City A", "date": "07/04/2026", "time": "17:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 45},
    #route  b to c
    {"bus_number": "BUS1067", "start": "City B", "end": "City C", "date": "07/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City B", "end": "City C", "date": "07/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City B", "end": "City C", "date": "07/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City B", "end": "City C", "date": "07/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    #route c to b
    {"bus_number": "BUS1067", "start": "City C", "end": "City B", "date": "07/04/2026", "time": "23:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1896", "start": "City C", "end": "City B", "date": "07/04/2026", "time": "13:15", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1904", "start": "City C", "end": "City B", "date": "07/04/2026", "time": "24:00", "seats": 20, "selected_seat": ["Available"]*20, "price": 65},
    {"bus_number": "BUS1450", "start": "City C", "end": "City B", "date": "07/04/2026", "time": "15:30", "seats": 20, "selected_seat": ["Available"]*20, "price": 65}
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
    print("\n-------------Available Buses List:-------------")
    for m in matches:
       print("Bus Number: "+m['bus_number']+" | Route: "+ m['start']+" to "+ m['end']+" | Time: "+m['time']+" | Available seats: "+str(m['seats']))

    #Bus selection logic
    bus_selection = input("\nPlease select desired bus by entering bus number: ").strip().upper()

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
            seat_count = int(input("\nPlease enter number of seats you want to book: "))
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
                    confirmation = input("Please enter 'Confirm'/'Cancel' for booking: ").strip().lower()
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

