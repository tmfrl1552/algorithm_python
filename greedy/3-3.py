n, m = map(int, input().split())
a = -9999

for i in range(n):
  data = list(map(int, input().split()))
  if a < min(data):
    a = min(data)

print(a)

'''
1. 각 행의 작은 수들 중에서도 큰 수를 저장할 a를 초기화한다.
2. 각 행의 값을 입력받을 때 마다 가장 작은 min 값을 확인하여 a값과 비교한다.
3. a값 보다 크다면 a값을 업데이트한다.
'''