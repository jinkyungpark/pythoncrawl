import re

print("[ ] 괄호 : 괄호 안에 들어가는 문자가 들어 있는 패턴")
pattern = re.compile('[abcdefgABCDEFG]')
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))
print()
print("하이픈(-)을 이용하면 알파벳 전체를 나타낼 수 있음")
pattern = re.compile('[a-z]')
print(pattern.search("k1234"))  # <re.Match object; span=(0, 1), match='k'>
print(pattern.search("Z1234"))
print()
print("[a-zA-Z] 으로 표기하면 대소문자를 모두 포함해서 알파벳 전체를 나타낼 수 있음")
pattern = re.compile('[a-zA-Z]')
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 1), match='Z'>
print()
print("[a-zA-Z0-9] 로 표기하면 대소문자를 모두 포함해서 알파벳 전체와 함께 숫자 전체도 나타낼 수 있음")
pattern = re.compile('[a-zA-Z0-9]')
print(pattern.search("1234---"))  # <re.Match object; span=(0, 1), match='1'
print(pattern.search("---------------!@#!@$!$%#%%%#%%@$!$!---"))
print()
print("[ ] 괄호 안에서 [ 바로 뒤에 ^ 을 쓰면 그 뒤에 오는 문자가 아닌 패턴을 찾음")
# 문자를 결국 알파벳, 숫자, 특수문자, whitespace(스페이스, 탭, 엔터등) 로 분류할 수 있으므로
# [^ \t\n\r\f\v] 는 이중에서 whitespace 가 아닌 알파벳, 숫자, 특수문자를 지칭함
pattern = re.compile('[^a-zA-Z0-9]')
# <re.Match object; span=(0, 1), match='-'>
pattern.search("---------------!@#!@$!$%#%%%#%%@$!$!---")
print()
pattern = re.compile('[^ \t\n\r\f\v]')
print(pattern.search("-"))  # <re.Match object; span=(0, 1), match='-'>
print(pattern.search(" "))
print()
print("그러면 한글만? --> [가-힣]")
pattern = re.compile('[가-힣]')
print(pattern.search("안"))   # <re.Match object; span=(0, 1), match='안'>
