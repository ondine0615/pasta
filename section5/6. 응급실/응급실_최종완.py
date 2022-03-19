from collections import deque
import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 대기목록에서 첫번째 환자(A)를 꺼내고 우선순위 파악
    # 그 환자보다 우선순위가 높은(>) 환자(B)가 있다면 -> A를 맨 뒤로 보내고 B를 진료(꺼냄)
    # 없다면 A를 진료(꺼냄)
    # 위험도는 50~100, N = 환자수 (5~100)
    # 대기목록상 M(0~N-1)번째 환자는 몇번째에 진료를 받는가?
    
    정답 = -1
    
    N, M = map(int, input().split())
    priority = deque(map(int,input().split()))
    patientID = deque(range(0, N))

    nth = 0
    while len(priority) > 1:
        currentPatientPriority = priority.popleft()
        currentPatientID = patientID.popleft()

        for idx in range(len(priority)):
            otherPatientPriority = priority[idx]
            otherPatientID = patientID[idx]

            # 현재 뽑힌 환자의 우선순위가 다른 환자보다 낮다면
            if otherPatientPriority > currentPatientPriority:
                priority.append(currentPatientPriority)
                patientID.append(currentPatientID)
                break
        else:
            nth += 1
            if M == currentPatientID:
                정답 = nth
                break


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
