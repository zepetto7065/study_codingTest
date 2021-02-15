<완전탐색>

- 가능한 방법을 전부 만들어 보는 알고리즘

<순열과 조합>

from itertools import permutations, combinations

chars = ['A', 'B', 'C']

p = list(permutations(chars, 2))  # 순열
print(p)
>> [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

c = list(combinations(chars, 2))  # 조합
print(c)
>> [('A', 'B'), ('A', 'C'), ('B', 'C')]


