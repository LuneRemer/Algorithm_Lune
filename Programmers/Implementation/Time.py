# Exercise - Time
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하라
# Input : N (0 <= N <= 23)
# Output : 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수

n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time_str = str(h)+str(m)+str(s)
            if '3' in time_str:
                count += 1

print(count)
