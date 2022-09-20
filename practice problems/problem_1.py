"""
Given a list of people with their birth and death
years, find the year with the highest population.

people = 
1750 -> 1803 -> 1809 -> 1840 -> 1845 -> 1860 -> 1869 -> 1894
1900 -> 1920 -> 1921 -> 1935 -> 1955 -> 1969 -> 

"""
people = [
    [1999, 2013],
    [1955, 1999],
    [2020],
    [1920, 1989],
    [1999, 1999],
    [1987, 1989],
    [1845, 1900],
    [1969, 2022],
    [1803, 1809],
    [1750, 1869],
    [1860, 1921],
    [1840, 1935],
    [1894, 1921],
    [2000],
    [1998],
    [1988],
    [1860,1921],
    [1987, 1989]
]

# My trible Idea
def _hashYears(people, count = 0, hash = {}):
    if len(people) <= count: return hash
    if len(people) <= 1: return people[0]
    aliveFor = people[count]
    if not aliveFor: return
    if len(aliveFor) < 2: aliveFor.append(2022)
    for year in range(aliveFor[0], aliveFor[1]+1):
        if year in hash:
            hash[year] += 1
        else:
            hash[year] = 1
    return _hashYears(people, count+1, hash)


def findYearRange(people):
    hashYears = _hashYears(people)
    highest = 0
    list = []
    for year in hashYears:
        if hashYears[year] > highest:
            list.clear()
            list.append(year)
            highest = hashYears[year]
        elif hashYears[year] == highest:
            list.append(year)
    print(list)


#findYearRange(people)
# Try 2 ====================================================================
# ==========================================================================

def getMostPopYear(people):
    unorderedTimelineDelta, firstBirthYear, lastBirthYear = _timelineHash(people)



# Well, this is obvious now
def _timelineHash(people, count=0, firstBirth=99999, lastBirth=0, hash={}):
    if len(people) <= count: return hash, firstBirth, lastBirth
    if len(people) <= 1: return people[0]
    if len(people[count]) < 2: people[count].append(None)
    born, death = people[count]
    # Checking for earliest and latest Birth year
    if born < firstBirth: firstBirth = born
    if born > lastBirth: lastBirth = born
    # Adding up or down values to the delta hash
    if born in hash:
        hash[born] += 1
    else:
        hash[born] = 1
    if death:
        deathN = death + 1
        if deathN in hash:
            hash[deathN] -= 1
        else:
            hash[deathN] = -1
    return _timelineHash(people, count+1, hash)

#print(_timelineHash(people))

# Try 3 ====================================================================
# ==========================================================================

class DepthNode:
    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
        self.right = None
        self.left = None
        self.depth = 0
    def insertFromRoot(self, pos, val):
        if self.pos == pos:
            self.val += val
        elif self.pos < pos:
            if self.right == None:
                self.right = DepthNode(pos, val)
                self.right.depth = self.depth + val
            elif self.right.pos <= pos:
                self.depth -= val
                self.right.insertFromRoot(pos, val)
            else:
                temp = self.right
                self.right = DepthNode(pos, val)
                self.right.right = temp
        elif self.pos > pos:
            temp = DepthNode(pos, val)
            temp.right = self
            self.left = temp
            self.left.depth -= val
    def findRoot(self):
        if self.left == None:return self
        return self.left.findRoot()
    def display(self, list=[]):
        list.append(f'({self.pos}:Depth:{self.depth})')
        if self.right == None: return "->".join(list)
        return self.right.display(list)




def timelineNode(people, count=0, rootNode=None):
    if len(people) <= count: return rootNode
    if len(people) <= 1: return people[0]
    if len(people[count]) < 2: people[count].append(None)
    born, death = people[count]
    if not rootNode:
        rootNode = DepthNode(born, 1)
    else:
        # Create Birth and Root node
        if born:
            rootNode.insertFromRoot(born, 1)
            # Checking for new root
            rootNode = rootNode.findRoot()
        if death:
            rootNode.insertFromRoot(death, -1)
            # Checking for new root
            rootNode = rootNode.findRoot()
    return timelineNode(people, count+1, rootNode)

print(timelineNode(people).display())