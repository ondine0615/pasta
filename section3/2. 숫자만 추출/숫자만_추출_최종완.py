import re
import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#

    정답 = []
    word = input()

    pattern = re.compile(r"[0-9]+")
    matches = list(map(int, pattern.findall(word)))
    numString = ""
    for w in matches:
        numString += str(w)
    number = int(numString)
    
    divisor = set()

    for i in range(1, number + 1):
        if number % i == 0:
            divisor.add(i)

    정답.append(number)
    정답.append(len(divisor))

#============================================================================#

    END = time()
    realAnswer = open(pwd + f"\\out{file_no}.txt", 'r').readlines()
    for index in range(0,len(realAnswer)):
        if str(정답[index]).strip() != str(realAnswer[index]).strip():
            print(정답)
            print(realAnswer)
            print("오답")
            break
    else:
        print("정답")

    print(f"실행시간: {END - START}")
