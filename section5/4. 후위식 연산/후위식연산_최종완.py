import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 후위연산식이 주어지면 연산한 결과를 출력한다.
    
    정답 = 0
    
    order = input()
    stack = []

    for char in order:
        if char.isnumeric():
            stack.append(char)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            res = 0

            if char == "+":
                res = first + second
            elif char == "*" :
                res = first * second
            elif char == "-":
                res = first - second
            elif char == "/":
                res = first / second
            
            stack.append(res)

    정답 = stack.pop()


#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{FILE_NO}.txt", 'r').readline().rstrip()

    if int(정답) == int(REAL_ANSWER):
        print("정답")
    else:
        print("오답")
        print(정답)
        print(REAL_ANSWER)
    print(f"실행시간: {END - START}")
