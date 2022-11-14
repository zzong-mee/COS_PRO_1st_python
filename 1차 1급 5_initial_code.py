#You may use import as below.
#import math

def solution(n):
    # 여기에 코드를 작성해주세요.
    a = [ [0]* n for _ in range(n)]
    dir = 0 # 방향 0 1 2 3 0 1 2 3 ...
    loop = n # 해당 방향으로 채우는 숫자 개수
    r, c = 0, -1  # 좌표의 초기값
    dr = [0, 1, 0, -1]  # 방향에 대한 r의 변량 x
    dc = [1, 0, -1, 0]  # 방향에 대한 c의 변량 y
    num = 0
    while num < n*n :
        for _ in range(loop) :
            r += dr[dir]
            c += dc[dir]
            num += 1
            a[r][c] = num
            #print(f'[{r}, {c}] = {num}', end=' ')

        dir = (dir + 1) % 4
        if dir % 2 : loop -= 1
    #print(a)
    answer = 0
    for x in range(n):
        answer += a[x][x]   # a[0][0], a[1][1], a[2][2], a[3][3]
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")