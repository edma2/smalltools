# moon.py - retrieves current date and time and calculates today's moon phase
# author: Eugene Ma (edma2)
import datetime

def moon_phase(year, month, day):
        days_since_1900 = 694039.09
        lunar_phase_cycle = 29.53

        if (month < 3):
                year -= 1
                month += 12

        total_days_year = int(365.25 * year)
        total_days_month = int(30.6 * month)
        total_days = total_days_year + total_days_month + day - days_since_1900
        fraction = total_days/lunar_phase_cycle - int(total_days/lunar_phase_cycle)
        # Scale moon phase from 0 to 7
        moon_phase = fraction * 8 + 0.5
        moon_phase = int(moon_phase % 8)

        return moon_phase

now = datetime.datetime.now()
print "Current date and time:", now
phase = moon_phase(now.year, now.month, now.day)
print "Today's moon phase:",

if phase == 0:
        phase = "New moon  |"
elif phase == 1:
        phase = "Waxing crescent  )"
elif phase == 2:
        phase = "First quarter  |)"
elif phase == 3:
        phase = "Waxing gibbous  {)"
elif phase == 4:
        phase = "Full moon!  (|)"
elif phase == 5:
        phase = "Waning gibbous  (}"
elif phase == 6:
        phase = "Third quarter  (|"
elif phase == 7:
        phase = "Waning crescent  ("

print phase
