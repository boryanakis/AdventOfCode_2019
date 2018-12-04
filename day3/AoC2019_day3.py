inFile = open("input", "r")
claims = inFile.readlines()
claims = [l.rstrip() for l in claims]
claims = [claim.replace('#', '') for claim in claims]
claims = [claim.replace(': ', ':') for claim in claims]
claims = [claim.replace(' @ ', ':') for claim in claims]
claims = [claim.replace('x', ',') for claim in claims]


print(claims[:5])

fabricDict = {}

for i in range(2000):
    fabricDict[i] = [0] * 2000

idsDict = {}
for claim in claims:

    ## parse claim
    claimID, start, dims = claim.split(':')
    x, y = start.split(',')
    x = int(x)
    y = int(y)
    width_x, height_y = dims.split(',')
    width_x = int(width_x)
    height_y = int(height_y)

    idsDict[claimID] = width_x * height_y


    for r in range(y, y + height_y):
        for c in range(x, x + width_x):
            if fabricDict[r][c] == 0:
                fabricDict[r][c] = claimID
            elif fabricDict[r][c] == 'X':
                continue
            else:
                fabricDict[r][c] = 'X'

mySum = 0
for r in range(2000):
    mySum += fabricDict[r].count('X')

print(mySum)

for cID in idsDict:
    cID_sum = 0
    for r in range(2000):
        cID_sum += fabricDict[r].count(cID)

    if cID_sum == idsDict[cID]:
        print(cID)