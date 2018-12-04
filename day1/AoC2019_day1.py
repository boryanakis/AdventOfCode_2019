import sys
import itertools



data = open("input", "r")

numsList = data.readlines()
numsList = [int(x.rstrip()) for x in numsList]
print(f"sample numList: {numsList[:20]}")

sum1 = sum(numsList)
print(f"sum1: {sum1}")
ssum = 0
myList = [0]

for element in itertools.cycle(numsList):
    # print(element)

    ssum += element
    if ssum in myList:
        print(ssum)
        sys.exit()
    else:
        myList.append(ssum)
