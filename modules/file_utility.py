# File Utility

def getListFromFile(fileName, delimiter):
    return open(fileName, "r").read().split(delimiter)
