import sys
from math import sqrt

numbers = []
for line in sys.stdin:
    tokens = line.split()
    for token in tokens:
        numbers.append(sqrt(int(token)))

numbers.reverse()

for number in numbers:
    print(f'{number:.4f}')
