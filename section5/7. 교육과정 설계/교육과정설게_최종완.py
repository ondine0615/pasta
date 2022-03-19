from collections import deque, OrderedDict
import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 첫번째 줄에 반드시 지켜야 하는 순서 (순서중요)이 주어짐
    # 두번째 줄에 N(교육과정의 개수)가 주어짐
    # 그 이후로는 수업과정이 주어짐
    # 출력은 "#n YES/NO"로
    # 그냥 주어진 교육과정 중 필수과정의 순서를 따지면 그만
    
    정답 = []
    
    requiredCourse = list(input())
    N = int(input())
    n = 0
    courses = [deque(input()) for _ in range(N)]

    for course in courses:
        n += 1
        requiredCourseCheck = OrderedDict()

        for c in course:
            requiredCourseCheck[c] = None

        정답_임시 = f'#{n} '
        # 왜 NO만 나오는지 아라보자...
        if requiredCourse == list(requiredCourseCheck.keys()):
            정답_임시 += 'YES'
        else:
            정답_임시 += 'NO'

        정답.append(정답_임시)

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
