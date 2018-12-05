import re
import pprint
import statistics


dataFile = open("input", "r")

data = dataFile.readlines()
data = [datum.rstrip() for datum in data]

# print(data[:5])

# make a dictionary
log = []

for datum in data:
    # get the date
    matchObj = re.search(r'\[(.+)\]', datum)
    dateInLog = matchObj.group()
    entry = [dateInLog, datum[19:]]
    log.append(entry)


log = sorted(log, key=lambda x: (x[0]))
pprint.pprint(log[:6])

sleepyGuards = {}
for entry in log:
    timestamp = entry[0]
    event = entry[1]

    match = re.search(r'\d+:\d+', timestamp)
    time = match.group()
    mins = int(time[3:])
    # print(time, mins)

    if 'Guard' in event:
        gmatches = re.search(r'(\w{5}\s#)(\d+)(.+)', event)
        guardID = int(gmatches.group(2))
    elif 'falls asleep' in event:
        startSleep = mins
    elif 'wakes up' in event:
        stopSleep = mins

        if guardID not in sleepyGuards:
            sleepyGuards[guardID] = [0]*60
        for i in range(startSleep, stopSleep):
            sleepyGuards[guardID][i] += 1

guards = list(sleepyGuards.keys())
print('guards_list:', guards)

# --- Total Sleep (Strategy #1)
totalSleep = []
for guard in guards:
    totalSleep.append([guard, sum(sleepyGuards[guard])])

totalSleep = sorted(totalSleep, key=lambda x: (x[1]))
print(totalSleep)
theSleepiestGuard = totalSleep[-1][0]

timesAsleepAtMaxMinute = max(sleepyGuards[theSleepiestGuard])
mostPopularMinute = sleepyGuards[theSleepiestGuard].index(timesAsleepAtMaxMinute)

print(f'guard {theSleepiestGuard} popMinute {mostPopularMinute} freq {timesAsleepAtMaxMinute}')

print(f'result {theSleepiestGuard * mostPopularMinute}')

# --- Strategy #2
freqList = []
for guard in guards:
    freqList.append([guard, max(sleepyGuards[guard])])

freqList = sorted(freqList, key=lambda x: (x[1]))
print(freqList)
theMostConsistentGuard = freqList[-1][0]
mostConsPopMinute = sleepyGuards[theMostConsistentGuard].index(freqList[-1][1])

print(f'guard {theMostConsistentGuard} popMinute {mostConsPopMinute} freq {freqList[-1][1]}')

print(f'result {theMostConsistentGuard * mostConsPopMinute}')
