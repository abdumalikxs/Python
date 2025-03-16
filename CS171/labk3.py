import math


def museumParkingPrice(entryDay, entryHour, entryMinute, exitHour, exitMinute, visitType):
    price = 0
    if exitHour == entryHour and exitMinute == entryMinute:
        price = 0
    if visitType == "Member" and (((exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute)) < 60):
        return 0
    if entryDay == "Friday" and (visitType == "Member" or visitType == "Public") and entryHour >= 17:
        if exitHour > entryHour:
            price = 10
        elif exitHour * 60 + exitMinute < entryHour * 60 + entryMinute:
            price = 10 + 2 * exitHour
    elif entryDay == "Friday" and visitType == "Visitor" and entryHour >= 17:
        if exitHour >= entryHour:
            return 10
        else:
            return 10 + 2 * math.ceil((exitHour * 60 + exitMinute)/60)

    if entryDay != 'Friday':
        if visitType == "Public" and (entryHour*60 + entryMinute) < (exitHour * 60 + exitMinute):
            if (exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute) < 4 * 60:
                price = 39
            else:
                price = 39 + 2 * \
                    math.ceil(
                        ((((exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute))/60 - 4)))
        elif visitType == "Public" and (entryHour*60 + entryMinute) > (exitHour * 60 + exitMinute):
            price = 39 + 2 * \
                math.ceil((1440 - (entryHour * 60 + entryMinute) +
                          (exitMinute + exitHour * 60)) / 60 - 4)
        elif visitType == "Visitor" and (entryHour*60 + entryMinute) < (exitHour * 60 + exitMinute):
            if (exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute) < 4 * 60:
                price = 20
            else:
                price = 20 + 2 * \
                    math.ceil(
                        ((((exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute))/60 - 4)))
        elif visitType == "Visitor" and (entryHour*60 + entryMinute) > (exitHour * 60 + exitMinute):
            price = 20 + 2 * \
                math.ceil((1440 - (entryHour * 60 + entryMinute) +
                          (exitMinute + exitHour * 60)) / 60 - 4)
        elif visitType == "Member" and (entryHour*60 + entryMinute) < (exitHour * 60 + exitMinute):
            if (exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute) < 4 * 60:
                price = 15
            else:
                price = 15 + 2 * \
                    math.ceil(
                        ((((exitHour * 60 + exitMinute) - (entryHour * 60 + entryMinute))/60 - 4)))
        elif visitType == "Member" and (entryHour*60 + entryMinute) > (exitHour * 60 + exitMinute):
            price = 15 + 2 * \
                math.ceil((1440 - (entryHour * 60 + entryMinute) +
                          (exitMinute + exitHour * 60)) / 60 - 4)

    if price > 55:
        return 55
    return price


print(museumParkingPrice("Tuesday", 10, 15, 13, 45, "Visitor"))
print(museumParkingPrice("Wednesday", 9, 45, 13, 46, "Member"))
print(museumParkingPrice("Sunday", 13, 45, 10, 15, "Public"))
print(museumParkingPrice("Friday", 18, 18, 19, 7, "Member"))
print(museumParkingPrice("Friday", 18, 18, 7, 9, "Visitor"))


# Some minor fixes  needed here
