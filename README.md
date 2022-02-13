# 220122

## 인프런 파이썬 알고리즘 문제풀이 (코딩테스트 대비)
- https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8

  - 하루 1문제씩 풀고 문제 폴더에 '자기 이름.확장자'로 커밋
  - 주말에 GoogleMeet으로 모여서 정답 코드의 이해와 새로운 접근 방식 공유

###################################################

#### 그냥 혹시 몰라 써놓는 input 방법
import sys  
sys.stdin=open('input.txt','r') 을 한 뒤에,  (참고로 이 방법이 interactive shell에서는 안먹힘, 쥬피터에서는 못쓴다는 것)

![image](https://user-images.githubusercontent.com/76681523/150662324-6cb1f033-59c0-4268-9387-39b4935d0844.png)

- (1),(2) map(함수, 리스트or튜플) : 첫번째 인자에 있는 함수를 기준으로 두번쨰 인자 내에 있는 원소들을 하나씩 집어넣어 함수를 수행하는 것
  - 작동원리를 풀어서 생각해 보면,
  - for i in range(len(a)):
    - a[i]=int(a[i])
  - 로 정도로 볼 수 있는 것 같음.
  
 - (3) 리스트화 하는 것

저번 봉우리 문제에서 처럼 2차원 리스트로 만들고 싶으면, 

a = [list(map(int,input().split())) for _ in range(n)] 
으로 만들면 되는데,   

만약 문제에서 주어진 숫자가 

2   
1 2 3 4 5    
6 7 8 9 10  

라고 할 때,

n=int(input())   
a = [list(map(int,input().split())) for _ in range(n)]    
print(n)    
print(a[0])    
을 요구한다면,         

2     
[1,2,3,4,5] 가 출력됌.  

즉, 2차원 리스트에서는 한줄의 리스트 자체가 하나의 원소로 취급 되는 것이라고 생각할 수 있는 것 같음.
