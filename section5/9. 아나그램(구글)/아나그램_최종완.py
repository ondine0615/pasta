import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 아나그램이란? 단어를 구성하는 알파벳(대소문자 구분)의 종류와 개수가 완전히 동일

    word1 = sys.stdin.readline().rstrip()
    word2 = sys.stdin.readline().rstrip()

    word1Alphabets = dict()
    word2Alphabets = dict()
    
    for alphabet in word1:
        if alphabet in word1Alphabets.keys():
            word1Alphabets[alphabet] += 1
        else:
            word1Alphabets[alphabet] = 1

    for alphabet in word2:
        if alphabet in word2Alphabets.keys():
            word2Alphabets[alphabet] += 1
        else:
            word2Alphabets[alphabet] = 1

    #자바라면 상상할 수 없어보이는 연산자 오버라이딩!
    정답 = ['YES' if word1Alphabets == word2Alphabets else 'NO']


#============================================================================#

    END = time()
    REAL_ANSWER = list(map(lambda s: s.rstrip(), open(pwd + f"\\out{FILE_NO}.txt", 'r').readlines()))

    if 정답 == REAL_ANSWER:
        print("정답")
    else:
        print("오답")
        print(정답)
        print(REAL_ANSWER)
    print(f"실행시간: {END - START}")
