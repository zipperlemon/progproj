import re

def removeBadChars(string):
    tmp = re.sub("[{}<>]", "", string)
    return tmp
