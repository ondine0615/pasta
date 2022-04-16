import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 첫번째줄에 쓸 단어의 개수 N
    # 두번째줄부터 ~ N+1 번째 줄 까지 써야할 단어
    # N+2 ~ 는 시에 쓰인 N-1개의 단어
    # 안 쓴 단어는 항상 하나

    requiredWords = set()
    usedWords = set()

    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        requiredWords.add(sys.stdin.readline().rstrip())
    
    for _ in range(N-1):
        usedWords.add(sys.stdin.readline().rstrip())

    #자바라면 상상할 수 없어보이는 연산자 오버라이딩!
    정답 = list(requiredWords - usedWords)


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
