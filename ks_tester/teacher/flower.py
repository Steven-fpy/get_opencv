
import math


# 붉은색 꽃, 노란색 꽃, 보라색 꽃을 색상별로 최소 5봉지 이상 구매하고 싶다.
# 그 중 품종에 대한 요구 사항은 적어도 다음 조건 중 하나를 충족한다. 

# 1. 노란색 꽃은 빨간색 꽃의 2배가 필요하다. 
# 2. 보라색 꽃은 노란색 꽃의 1/3 이다. 

# 이 비율에 따라 구매가 진행되며 총 구매 경비 x는 (n<x<2000)

MIN_COUNT = 5
COST_RED = 80
COST_YELLOW = 50
COST_PURPLE = 36

inputText = input('구매경비 (최대 2000): ')

if inputText.isdigit():
    totalMoney = int(inputText)

    for n in range(MIN_COUNT, totalMoney // COST_RED):

        redCount = n
        currentRedCost = redCount * COST_RED
        money = totalMoney - currentRedCost

        # print(f'{redCount }', end='')
        # print(f'[{redCount}]')

        # if money <= 0:
        #     # print(f'break {redCount}')
        #     continue

        yellowTryCount = money // COST_YELLOW
        for yellowCount in range(MIN_COUNT, yellowTryCount):

            currentYellowCost = yellowCount * COST_YELLOW
            leftMoney = money - currentYellowCost

            # if leftMoney <= 0:
            #     # print(f'break {redCount}, {yellowCount}, {0}')
            #     continue

            # pupleCount = math.ceil(leftMoney / COST_PURPLE)
            pupleCount = leftMoney // COST_PURPLE
            # pupleCount = round(leftMoney / COST_PURPLE)

            totalCost = redCount * COST_RED + yellowCount * COST_YELLOW + pupleCount * COST_PURPLE

            if pupleCount >= MIN_COUNT and (yellowCount == redCount * 2 or pupleCount == yellowCount // 3):
            # if pupleCount >= MIN_COUNT and (yellowCount == redCount * 2 or pupleCount == math.ceil(yellowCount / 3)):
            # if pupleCount >= MIN_COUNT and (yellowCount == redCount * 2 or pupleCount == round(yellowCount / 3)):
                print(f'빨: {redCount}, 노: {yellowCount}, 보: {pupleCount}, 총비용: {totalCost}')
                continue

            # print(f'break {redCount}, {yellowCount}, {pupleCount}')



