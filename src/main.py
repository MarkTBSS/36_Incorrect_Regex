import re

regexString = '.*+'

try:
    re.compile(regexString)
    print("True")
except re.error:
    print("False")