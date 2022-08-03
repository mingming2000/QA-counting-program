import re

a = input()
a = re.sub('\n', '', a)
a = a.split(' ' or '.')

print(a)

cnt = 0
for i in range(0, len(a)):
    if(a[i] == '전민경'):
        cnt = cnt + 1

print('답변 개수:', cnt)

