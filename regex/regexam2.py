import re

print("**** 반복 ****")
print("? 사용법 : 최소 0~1")
pattern = re.compile('D?A')  # D가 최소 0~1 이고 A
print(pattern.search("A"))   # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("AA"))  # <re.Match object; span=(0, 1), match='A'>
print()
print("* 사용법 : 0~무한대")
pattern = re.compile('D*A')  # D가 0~무한대 이고 A
print(pattern.search("A"))   # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("DDDDDDDDDDDDDDA"))
# <re.Match object; span=(0, 15), match='DDDDDDDDDDDDDDA'>
print()
pattern = re.compile('AD*A')
print(pattern.search("ADA"))  # <re.Match object; span=(0, 3), match='ADA'>
print(pattern.search("ADDDDDDDDDDDDDDA"))
# <re.Match object; span=(0, 16), match='ADDDDDDDDDDDDDDA'>
print()
print("+ 사용법 : 최소 1~무한대")
pattern = re.compile('D+A')
print(pattern.search("A"))  # None
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA"))
# <re.Match object; span=(0, 29), match='DDDDDDDDDDDDDDDDDDDDDDDDDDDDA'>
