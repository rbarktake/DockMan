import datetime

def getDateString(intDate):
    #return datetime.datetime.fromtimestamp(intDate).strftime('%Y-%m-%d %H:%M:%S')
    return datetime.datetime.fromtimestamp(intDate).strftime('%c')


if __name__ == '__main__':
    print(getDateString(1464529374))
