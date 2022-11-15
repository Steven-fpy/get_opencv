import time

Red = 80
Yellow = 50
Purple = 36
TotalCost = 2000
Min = 4

#2r == y, p == r/3 , n<x<2000

print("예산을 입력해 주세요(최대 2000원)")
n = input("숫자를 입력해 주세요 : ")
print (f"입력하신 예산은 {n}원 입니다")
m = int(n)
if m >= 2001:
    print("예산을 초과하였습니다. 다시 입력해주세요(최대 2000원)")

R, Y, P = 0, 0, 0
      
def flower():
    global R, Y, P
    if (R*Red + Y*Yellow) < TotalCost:
        # for R in range(Min,Red//TotalCost):
        for R in range(Min,TotalCost//Red):
        
            R += 1
            # print("R",R)
            # for Y in range(Min,Yellow//TotalCost):
            for Y in range(Min,TotalCost//Yellow):

                # Y += 1
                Y = R*2
                
                # P = (TotalCost-(R*Red+Y*Yellow))//36
                for P in range(Min, Purple//TotalCost):
                    P += 1
                #     # if m <= TotalCost and (2*R == Y or P == R//3): # and ((R + Y) < TotalCost):
                    if (2*R == Y or P == R//3) and ((R + Y) < TotalCost) and (P > 0):

                    # ((R + Y) < TotalCost)

                        print(f"빨간꽃 = {R}, 노란꽃 = {Y}, 보라꽃 = {P}") 
                        time.sleep(0.3)
                                # pass
while P >= 0:
    flower()
    break

    