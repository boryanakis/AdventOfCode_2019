polymerFile = open('input', 'r')

polymer = polymerFile.readlines()
polymerString = polymer[0].rstrip()
polymer = list(polymerString)

print(len(polymer))
# print(polymer)

def areSameType(a:str, b:str):
    if a.lower() == b.lower():
        result = True
    else:
        result = False
    return result

def areOppositePolarity(a:str, b:str):
    if a.islower() and b.isupper():
        result = True
    elif a.isupper() and b.islower():
        result = True
    else:
        result = False
    return result

def boom(a:str, b:str):
    if areSameType(a, b) and areOppositePolarity(a, b):
        result = True
    else:
        result = False
    return result

def reduce(polymer:list):
    i = 0
    while True:
        length = len(polymer)
        if i > length -2:break

        if boom(polymer[i], polymer[i+1]):
            del polymer[i]
            del polymer[i]
            # print(polymer)
            i = 0  if i < 100 else i-100

        else:
            i += 1

    # print(''.join(polymer))
    print('* --- RESULT ------------   ',len(polymer))

elements = list(set(polymerString.lower()))
print('num of unit types:',len(elements))


print('polymer length:', len(polymer))
for element in elements:
    forbiddenChars = [element, element.upper()]
    print(forbiddenChars)

    newPolymer = [x for x in polymerString if x not in forbiddenChars]
    print('newPolymer Length:', len(newPolymer))

    reduce(newPolymer)


