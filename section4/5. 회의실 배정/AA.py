# (중요!) 여기서는 회의가 끝나는 시간으로 정렬해야한다

# 패배 요인
# 최대한 짧은 시간으로 생각함...

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

#회의 시간에 따라 정렬함
ls.sort(key = lambda x: x[0])
ls.sort(key = lambda x: x[1])

reserved = [ls[0]]
ans = 1

for idx in range(1, len(ls)):
    start = ls[idx][0]
    end = ls[idx][1]
    if start >= reserved[ans-1][1]:
        ans += 1
        reserved.append([start, end])

print(ans)