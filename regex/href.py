import re

href = "http://item.gmarket.co.kr/Item?goodscode=1677762404&amp;ver=637360623912537212"

pattern = re.compile("code=[0-9]+")
print(pattern.findall(href)[0].split("="))  # ['code', '1677762404']
