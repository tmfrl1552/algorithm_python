'''
<규칙>
1. 0, 1 숫자를 마주치면 -> x 연산보다는 + 연산을 해야 한다.
2. 그 외의 숫자들은 무조건 x 연산
3. result가 0일 경우에도 그 다음 숫자는 + 연산을 해야 한다.(x연산은 0을 만드므로)
'''
#숫자로 이루어진 문자열 입력받기
s = list(map(int, input()))
#처음 오는 숫자로 초기화
result = s[0]

#두 번째 숫자부터 연산하기
for i in s[1:]:
  if i == 0 or i == 1 or result == 0:
    result += i
  else:
    result *= i

print(result)