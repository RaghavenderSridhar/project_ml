print("Hello world")

from postal.parser import parse_address
a=parse_address('The Book Club 100-106 Leonard St, Shoreditch, London, Greater London, EC2A 4RH, United Kingdom')
print(a)

from postal.expand import expand_address
b=expand_address('Quatre vingt douze Ave des Champs-Élysées')
print(b)