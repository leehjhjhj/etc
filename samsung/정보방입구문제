n = int(input())
k = int(input())
lst = []
one = n - 3
two = n - 1
for _ in range(n):
    lst.append(0)
lst[one] = 1
lst[two] = 1

for i in range(k-2):
    if lst[one + 1] == 0:
        lst[two] = 0
        two -= 1
        lst[two] = 1
    else:
        lst[one] = 0
        one -= 1
        lst[one] = 1
        lst[two] = 0
        two = -1
        lst[two] = 1
cnt = 0
answer = 0
for _ in range(n):
    target = lst.pop()
    if target == 1:
        answer = n - cnt
        break
    cnt += 1

binary_answer = []
while answer // 2 != 0:
    if answer % 2 == 1:
        binary_answer.append(1)
        answer //= 2
    else:
        binary_answer.append(0)
        answer //= 2
    if answer == 1:
        binary_answer.append(1)

for i in range(len(binary_answer) -1, -1, -1):
    print(binary_answer[i], end="")
