# 문제 설명
# n*n 크기의 정사각형 공간에서 여행가는 (1,1)에서 시작 
# 가장 오른쪽 아래 좌표는 (n,n)
# 여행가는 상하좌우로만 한칸씩 이동할 수 있다.
# 정사각형 공간을 벗어나는 움직임은 무시된다.
# 입력은 n 과 L,R,U,D 로 주어진다.

n = int(input())
plan = str(input())

# 2사분면과 동일

init_x = 1
init_y = 1

plan_dict = {}
plan_dict['L'] = (-1,0)
plan_dict['R'] = (1,0)
plan_dict['U'] = (0,-1)
plan_dict['D'] = (0,1)

for move in plan:
    temp_x = init_x+plan_dict[move][0]
    temp_y = init_y+plan_dict[move][1]
    if temp_x>0 and temp_x<=n and temp_y>0 and temp_y<=n:
        init_x = temp_x
        init_y = temp_y

# 수학에서의 x,y와 반대로 출력
print(str(init_y) + " " + str(init_x))
    


