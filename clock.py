import datetime
import time

class AlarmClock:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.alarm_time = None
        self.alarm_set = False
        self.snooze_count = 0
        self.alarm_duration = 30  # Default duration of the alarm in seconds

    def set_time(self, hours, minutes):
        self.current_time = self.current_time.replace(hour=hours, minute=minutes)

    def set_alarm(self, hours, minutes):
        alarm_time = self.current_time.replace(hour=hours, minute=minutes)

        if alarm_time > self.current_time:
            self.alarm_time = alarm_time
            self.alarm_set = True
        else:
            print("Invalid alarm time. Please set a future time.")

    def is_alarm_time(self):
        return self.alarm_set and self.current_time >= self.alarm_time

    def trigger_alarm(self):
        if self.is_alarm_time():
            print("ALARM! Wake up!")

# Example usage
alarm_clock = AlarmClock()

# Set the current time
current_hours = int(input("Enter current hours: "))
current_minutes = int(input("Enter current minutes: "))
alarm_clock.set_time(current_hours, current_minutes)

# Set the alarm time
alarm_hours = int(input("Enter alarm hours: "))
alarm_minutes = int(input("Enter alarm minutes: "))
alarm_clock.set_alarm(alarm_hours, alarm_minutes)

# Check if it's time for the alarm and trigger it
while not alarm_clock.is_alarm_time():
    print("Current time:", alarm_clock.current_time)
    time.sleep(0.5)  # Wait for 1 second
    alarm_clock.current_time += datetime.timedelta(seconds=1)

alarm_clock.trigger_alarm()
