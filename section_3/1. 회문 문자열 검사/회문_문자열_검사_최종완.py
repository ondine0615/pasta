import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#

    정답 = []
    N = int(input())
    words = [input() for _ in range(0,N)]

    for idx in range(0, len(words)):
        word = words[idx].lower()
        wordLength = len(word)
        maxIndex = wordLength - 1
        middleIndex = maxIndex // 2

        #회문 문자열 검사 :: 길이가 짝수일 때
        if wordLength % 2 == 0:
            for i in range(0, middleIndex + 1):
                if word[i] != word[maxIndex - i]:
                    정답.append(f"#{idx+1} NO\n")
                    break
            else:
                정답.append(f"#{idx+1} YES\n")
        else:  # 길이가 홀수일 때
            for i in range(0, middleIndex):
                if word[i] != word[maxIndex- i]:
                    정답.append(f"#{idx+1} NO\n")
                    break
            else:
                정답.append(f"#{idx+1} YES\n")
        
        


#============================================================================#

    END = time()
    realAnswer = open(pwd + f"\\out{file_no}.txt", 'r').readlines()
    for index in range(0,len(realAnswer)):
        if 정답[index].strip() != realAnswer[index].strip():
            print(정답)
            print(realAnswer)
            print("오답")
            break
    else:
        print("정답")

    print(f"실행시간: {END - START}")
