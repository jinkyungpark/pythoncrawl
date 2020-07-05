import re

# 찾고 바꾸기 : sub
print()
print("**** 찾고 바꾸기 ****")
pattern = re.compile('D[.]A')
string = "DDA D1A DDA DA"
result = re.sub('D.A', 'Dave', string) 
print(result)   # Dave Dave Dave DA

# match 와 search 함수
# match : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴
# search : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 리턴
pattern = re.compile('[a-z]+')
matched = pattern.match('Dave')
print("matched : ", matched)  # None
searched = pattern.search("Dave")
print("serched : ", searched)  # <re.Match object; span=(1, 4), match='ave'>

# findall 함수: 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴함
pattern = re.compile('[a-z]+')
findalled = pattern.findall('Game of Life in Python')
print(findalled)   # ['ame', 'of', 'ife', 'in', 'ython']
pattern2 = re.compile('[A-Za-z]+')
findalled2 = pattern2.findall('Game of Life in Python')
print(findalled2)   # ['Game', 'of', 'Life', 'in', 'Python']

# 예제
print()
pattern = re.compile('[a-z]+')
findalled = pattern.findall('GAME')
if len(findalled) > 0:
    print("정규표현식에 맞는 문자열이 존재함")
else:
    print("정규표현식에 맞는 문자열이 존재하지 않음")   # 정규표현식에 맞는 문자열이 존재하지 않음

# split 함수: 찾은 정규표현식 패턴 문자열을 기준으로 문자열을 분리
print()
pattern2 = re.compile(':')
splited = pattern2.split('python:java')
print(splited)
