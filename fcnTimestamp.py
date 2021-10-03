# function to create timestamp and/or sync trigger
from datetime import datetime

def fcnTimestamp():

    triggerMillisecond = 1_000_000

    # loop shall run as long, as the time stamp has a to high ms value. 
    # that way, the loop will break e.g. in a window x.000 - x.100 s or more narrow
    # afterwards a scan can be triggered in main
    while triggerMillisecond > 0.010:
        # create timestamp
        time = datetime.now()
        timestamp = datetime.timestamp(time)

        # reduce to only ms
        triggerMillisecond = round(timestamp-int(timestamp),3)

    # IF the timestamp had less than 10ms, the loop has broken here

    return(timestamp)

