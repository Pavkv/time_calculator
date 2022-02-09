def checkDayM(time):
    t = [time, 0]
    if t[0] < 24:
        return t
    else:
        while t[0] >= 60:
            t[0] = t[0] - 60
            t[1] += 1
    return t


def checkDayH(time):
    t = [time, 0]
    if time < 24:
        return t
    else:
        while t[0] >= 24:
            t[0] = t[0] - 24
            t[1] += 1
    return t


def addDay(*args):
    time = args[0]
    if len(args) > 1:
        day = args[1]
        if 0 < time < 2:
            return ', ' + day + ' (next day)'
        elif time >= 2:
            return ', ' + day + ' ( ' + str(time) + ' days later)'
        else:
            return ', ' + day
    else:
        if 0 < time < 2:
            return ', (next day)'
        elif time >= 2:
            return ', (' + str(time) + ' days later) '
        else:
            return ''


def add_time(*args):
    startTime = args[0].split(' ')
    timeToAdd = args[1]
    dayOfWeek = False
    if len(args) > 2:
        dayOfWeek = args[2]
        dayOfWeek = dayOfWeek.lower()
        dayOfWeek = dayOfWeek[0].upper() + (dayOfWeek[1:])
        days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if startTime[1] == 'AM':
        startTime = [int(startTime[0].split(':')[0]), int(startTime[0].split(':')[1])]
    else:
        startTime = [int(startTime[0].split(':')[0]) + 12, int(startTime[0].split(':')[1])]
    endTime = [startTime[0]+int(timeToAdd.split(':')[0]), startTime[1] + int(timeToAdd.split(':')[1])]
    timeM = checkDayM(endTime[1])
    endTime[0] += timeM[1]
    timeH = checkDayH(endTime[0])
    if timeH[0] == 0:
        timeH[0] = 12
    if 0 < timeH[1] < 2:
        if timeH[0] <= 12 and timeM[0] < 10:
            s = str(timeH[0]) + ':' + '0' + str(timeM[0]) + ' AM'
        elif timeH[0] <= 12 and timeM[0] >= 10:
            s = str(timeH[0]) + ':' + str(timeM[0]) + ' AM'
        elif timeH[0] > 12 and timeM[0] < 10:
            s = str(timeH[0] - 12) + ':' + '0' + str(timeM[0]) + ' PM'
        elif timeH[0] > 12 and timeM[0] >= 10:
            s = str(timeH[0] - 12) + ':' + str(timeM[0]) + ' PM'
    elif timeH[1] >= 2:
        if timeH[0] <= 12 and timeM[0] < 10:
            s = str(timeH[0]) + ':' + '0' + str(timeM[0]) + ' AM'
        elif timeH[0] <= 12 and timeM[0] >= 10:
            s = str(timeH[0]) + ':' + str(timeM[0]) + ' AM'
        elif timeH[0] > 12 and timeM[0] < 10:
            s = str(timeH[0] - 12) + ':' + '0' + str(timeM[0]) + ' PM'
        elif timeH[0] > 12 and timeM[0] >= 10:
            s = str(timeH[0] - 12) + ':' + str(timeM[0]) + ' PM'
    elif timeH[1] == 0:
        if timeH[0] <= 12 and timeM[0] < 10:
            s = str(timeH[0]) + ':' + '0' + str(timeM[0]) + ' AM'
        elif timeH[0] <= 12 and timeM[0] >= 10:
            s = str(timeH[0]) + ':' + str(timeM[0]) + ' AM'
        elif timeH[0] > 12 and timeM[0] < 10:
            s = str(timeH[0] - 12) + ':' + '0' + str(timeM[0]) + ' PM'
        elif timeH[0] > 12 and timeM[0] >= 10:
            s = str(timeH[0] - 12) + ':' + str(timeM[0]) + ' PM'
    if dayOfWeek:
        if timeH[1] > 0:
            d = timeH[1]
            while d > 7:
                d = d - 7
            dayOfWeek = days[days.index(dayOfWeek) + d]
            return s + addDay(timeH[1], dayOfWeek)
        else:
            return s + addDay(timeH[1], dayOfWeek)
    else:
        return s + addDay(timeH[1])


print(add_time("3:00 PM", "3:10"))