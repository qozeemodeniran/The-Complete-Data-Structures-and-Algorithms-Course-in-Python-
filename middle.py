def MiddleElement(myList):
    newList = []
    for i in range(len(myList)):
        if myList[i] == myList[0] or myList[i] == myList[-1]:
            continue
        else:
            newList.append(myList[i])
    return newList

print(MiddleElement([4, 9, 1, 2, 3, 4]))