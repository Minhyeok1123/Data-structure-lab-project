# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    # 입력 힌트
    leftCount = 0
    rightCount = 0
    result = 0
 # 문자열의 각 문자에 대해 반복합니다.
    for char in input:
        if(char == '('):
            # 여는 괄호의 경우 leftCount를 증가합니다.
            leftCount += 1
        elif(char == ')'):
            # 닫는 괄호의 경우 rigtcount를 증가합니다.
            rightCount += 1

 #닫는 괄호의 개수가 0이 아닌경우 진행합니다.
        if(rightCount != 0):
            if(leftCount != 0):
                # 여는 괄호가 있는 경우, 한 쌍의 괄호를 짝지어 각각 감소시킵니다.
                leftCount -= 1
                rightCount -= 1
            else:
                # 여는 괄호가 없는 경우, 닫는 괄호의 개수를 감소시키고 결과를 증가시킵니다.
                rightCount -= 1
                result += 1

 # 남아있는 여는 괄호의 개수를 결과에 더합니다.
    result += leftCount
   
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")