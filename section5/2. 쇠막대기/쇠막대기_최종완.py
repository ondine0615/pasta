from collections import deque
import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 쇠막대기
    # 쇠막대기를 레이저 컷팅할거다 
    # '(' <- 막대 시작 ')' <- 막대 끝, '()'시 레이저 존재
    # 쇠막대기 스택은 맨 밑이 제일 길고 그 위로 갈수록 짧아짐
    # 레이저는 그 어떤 쇠막대기의 끝점과 겹치지 않음
    # 잘린 쇠막대기의 총 개수는?

    정답 = 0
    
    order = input()

    temp = deque(maxlen=len(order))
    lastEncounteredChar = ''
    pipe = 0
    for char in order:
        # 1. 들어온 char가 '('시
        if char == '(':
            pipe += 1
            temp.append(char)
        # 2. 들어온 char가 ')'시 
        elif char == ')':
            lastChar = temp.pop()
            pipe -= 1

            if lastEncounteredChar == '(': # 레이저임
                #레이저컷팅 실시!
                정답 += pipe
            else: #어떤 파이프의 끝을 나타냄
                정답 += 1
        lastEncounteredChar = char

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
