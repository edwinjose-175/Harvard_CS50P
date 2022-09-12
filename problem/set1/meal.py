# Edited return expression of 'Convert' function
    # added a precision of 2 to the round function
    # changed type cast of float to int for the 'hours' and 'minutes' variable

def main():
    meal_time = input("What time is it? ")
    # convert function call
    converted_meal_time = convert(meal_time)

    if  7.0 <= converted_meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_meal_time <= 19.0:
        print("dinner time")
    else:
        pass

def convert(meal_time):
    hours, minutes = meal_time.split(":")
    if ' ' in minutes:
        minutes, meridiem = minutes.split()
        if meridiem == 'a.m.':
            return int(hours) + round(int(minutes)/60, 2)
        elif meridiem == 'p.m.':
            return (int(hours) + 12) + round(int(minutes)/60, 2)
    else:
        return int(hours) + round(float(minutes)/60, 2)

if __name__ == "__main__":
    main()
