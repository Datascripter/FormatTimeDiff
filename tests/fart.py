from datetime import datetime, timedelta
from time import sleep

deltaTime = datetime.now()
now = datetime.now()

print(now)

try: 
    now 
except NameError: 
    now = datetime.now()
    time_diff = deltaTime - now
    print("Created new now:", now)
else: 
    time_diff = deltaTime - now
    print("Already Existed:", now)

del now

try: 
    now 
except NameError: 
    now = datetime.now()
    time_diff = deltaTime - now
    print("Created new now:", now)
else: 
    time_diff = deltaTime - now
    print("Already Existed:", now)