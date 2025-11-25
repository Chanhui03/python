# 보석 도둑
import sys
import heapq
input = sys.stdin.readline

# n = 물품의 수
# k = 버틸 수 있는 무게
n, k = map(int, input().split())
# 보석 
gem = []
for _ in range(n):
    weight, value = map(int, input().split())
    # heapq로 우선순위 큐 구조 사용
    # weight가 작은 값부터 pop, weight가 같으면 value가 작은 값부터 pop
    heapq.heappush(gem, [weight, value])
# 가방
bag = []
for _ in range(k):
    capacity = int(input())
    # capacity가 작은 값부터 pop
    heapq.heappush(bag, capacity)

# 출력용 총 가치
total_value = 0
# 현재 가방이 담을 수 있는 보석들
capable_gem = []

# 가방 수만큼 반복
for _ in range(k):
    # 가방 중 용량이 가장 작은 가방부터 pop
    capacity = heapq.heappop(bag)

    # 보석이 남아 있고, 그중 가장 가벼운 보석(gem[0])이 가방에 들어갈 수 있으면 True
    while gem and (capacity >= gem[0][0]):
        # gem에서 가장 작은 값 pop
        [weight, value] = heapq.heappop(gem)
        # capable_gem heapq에 -value push
        # capable_gem에 들어갈 수 있는 가장 value가 높은 것부터 선택하기 위해 음수로 push
        heapq.heappush(capable_gem, -value)

    # capable_gem에 gem이 들어갔으면 아까 음수로 넣은 value pop하고 음수였으니 마이너스
    if capable_gem:
        total_value -= heapq.heappop(capable_gem)
    elif not gem:
        break

print(total_value)