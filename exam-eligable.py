medical = input("Do you have any medical condition? (y/n): ")
medical = medical.strip().upper()

if medical == "Y":
    print("You are allowed for exam.")
else:
    attendance = int(input("What is your attendance?: "))
    if attendance >= 75:
        print("You are allowed for the exam.")
    else:
        print("You AREN'T allowed for exam.")
