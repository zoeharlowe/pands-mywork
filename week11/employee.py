# employee.py
# This program creates an employee class that can log time spent on projects.
# Author: Zoe McNamara Harlowe

import datetime as dt
from timesheetentry import *

class Employees:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + ' ' + self.last
    
    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes) 
        self.timesheets.append(timesheetentry)

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

# Test case for Employees class
if __name__ == '__main__':
    test = Employees('Zoe', 'Harlowe')
    print(test)
    assert ('Zoe Harlowe' == str(test))
    test.logminutes('p1', 30)
    test.logminutes('p1', 60)
    mins = test.gettotaltime()
    print(mins)
    assert(mins == 90)

    print('all good')