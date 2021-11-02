# 문제설명 생략
# 체스판(8*8)위에서 나이트가 나이트 이동규칙대로 움직임
# 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력
# 열 위치는 a~h로 대체, 행은 1~8.
# 입력 형식은 a1, c2 같이 주어짐. 

init = str(input())

init_x = init[0]
init_y = int(init[1])

# 그냥 체스판을 2사분면이라고 생각해도 무방

dict = {}
dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4
dict['e'] = 5
dict['f'] = 6
dict['g'] = 7
dict['h'] = 8

init_x = dict[init_x]

def possible_location(init_row, init_col):
    possible = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,-1),(-2,1)]
    count = 0   

    for row, col in possible:
        temp_row = init_row
        temp_col = init_col
        temp_row += row
        temp_col += col
        if temp_row>0 and temp_col>0 and temp_row<9 and temp_col<9:
            count += 1            
    return count

print(possible_location(init_x,init_y))
