import re

def removeBadChars(string):
    """Haalt verboden tekens uit een string"""
    tmp = re.sub("[{}<>]", "", string)
    return tmp
