def add_time(start, duration, weekday=''):
  startPieces = start.split()
  AMpm= startPieces[1]
  startTime= startPieces[0]
  startHour= int(startTime.split(':')[0])
  startMin= int(startTime.split(':')[1])
  week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  durHours= int(duration.split(':')[0])
  durmins= int(duration.split(':')[1])
  
  #convert to 24h
  if AMpm == 'PM':
    startHour += 12
  newTimeHour= int(startHour + durHours)
  newTimeMin= int(startMin + durmins)

  #calculate days
  dayCount=0
  if newTimeMin >= 60:
    addDays= int((newTimeMin-(newTimeMin % 60))/60)
    newTimeMin= newTimeMin % 60
    newTimeHour += addDays
  while newTimeHour >=24:
    newTimeHour -= 24
    dayCount += 1
  if dayCount < 1:
    days = ''
  elif dayCount== 1:
    days = ' (next day)'
  else:
    days = ' (' + str(dayCount) + ' days later)'

  #minute format
  if newTimeMin < 10:
    newTimeMin = '0' + str(newTimeMin)
  else:
    newTimeMin = str(newTimeMin)

  #determine weekday
  if weekday != '':
    weekday = weekday.lower().capitalize()
    index = week.index(weekday)
    newIndex = index + dayCount
    if newIndex > (len(week)-1):
      while newIndex > (len(week)-1):
        newIndex -= 7
    weekday = ', ' + week[newIndex]
    
  #cpnvert to 12h
  if newTimeHour == 12:
    newAMpm = ' PM'
  elif newTimeHour >12:
    newTimeHour = newTimeHour - 12
    newAMpm = ' PM'
  elif newTimeHour == 0:
    newTimeHour = 12
    newAMpm = ' AM'
  else:
    newAMpm = ' AM'

  new_time = str(newTimeHour) + ':' + newTimeMin + newAMpm + weekday + days
  
  return new_time