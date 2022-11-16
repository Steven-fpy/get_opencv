import time
import math

RED = 80
YELLOW = 50
PURPLE = 36
MIN_C = 5

#2r == y, p == r/3 , n<x<2000

print("예산을 입력해 주세요(최대 2000원)")
inputText = input("숫자를 입력해 주세요 : ")
print (f"입력하신 예산은 {inputText}원 입니다")

if inputText.isdigit():
    totalM = int(inputText)
    # if totalM >= 2001:
    #     print("예산을 초과하였습니다. 다시 입력해주세요(최대 2000원)")

    for r in range(MIN_C,totalM//RED+1):
        rC = r
        cRC = rC * RED
        moNey = totalM - cRC

        # print("R",R)
        # for Y in range(Min,Yellow//TotalCost):
        for yC in range(MIN_C,moNey//YELLOW+1):

            # Y += 1
            cYC = yC*YELLOW
            lM = moNey - cYC 
            # P = (TotalCost-(R*Red+Y*Yellow))//36
            pC = lM // PURPLE
            #     # if m <= TotalCost and (2*R == Y or P == R//3): # and ((R + Y) < TotalCost):
            if pC >= MIN_C and (yC == rC * 2 or pC == yC//3):
            
            # if (2*R == Y or P == R//3) and ((R + Y) < TotalCost) and (P > 0):

                # ((R + Y) < TotalCost)

                print(f"빨간꽃 = {rC}, 노란꽃 = {yC}, 보라꽃 = {pC}") 
                continue    