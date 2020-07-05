import re

print("{n} 사용법")
pattern = re.compile('AD{2}A')
print(pattern.search("ADA"))
print(pattern.search("ADDA"))
print(pattern.search("ADDDA"))
print()
print("{n,m} 사용법")
pattern = re.compile('AD{2,6}A')
print(pattern.search("ADDA"))
print(pattern.search("ADDDA"))
print(pattern.search("ADDDDDDA"))
