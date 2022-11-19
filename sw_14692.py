n = int(input())
turn = [int(input()) for _ in range(n)]
results = []
cnt = 0
for i in turn:
    cnt += 1
    if i % 2 == 0:
        results.append(f"#{cnt} Alice")
    elif i % 2 == 1:
        results.append(f"#{cnt} Bob")

for result in results:
    print(result)