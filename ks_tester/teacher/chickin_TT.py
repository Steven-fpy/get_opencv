
import math
import os
import sys

# 수탉은 5달러, 암닭은 3달러, 병아리는 3마리 1달러이다. 
# 100달러를 사용하여 닭 100마리를 사려면 몇마리의 수탉, 암탉, 병아리를 얻을 수 있을까? 

# 병아리 3마리
COST_CHICK = 1
# 암탉
COST_HEN = 3
# 수탉
COST_ROOSTER = 5

# 사용가능한 비용
MAX_MONEY = 100
# 목표 수량
MAX_COUNT = 100


maxRoosterCount = MAX_MONEY // COST_ROOSTER
maxHenCount = MAX_MONEY // COST_HEN
maxChickCount = MAX_MONEY // COST_CHICK


for rooster in range(1, maxRoosterCount):
    for hen in range(1, maxChickCount):
        for chick in range(1, maxChickCount):
            totalCost = rooster * COST_ROOSTER + hen * COST_HEN + chick * COST_CHICK
            totalCount = rooster + hen + chick * 3
            # if totalCost <= MAX_MONEY and MAX_COUNT == rooster + hen + chick * 3:
            if totalCost == MAX_MONEY and MAX_COUNT == rooster + hen + chick * 3:
                print(f'총구매비용: {totalCost}, 총수량: {totalCount}, 수탉: {rooster}, 암탉: {hen}, 병아리: {chick * 3}')

        

# henCount = 0
# roosterCount = 0
# chickCount = 0

# totalCount = 0
# while True:

#     henCount = 0
#     chickCount = 0
        
#     currentMoney = maxMoney
#     currentMoney -= COST_ROOSTER
#     roosterCount += 1
#     totalCount += 1

#     # print('totalCount: ', totalCount)

#     if currentMoney <= 0 or totalCount >= 100:
#         break

#     while True:

#         chickCount = 0

#         total2 = totalCount
#         currentMoney2 = currentMoney   
#         currentMoney2 -= COST_HEN
#         henCount += 1
#         total2 += 1
#         # print('total2: ', total2)

#         if currentMoney2 <= 0 or total2 >= 100:
#             break

#         while True:
#             currentMoney2 -= COST_CHICK
#             chickCount += 3
#             total2 += 3
#             # print('chick total2: ', total2)

#             if currentMoney2 <= 0 or total2 > 100:
#                 break
#             elif total2 == 100:
#                 print(f'총구매수량: {total2}, 수탉: {roosterCount}, 암탉: {henCount}, 병아리: {chickCount}')
#                 break

#         if total2 >= 100:
#             break