import re
import pprint
import datetime


dataFile = open("input", "r")

data = dataFile.readlines()
data = [datum.rstrip() for datum in data]

print(data[:5])

# make a dictionary
logDict = {}

for datum in data:
    # get the date
    matchObj = re.search(r'1518-\d+-\d+', datum)
    dateInLog = matchObj.group()
    if dateInLog not in logDict:
        logDict[dateInLog] = {}

    matchObj = re.search(r'\d+:\d+', datum)
    time = matchObj.group()
    print(time)

    log_entry = datum[19:]
    print(log_entry)
    logDict[dateInLog][time] = log_entry

pprint.pprint(logDict)

print(logDict.keys())
dictKeys = list(logDict.keys())
"%Y-%m-%d"
sorted_dates = sorted(logDict.keys(), key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
finalDict = {}

outFile = open('sleepy.csv', 'w')
for sortedDate in sorted_dates:
    timesKeys = logDict[sortedDate].keys()
    sorted_times = sorted(logDict[sortedDate].keys(), key=lambda x: datetime.datetime.strptime(x, "%H:%M"))
    # print(sorted_times)
    for sortedTime in sorted_times:
        info = logDict[sortedDate][sortedTime]
        if 'Guard' in info:
            info = info.replace('Guard #','')
            info = info.replace(' begins shift', '')
            currentGuard = info
        elif 'falls asleep' in info:
            startSleep = int(sortedTime[3:])
        elif 'wakes up' in info:
            stopSleep = int(sortedTime[3:])
            # print(currentGuard)
            currentLine = ['.']*60
            for i in range(startSleep, stopSleep+1):
                currentLine[i] = '#'
            lineOut = [currentGuard]
            lineOut.extend(currentLine)
            outFile.write(','.join(lineOut)+'\n')


