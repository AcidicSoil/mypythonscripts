import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phoneNumRegex.findall('call me 415-555-1234 tommorrow, or at 415-555-9999 for my office line'))