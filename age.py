from datetime import datetime

while True:
    birthdate_inp = input("Enter a birthdate in the format DD-MM-YYYY: ")
    try:
        birthdate = datetime.strptime(birthdate_inp, "%d-%m-%Y")

        todays_date = datetime.today()
        age = todays_date.year - birthdate.year

        if (todays_date.day, todays_date.month) < (birthdate.day, birthdate.month):
            age -= 1

        print(f"You are {age} years old.")

    except ValueError:
        print("Date input is incorrectly formatted. Must be DD-MM-YYYY..")
