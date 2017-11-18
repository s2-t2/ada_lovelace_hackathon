from icalendar import *
import io

def calculate_time(event):
    return event['DTSTART'].dt


def lecturize(event):
    return event['SUMMARY']


g = io.open('in_class_remainder.ics', mode='r', encoding="utf-8")
gcal = Calendar.from_ical(g.read())

sessions = [(lecturize(e), calculate_time(e)) for e in gcal.walk('vevent')]

print sessions

g.close()
