# 문제설명
# n*m 크기의 직사각형
# 각 칸은 (A,B) 형태로 나타내고, 
# A는 북쪽으로부터 떨어진 칸의 개수
# B는 서쪽으로 부터 떨어진 칸의 개수
# 각각의 칸은 육지 or 바다, 바다는 갈 수 없는 칸
# 1. 현 위치에서 왼쪽방향 부터 차례대로 갈곳을 정하고,
# 2. 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재하면, 왼쪽으로 한칸 전진.
# 가보지 않은 칸이 없다면, 또 한번 왼쪽으로 회전
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸 인경우,
# 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1번 단계로 돌아감.
# 이때, 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤
# 입력 : 
# n,m(첫째 줄)
# 현재 있는 칸과 방향(0,1,2,3 순서대로 북동남서) <각각 공백구분 입력>
# 맵 표기(0은 육지, 1은 바다)<공백 구분 입력>
# 출력 : 방문한 칸의 개수

n,m = map(int, input().split(' '))

x, y, d = map(int, input().split(' '))

game_map = []

for i in range(n):
    temp = list(map(int, input().split(' ')))
    game_map.append(temp)

visit_map = game_map # 방문 맵

#0,1,2,3 북동남서
#갈 곳이 있으면, True 반환, 없으면 False 반환
def move(current, direction): # current : 현재 위치 좌표
    if direction == 0:

    elif direction == 1:

    elif direction == 2:

    elif direction == 3:

# 생각한 문제 풀이 방향
# 무한 while 문을 돌려서, move 메소드가 False를 반환할때까지 돌린다.
# move 메소드 내에서, 갈곳이 있는지 없는지 여부는, visit_map을 확인해서 판단.
# visit_map이 cache 메모리 같은 역할을 함.







