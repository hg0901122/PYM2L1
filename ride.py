ride = input("Select a ride (Bike, Car): ").strip().upper()

if ride == "BIKE":
    type = input("What type of bike do you want (City, MTB): ").strip().upper()

if ride == "CAR":
    type = input("What type of car do you want (normal, sport): ").strip().upper()

print("You have choosen a", ride,"of type", type)

