import re

def matching(string, pattern):
    if re.fullmatch(pattern, string):
        return True
    return False

string= input()
pattern= input()
print(matching(string, pattern))


#using regular expressions is one of the easiest ways to check the patterns. using fullmatch function, it will check for the full match of the pattern in the string.