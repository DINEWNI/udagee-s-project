key = True
owner = True
theif = False
police = True
if (key or owner) and( not theif or police):
    print("Door unlocked .you are welcome!")
else:
    print("Door closed. Alarm ringing.")
