from datetime import datetime, timedelta
from time import sleep


def formattimediff(outputMode):
    deltaTime = datetime.now()

    try: 
        now 
    except NameError: 
        now = datetime.now()
        time_diff = deltaTime - now
        newCreated = "Y"
        print("Process Started: ", now)
    else: 
        time_diff = deltaTime - now

    # Extract hours, minutes, and seconds
    hours, remainder = divmod(time_diff.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    # Round the seconds
    seconds = round(seconds)

    # Format the output
    FTDiff= f"{int(hours)} Hours, {int(minutes)} Minutes, {int(seconds)} Seconds"

    if outputMode == "delta":
        print("Time elapsed:", FTDiff)

    elif outputMode == "completion":
        print("Process completed in:", FTDiff)

    else:
        print("Runtime:", FTDiff)


#now = datetime.now()
#print("Process started at:", now)
formattimediff("delta")

sleep(5)

formattimediff("delta")

sleep(5)

formattimediff("delta")

sleep(5)

formattimediff("delta")

sleep(5)

formattimediff("fart")

sleep(5)

formattimediff("completion")