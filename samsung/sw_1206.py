results = []
for _ in range(10):
    n = int(input())
    building = list(map(int, input().split()))
    nice_view = 0
    for p in range(2, n-2):
        max_height = max(building[p-1], building[p-2],building[p+1], building[p+2])
        if building[p] > max_height:
            nice_view += building[p] - max_height
    results.append(nice_view)
cnt = 1
for result in results:
    print(f"#{cnt} {result}")
    cnt += 1
