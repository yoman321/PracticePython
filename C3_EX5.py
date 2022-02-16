#Find future dates

def dayOfWeek(day):
    match day:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"

currentDay = int(input("Enter today's date: "))
elapsedDay = int(input("Enter the number of days elapsed since today: "))

targetDay = currentDay + elapsedDay % 7

if (targetDay >= 7):
    targetDay %= 7

print("Today is {} and the future days is {}".format(dayOfWeek(currentDay), dayOfWeek(targetDay)))
