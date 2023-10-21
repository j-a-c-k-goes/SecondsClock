"""
    @module SecondsClock.py
    @date 2023 10 21
    @author jackjackjack
    @desc Class module to display current time in seconds.
"""
from datetime import datetime
class SecondsClock:
    clocks_created = 0
    total_seconds_in_day = 24 * 60 * 60
    def __init__(self):
        self.current_hour = datetime.now().hour
        self.current_minute = datetime.now().minute
        self.current_second = datetime.now().second
        self.total_time_in_seconds = None
    def getCurrentHour(self):
        return self.current_hour
    def getCurrentMinute(self):
        return self.current_minute
    def getCurrentSeconds(self):
        return self.current_second
    def setCurrentHour(self, new_hour):
        self.current_hour = new_hour
    def setCurrentMinute(self, new_minute):
        self.current_minute = new_minute
    def setCurrentSecond(self, new_second):
        self.current_second = new_second
    def setTotalTime(self, new_total_time):
        self.total_time_in_seconds = new_total_time
    def convertHoursToSeconds(self, hours_to_convert:int):
        converted_hours = int(hours_to_convert * 60 * 60)
        return converted_hours
    def convertMinutesToSeconds(self, minutes_to_convert:int):
        converted_minutes = int(minutes_to_convert * 60)
        return converted_minutes
    def sumTimeAsSeconds(self):
        time_in_seconds = ( self.convertHoursToSeconds( self.getCurrentHour() ) ) + ( self.convertMinutesToSeconds( self.getCurrentMinute() ) ) + ( self.getCurrentSeconds() )
        return time_in_seconds
    def calcRemainingSeconds(self):
        return self.total_seconds_in_day - self.sumTimeAsSeconds()
    def displayTime(self):
        print( f"""SE\t{self.sumTimeAsSeconds()}\nSR\t{self.calcRemainingSeconds()}""" )
        print( f"""\t{ round( ((self.sumTimeAsSeconds() / self.calcRemainingSeconds()) *100),2 ) }% Complete""")
    def update(self):
        self.setCurrentHour( datetime.now().hour )
        self.setCurrentMinute( datetime.now().minute )
        self.setCurrentSecond( datetime.now().second )
        self.setTotalTime( self.sumTimeAsSeconds() )