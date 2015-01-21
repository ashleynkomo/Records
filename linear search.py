def GetContactIndex(contactList):
    nameToFind = input("Please enter contact name: ")
    for index in range(len(contactList)):
        if contactList[index].name == nameToFind:
            return index
    return -1 


#main
contactList = ["Jack","Bill","Kerri","Alphonse","Edward",
               "Jones","James","Arnold","Stacy","Phil"]
GetContactIndex(contactList)
print(index)
