num = int(input("숫자 입력:"))
bull = 0
for i in range(2, num):
    if num % i != 0:
        continue
    else:
        bull = 1
        break

if bull == 0:
    print(f"{num} 는 소수입니다.")
else:
    print(f"{num} 는 소수가 아닙니다.")
