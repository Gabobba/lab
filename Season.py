def checkSeason(month, day):
    seasonChange = isSeasonChanging(month, day)
    if not isValidMonth(month):
        print("Non pensavo che in un anno ci fossero " + str(month) + " mesi!")
        return
    if not isValidDay(day):
        print("Il giorno inserito non esiste.")
        return
    if (month == 1 or month == 2 or month ==3):
        if(seasonChange):
            print("Spring")
        else:
            print("It's winter!")
    elif (month ==4 or month == 5 or month == 6):
        if (seasonChange):
            print("Summer")
        else:
            print("It's spring")
    elif (month == 7 or month==8 or month==9):
        if (seasonChange):
            print("Fall")
        else:
            print("It's sommer!")
    else:
        if (seasonChange):
            print("Winter")
        else:
            print("It's fall!")
    return


def isValidMonth(month):
    return(month>0 and month<=12)


def isValidDay(day):
    return (day>0 and day<=31)


def isSeasonChanging(month, day):
    return (month%3 == 0 and day >= 21)


checkSeason(12, 23)
