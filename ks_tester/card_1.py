import random
import time


Input = input("숫자를 입력해주세요 (2~100) : ")
print(f"{Input} 개의 숫자로 게임을 시작합니다.")            #랜덤 자연수
print("로딩중...")
time.sleep(1)

Card = [] 
MaxCard = int(Input)

while len(Card) < MaxCard:
    R = random.randint(1,100)
    if R not in Card:
        Card.append(R)
# print("card : ", Card)

for i in range(0,MaxCard):
    i += 1
    Cards = [Card[i]]
    print(f"card[{i}] : {Cards}")
    







# def solution(cards):
#     answer = 0
#     return answer

# stdio
# stdbool
# stdlib

# int solution(int cards[], size_t cards_len){
# int answer = 0;
# return answer;
# } 