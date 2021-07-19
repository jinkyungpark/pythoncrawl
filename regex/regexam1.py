import re

pattern = re.compile('D.A')

# 패턴이 매칭되는지 여부 확인하기 : search
result = pattern.search('DAA')
print(result)  # <re.Match object; span=(0, 3), match='DAA'>
print(result.start(),result.end(),result.group())  # 0 3 DAA

result = re.search(r'D.A','D1A')
print(result)  # <re.Match object; span=(0, 3), match='D1A'>

result = pattern.search('D00A')
print(result)  # None

result = re.search(r'D.A','DA')
print(result)  # None

result = pattern.search('d0A')
print(result)  # None

result = pattern.search('d0A D1A 0111')
print(result)  # <re.Match object; span=(4, 7), match='D1A'>

