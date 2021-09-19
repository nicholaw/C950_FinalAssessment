"""
Represents time of day in a simple 24-hour clock format to minute percision;
Allows comparison between two times such as A.isAfter(B)
"""

class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0

    def of(strTime):
        time = Time()
        strTime = "".join(strTime.split())
        if(len(strTime) != 5):
            return time
        else:
            hour = int("" + strTime[0] + strTime[1])
            if(hour < 24 and hour >= 0):
                time.hour = hour
            minute = int("" + strTime[3] + strTime[4])
            if(minute < 60 and minute >= 0):
                time.minute = minute
        return time

    def isBefore(self, timeB):
        if(self.hour > timeB.hour):
            return False
        elif(self.hour < timeB.hour):
            return True
        else:
            if(self.minute >= timeB.minute):
                return False
            else:
                return True

    def isAfter(self, timeB):
        if(self.hour > timeB.hour):
            return True
        elif(self.hour < timeB.hour):
            return False
        else:
            if(self.minute > timeB.minute):
                return True
            else:
                return False
    
    def add_minutes(self, minutes):
        if(minutes < 0):
            return
        hours = 0
        while(minutes >= 60):
            hours = hours + 1
            minutes = minutes - 60
        self.minute = self.minute + minutes
        if(self.minute >= 60):
            self.minute = self.minute - 60
            hours = hours + 1
        self.hour = self.hour + hours
        if(self.hour >= 24):
            self.hour = self.hour - 24

    def __eq__(self, timeB):
        return (self.hour == timeB.hour and self.minute == timeB.minute)

    def __str__(self):
        string = ""
        if(self.hour < 10):
            string = string + "0" + str(self.hour)
        else:
            string = string + str(self.hour)
        string = string + ":"
        if(self.minute < 10):
            string = string + "0" + str(self.minute)
        else:
            string = string + str(self.minute)
        return string