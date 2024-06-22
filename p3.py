# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.

    result = 0
    isSuccess = True
    while(isSuccess):
        isSuccess = False
        queue = [] #방문 대기열
        queue.append((bear_x,bear_y, 0))  # BFS를 위한 큐 초기화

        visited = [[0] * N for _ in range(N)] #방문 여부 체크리스트
        xp = [-1,0,0,1]
        yp = [0,-1,1,0]

        while queue: 
            x, y, count = queue.pop(0) # 현재 방문할 노드를 큐에서 꺼냅니다.
            visited[x][y] = 1 # 현재위치를 방문한 것으로 표시합니다.
            if(forest[x][y] != 0 and bear_size > forest[x][y]):
                bear_x = x
                bear_y = y
                result += count
                forest[x][y] = 0

                honeycomb_count += 1
                if(honeycomb_count == bear_size):
                    bear_size += 1
                    honeycomb_count = 0
                isSuccess = True
                break

            for i in range(4):  # 현재 노드와 연결된 모든 노드를 탐색합니다.
                nextX = x + xp[i]
                nextY = y + yp[i]
                if (nextX < 0 or nextX >= N or nextY < 0 or nextY >=N):
                    continue
                if(bear_size < forest[nextX][nextY]):
                    continue
                if visited[nextX][nextY] == 0: #방문하지 않은 노드라면 큐에 추가하고 방문여부를 True로 변경합니다.
                    queue.append((nextX, nextY, count + 1))
                    visited[nextX][nextY] = 1

            
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")
