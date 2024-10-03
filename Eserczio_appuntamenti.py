def evalOverlap(start1, end1, start2, end2):
    if (isTimeConsistent(start1) and
        isTimeConsistent(end1) and
        isTimeConsistent(start2) and
        isTimeConsistent(end2)
    ):
        if (end1 >= start1 and end2 >= start2):
            if (end1 > start2):
                print("Non è possibile prendere un appuntamento")
            else:
                print("Appuntamento preso")
            return
        else:
            print("I dati inseriti non sono corretti")
            return
    else:
        print("L'orario inserito non esiste")


def isTimeConsistent(time):
    return (time >= 0 and time <= 23)


evalOverlap(8, 10, 9, 13)
