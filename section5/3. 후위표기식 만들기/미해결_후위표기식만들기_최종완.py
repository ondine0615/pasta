from collections import deque
import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

def convertInfixToPostfix(infix):
    numbers = list()
    operands = list()

    for c in infix:
        if str(c).isnumeric():
            numbers.append(c)
        else:
            operands.append(c)

    return ''.join(numbers)+ ''.join(operands)

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 중위표기식: 연산자가 중간에 옴 예) 3+5
    # 후위표기식: 연산자가 피연산자 뒤에 옴 예) 35+(3+5의 후위표기식)
    # 후위식의 또다른특징으로는 괄호가 붙었다면 식을 분리하는것으로 생각한다.


    정답 = ''
    
    order = input()

    BRACKET = ('(', ')')
    OPERATOR = {'+': 1, '-': 1, '*': 2, '/': 2}

    postfix = []
    operatorsInBracket = [deque()]
    operators = operatorsInBracket[0]
    openedBracket = 0
    recentOperatorPriority = 255 # 최근 연산자의 우선순위

    for char in order:
        if char.isnumeric():
            postfix.append(char)

        elif char in BRACKET:
            if char == '(':
                operatorsInBracket.append(deque())
                openedBracket += 1
            elif char == ')':
                postfix.extend(''.join(operatorsInBracket.pop()))
                openedBracket -= 1
        
        else:
            operatorPriority = OPERATOR[char]
            #char의 우선순위가 그 전것보다 더 높으면
            if operatorPriority > recentOperatorPriority: 
                operatorsInBracket.append(deque())
                openedBracket += 1
            elif operatorPriority < recentOperatorPriority and openedBracket > 0:
                postfix.extend(''.join(operatorsInBracket.pop()))
                openedBracket -= 1

            operatorsInBracket[openedBracket].append(char)
            recentOperatorPriority = operatorPriority
    postfix.extend(operatorsInBracket.pop())

    정답 = ''.join(postfix)

#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{FILE_NO}.txt", 'r').readline().rstrip()

    if 정답 == REAL_ANSWER:
        print("정답")
    else:
        print("오답")
        print(정답)
        print(REAL_ANSWER)
    print(f"실행시간: {END - START}")
