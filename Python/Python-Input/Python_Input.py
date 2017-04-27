'''
Created by: Michael Allen
Software:   Python 2.7.10
Version:    1.0
Date:       4/26/2017
Project:    Text Based Pace Calculator
'''

userName = raw_input("Hello! What is your name? ").lower()
print "Welcome " + userName.title() + " to Michael's pace calculator!"

def textBasedPaceCalculator():
    distanceRun = float(raw_input("Please enter a distance in miles: "))
    timeRun = raw_input("Please enter a time run. Format HH:MM:SS: ")
    timeSplit = timeRun.split(':')
    ### Converting hours and minutes to seconds 
    hourSplit = timeSplit[0]
    hourMinutes = int(hourSplit) * 60
    #print hourMinutes
    hourSeconds = int(hourMinutes) * 60
    #print hourSeconds
    minuteSplit = timeSplit[1]
    minutesSeconds = int(minuteSplit) * 60
    #print minutesSeconds
    secondSplit = int(timeSplit[2])
    # print secondSplit
    totalSeconds = hourSeconds + minutesSeconds + secondSplit
    # print totalSeconds
    dividedSeconds = totalSeconds / distanceRun
    #print round(dividedSeconds, 1)
    pacePerMile = dividedSeconds / 60
    pacePerMileRounded = round(pacePerMile, 2)
    pacePerMileRoundedSTR = str(pacePerMileRounded)
    splitPacePerMile = pacePerMileRoundedSTR.split('.')
    minutesPerMile = splitPacePerMile[0]
    remainderPerMile = splitPacePerMile[1]
    secondsPerMile = int(int(remainderPerMile) * 0.6)   

    
    print "Your pace per mile was " + minutesPerMile + " minutes " + str(secondsPerMile) + " seconds." 

textBasedPaceCalculator()
