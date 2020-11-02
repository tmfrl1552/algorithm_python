'''
<풀이>
1. target이 되는 숫자와 그 다음 숫자들을 한 번씩 비교한다.
2. 다르면 count, 같은 숫자면 count 하지 않는다.
'''
n, m = map(int, input().split())
weights = input().split()
count = 0

for i in range(n-1):
  for j in range(i+1, n):
    if weights[i] != weights[j]:
      count += 1

print(count)
