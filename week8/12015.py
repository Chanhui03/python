# 가장 긴 증가하는 부분 수열 2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [0]

for a in arr:
    # lis의 끝값보다 현재 a가 클 때
    if lis[-1] < a:
        lis.append(a)
    # lis의 끝값보다 현재 a가 작을 때
    else: # lis[-1] >= a:
        # lis의 시작값과 끝값
        left = 0
        right = len(lis)

        # left가 right을 만나거나 넘으면 종료
        while left < right:
            # 중간값 찾기
            mid = (right + left) // 2
            # lis의 중간값보다 현재 a값이 클 때
            if lis[mid] < a:
                # left를 (중간값 + 1)로 = 뒷부분만 보겠다
                left = mid + 1
            # lis의 중간값보다 현재 a값이 작을 때
            else: # lis[mid] >= a:
                # right을 mid로 (길이 축소) = 앞부분만 보겠다
                right = mid
        # while문 종료 = 현재 a값의 위치 찾음
        lis[right] = a

# lis[0] = 0이기 때문에 길이에서 1 뺌
print(len(lis) - 1)