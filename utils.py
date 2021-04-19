import re

def isPDF(filetype):
    return re.search(r'pdf|PDF', filetype)
