# 스도쿠

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
empty_positions = []

# 빈 칸 위치 저장
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty_positions.append((i, j))

# 특정 숫자를 해당 위치에 넣어도 되는지 확인
def is_valid(row, col, num):
    # 행, 열, 3x3 박스 검사
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
    # 3x3 박스 검사
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# 백트래킹으로 스도쿠 풀이
def solve(index):
    # 모든 빈 칸을 채웠다면 출력 후 종료
    if index == len(empty_positions):
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit(0)
    
    # 현재 빈 칸 위치
    row, col = empty_positions[index]

    # 1부터 9까지 숫자 시도
    for num in range(1, 10):
        if is_valid(row, col, num):
            # 해당 숫자 넣기
            board[row][col] = num
            # 다음 빈 칸으로 이동
            solve(index + 1)
            # 백트래킹: 원래대로 되돌리기
            board[row][col] = 0

solve(0)
