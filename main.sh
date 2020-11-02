n, m = map(int, input().split())
weights = input().split()

count = 0

for i in range(n-1):
  for j in range(i+1, n):
    if weights[n] != weights[m]:
      count += 1

print(count)