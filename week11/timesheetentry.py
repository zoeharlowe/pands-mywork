# timesheetentry.py
# This program creates a timesheet entry for a given employee and date.
# Author: Zoe McNamara Harlowe

import datetime as dt

class Timesheetentry:
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration
    def __str__(self):
        return self.project + ': ' + str(self.duration)

# Test case for Timesheetentry class
if __name__ == '__main__':
    ts = dt.datetime(2025, 4, 17, 14, 59)
    test = Timesheetentry('test', ts, 60)
    print(test)

if __name__ == '__main__':
    test = Employees('Zoe', 'Harlowe')
    print(test)
    assert ('Zoe Harlowe' == str(test))
