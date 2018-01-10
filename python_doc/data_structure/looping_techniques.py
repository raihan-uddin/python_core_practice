knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tick', 'tac', 'toe']):
    print(i, v)

question = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
    print('What is your {0}? It is {1}.'.format(q, a))


for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


import math
raw_data = [52.6, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.80]
print(raw_data)
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


print(filtered_data)