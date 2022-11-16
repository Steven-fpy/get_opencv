import time
import random
Input = input("숫자를 입력해주세요 (2~100) : ")
MaxCard = int(Input)-1

if MaxCard <2:
    print("입력 숫자 범위를 다시 확인해 주세요\n(허용범위는 2~100)")
    input("숫자를 입력해주세요 1(2~100) : ")
    print("입력 숫자 범위를 다시 확인해 주세요2\n(허용범위는 2~100)")
    input("숫자를 입력해주세요 2(2~100) : ")
    print("입력 숫자 범위를 다시 확인해 주세요3\n(허용범위는 2~100)")
    print("설명을 확실하게 읽어주세요 ~ 안녕")
    
elif MaxCard>=2:
    print(f"{Input} 개의 숫자로 게임을 시작합니다.")            #랜덤 자연수
    print("로딩중...")

time.sleep(1)

Card = []

# while True:
A_Card = [x for x in range(1,101)]
B_Card = [y for y in range(1,101)]

# print(A_Card)
# print(i)
    # A_Card = 0
    # print(A_Card, end=" ")
# print(A_Card[1]) 

random.shuffle(A_Card)
random.shuffle(B_Card)


# print(A_Card)

for i in range(1, MaxCard+1):
    # i += 1
    for j in range(1, MaxCard+1):
    # j += 1
        print(f"card-i[{j}] : {A_Card[j]}")
        # print(f"{A_Card[i]}")

        time.sleep(0.1)
        # print(f"card-j[{j}] : {B_Card[j]}")
    if A_Card[j] == B_Card[j]:
        # print("끝")
        print(A_Card[j])
        time.sleep(0.1)
        break
    break
