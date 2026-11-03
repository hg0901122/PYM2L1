unit = int(input("What is the number of units you are consuming: "))

if unit <= 50:
    usage = unit * 2.60
    surcharge = 25
elif unit <= 100:
    usage = (50 * 2.60) + (unit - 50) * 3.25
    surcharge = 35
elif unit <= 200:
    usage = (50 * 2.60) + (50 * 3.25) + (unit - 100) * 5.26
    surcharge = 45
else:
    usage = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + (unit - 200) * 8.45
    surcharge = 75

total = usage + surcharge
print("Total cost: ",total)