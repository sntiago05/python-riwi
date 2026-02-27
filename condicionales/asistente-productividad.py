from datetime import datetime as dt

actions = ["Relax", "Work", "Eexercise"]
now = dt.now()
hour = now.hour
day = now.weekday()

schedules = {
    "laboral": [(0, 8, 0), (8, 17, 1), (17, 19, 2), (19, 23, 0)],
    "no_laboral": [(0, 10, 0), (10, 15, 2), (15, 23, 0)],
}
day_type = "laboral" if day <= 5 else "no_laboral"
action_index = None
for start, end, index in schedules[day_type]:
    if start <= hour < end:
        action_index = index
        break
if action_index is not None:
    print(f"You should: {actions[action_index]}")
        

