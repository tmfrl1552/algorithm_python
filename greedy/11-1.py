'''
* 모험을 떠날 수 있는 최소 인원이 충족되면 바로 모험을 보낸다. *
1. 공포도가 적은 순으로 오름차순 정렬
2. 공포도에 인원을 맞춰 보내야 하므로 공포도에 인원이 맞춰지는 순간 모험 보내기
'''

n = int(input())
adv = list(map(int, input().split()))
# 모험가들 공포도 기준으로 오름차순 정렬
adv.sort()

# 공포도, 모인 인원, 떠난 그룹수(count) 초기화
horror, people, count= 0, 0, 0

for i in adv:
  # 만약 기존 공포도와 다르면 업데이트
  if horror != i:
    horror = i
  # 모인 인원에 1명 추가
  people += 1

  # 공포도와 모인 인원 수가 같다면 모험 떠나기
  if horror == people:
    count += 1
    people = 0


print(count)