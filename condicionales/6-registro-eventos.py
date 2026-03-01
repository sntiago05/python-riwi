class MinimunAgeExeception(Exception):
    pass


class OccupationExeception(Exception):
    pass


events = {
    # minimun age - actual occupation - max occupation
    "rock concert": [16, 0, 30],
    "finance event": [18, 99, 100],
    "mental health": [14, 30, 40],
    "anonymous alcoholics": [18, 10, 25],
}

event_list = list(events.keys())
while True:
    age = int(input("enter your age: "))
    print("We have the following events available:", "\n--> ".join(event_list))
    print("<-- Type 0 to exit -->")
    event_choose = input("Enter your choice: ").lower().strip()
    if event_choose == "0":
        break
    if event_choose in events:
        event = events[event_choose]
        try:
            if age < event[0]:
                raise MinimunAgeExeception(
                    f"You required at minimun {event[0]} Years old to enter at this event"
                )
            if event[1] >= event[2]:
                raise OccupationExeception("The event is full!")
            print(f"Welcome to {event_choose.title()}")
            event[1] += 1
            print(f"Current attendance: {event[1]}/{event[2]}")
        except (MinimunAgeExeception, OccupationExeception) as e:
            print(e)
            continue

    else:
        print("We dont have that event in our list rigth now")
