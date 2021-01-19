import re

with open('nomes.txt') as file:
    lines = file.read()
    pattern = r'[\w]+ Silva'
    regex = re.findall(pattern, lines)
    print(regex)
    regex = re.search(pattern,lines)
    print(regex.group())
    regex = re.match(pattern, lines)
    print(regex.group)