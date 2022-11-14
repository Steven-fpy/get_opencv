
import math
import os
import sys


# 수탉은 5달러, 암닭은 3달러, 병아리는 3마리 1달러이다. 
# 100달러를 사용하여 닭 100마리를 사려면 몇마리의 수탉, 암탉, 병아리를 얻을 수 있을까? 

# 병아리 3마리
chickCost = 1
# 암탉
henCost = 3
# 수탉
roosterCost = 5

# 사용가능한 비용
totalMoney = 100
# 목표 수량
maxCount = 100

henCount = 0
roosterCount = 0
chickCount = 0

totalCount = 0
while True:
        
    currentMoney = totalMoney
    currentMoney -= roosterCost
    roosterCount += 1
    totalCount += 1

    # print('totalCount: ', totalCount)

    if currentMoney <= 0 or totalCount >= 100:
        break

    while True:

        total2 = totalCount
        currentMoney2 = currentMoney   
        currentMoney2 -= henCost
        henCount += 1
        total2 += 1
        # print('total2: ', total2)

        if currentMoney2 <= 0 or total2 >= 100:
            break

        while True:
            currentMoney2 -= chickCost
            chickCount += 3
            total2 += 3
            # print('chick total2: ', total2)

            if currentMoney2 <= 0 or total2 > 100:
                break
            elif total2 == 100:
                print(f'총구매수량: {total2}, 수탉: {roosterCount}, 암탉: {henCount}, 병아리: {chickCount}')
                sys.exit()

        if total2 >= 100:
            break

        # start = totalCount
        # for n in range(start, 101, 3):
            
        #     totalMoney = totalMoney - chick
        #     chickCount += 1

        #     if totalMoney <= 0:
        #         break

        #     totalCount = n

# print(f'총구매수량: {totalCount}, 수탉: {roosterCount}, 암탉: {henCount}, 병아리: {chickCount}')
