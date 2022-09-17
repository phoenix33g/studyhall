class Person:
    def __init__(self, name, nextInLine):
        self.name = name
        self.nextInLine = nextInLine

def getMyPositionInLine(person):
    if person.nextInLine == None:
        return 1
    return 1 + getMyPositionInLine(person.nextInLine)


p1 = Person("Bill", None)
p2 = Person("Carry", p1)
p3 = Person("Monica", p2)
p4 = Person("Jerry", p3)


print(p3.name + " is " + str(getMyPositionInLine(p3)) + " in line.")