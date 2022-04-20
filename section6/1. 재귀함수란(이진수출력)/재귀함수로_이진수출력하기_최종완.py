import sys
from time import time


pwd = __file__[0:__file__.rfind("/")] # 모듈위치

def binary(num, square, answerArray):
    divisor = 2 ** square

    if divisor < 1:
        return

    answerArray.append(str(num // divisor))
    binary(num % divisor, square - 1, answerArray)


for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"/in{FILE_NO}.txt", 'r')

#============================================================================#
    
    N = int(sys.stdin.readline().rstrip())
    정답 = []
    square = 0

    while True:
        left = 2 ** square
        right = 2 ** (square+1)

        if left <= N and N < right:
            break

        square += 1 
    
    binary(N, square, 정답)

    
    정답 = ''.join(정답)

#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"/out{FILE_NO}.txt", 'r').readline()

    if 정답 == REAL_ANSWER:
        print("정답")
    else:
        print(정답)
        print(REAL_ANSWER)
        print("오답")
    print(f"실행시간: {END - START}")
