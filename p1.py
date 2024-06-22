# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    # 이곳에 코드를 작성하세요.
    input = sorted(input)

    # 평균과 중앙값을 저장할 변수를 초기화합니다.
    mean = 0
    median = 0

 # 입력 리스트의 합계를 계산하여 평균을 구합니다.
    sum = 0
    for num in input:
        sum += num
    mean = sum / len(input)

 # 정렬된 리스트의 중앙값을 구합니다.
    median = input[int(len(input)/2)]
 
 # 결과를 저장할 리스트를 초기화합니다.
    result = [0,0]
    
 # 결과 리스트에 평균과 중앙값을 저장합니다.
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
