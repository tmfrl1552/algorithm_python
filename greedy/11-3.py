'''
1. 모두 0으로 바뀔 때 vs 모두 1로 바뀔 때 수 중 더 적은 수 출력
2. 첫 번째 원소에 대해서 바뀔 수 있는 숫자로 카운트
3. 두 번째 원소부터 0->1, 1->0으로 바뀌는 구간에서의 후에 바뀌는 수로 카운트
ex. 0->1이면 1측 카운트, 1->0이면 0 측 카운트
'''
s = list(map(int, input()))
count0 = 0
count1 = 0

if s[0] == 1:
  count0 += 1
else:
  count1 += 1

for i in range(len(s) - 1):
  if s[i] != s[i+1]:
    if s[i+1] == 1:
      count0 += 1
    else:
      count1 += 1

print(min(count0, count1))