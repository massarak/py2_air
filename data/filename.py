

import datetime

def getFilename():
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S.json")
    #print filename
    return filename
