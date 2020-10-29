'''
1. 배열 중 제일 큰 수와 두 번째로 큰 수를 찾아낸다.
2. 묶음 단위(큰수 k번 + 두 번째 큰수 1번)를 (m//k)번으로 곱하기
3. m%k(나머지)가 있으면 그 만큼 제일 큰 수 곱해서 결과에 더해주기
'''

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
max1, max2 = arr[0], arr[1]

result = ((max1 * k) + max2) * (m//(k+1))
if m%(k+1) != 0:
  result += max1 * (m%k)

print(result)