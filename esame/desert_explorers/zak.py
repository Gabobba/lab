import csv
import math
import os

def parseData(filePath: str):
    if filePath.endswith(".csv") or filePath.endswith(".txt"):
        with open(filePath, "r") as csvFile:
            csvReader = csv.DictReader(csvFile)
            return [row for row in csvReader]
    else:
        raise ValueError("File is not a CSV or TXT.")


def getDiscreteDistance(start: tuple[int, int], goal: tuple[int, int]):
    x1,y1 = start
    x2,y2 = goal

    hd = abs(x2-x1)
    vd = abs(y2-y1)
    return math.sqrt(vd**2 + hd**2)


def getMinimumExitDistance(coords: tuple[int, int], size: tuple[int, int]):
    width, height = size
    x,y = coords

    distances: dict = {}
    distances["top"] = getDiscreteDistance((x,y), (x, width))
    distances["bot"] = getDiscreteDistance((x,y), (x,0))
    distances["left"] = getDiscreteDistance((x, y), (0, y))
    distances["right"] = getDiscreteDistance((x, y), (height, y))

    return min(distances.items(), key=lambda item: item[1])



def canExitDesert(survivor: dict) -> bool:
    maxDistance = float(survivor["speed"]) * float(survivor["endurance"])
    survivorCoords = (int(survivor["x"]), int(survivor["y"]))
    minimumDistance = getMinimumExitDistance(survivorCoords, (500, 500))
    return maxDistance >= minimumDistance[1]


def canReach(survivor: dict, goal: tuple[int, int]):
    maxDistance = float(survivor["speed"]) * float(survivor["endurance"])
    start = int(survivor["x"]), int(survivor["y"])
    distance = getDiscreteDistance(start, goal)
    return maxDistance >= distance


def travel(survivor: dict, to: tuple[int, int]):
    survivor["x"], survivor["y"] = to


def madeItToOasis(survivor: dict, oases: list) -> bool:
    madeIt: bool = False
    visited = survivor["visitedOasis"]
    for oasis in oases:
        if oasis not in visited:
            ox, oy = int(oasis["coord_x"]), int(oasis["coord_y"])
            if canReach(survivor, (ox, oy)):
                visited.append(oasis)
                survivor["visitedOasis"] = visited
                travel(survivor, (ox, oy))
                madeIt = True

    return madeIt


if __name__ == '__main__':
    desertData = parseData("./database/desert.csv")
    survivorsData = parseData("./database/survivors.txt")

    desert = desertData
    oases = []

    for desertPOI in desert:
        if desertPOI["location_type"] == "oasis":
            oases.append(desertPOI)

    survivors = survivorsData
    safe = []
    dead = []

    for survivor in survivors:
        survivor["visitedOasis"] = []


    while survivors:
        # immediate survivors
        for survivor in survivors:
            if canExitDesert(survivor):
                survivors.remove(survivor)
                safe.append(survivor)

        # iterate until everyone is either safe or dead (until survivor is empty)
        for survivor in survivors:
            if not madeItToOasis(survivor, oases):
                dead.append(survivor)
                survivors.remove(survivor)

    survivalChance = 100 * len(safe) / (len(safe) + len(dead))

    print("Sopravvissuti: " + str(survivalChance) + "%")
    print("")
    print("Recupero salme esploratori")
    for deceased in dead:
        print("<" + str(deceased["id"]) + ">: (" + str(deceased["x"]) + ", " + str(deceased["y"]) + ")")




