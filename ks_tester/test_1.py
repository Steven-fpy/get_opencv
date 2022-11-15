import math
import os
import time

# y = r*2 , p = y/3
# min = 5
# n <= 2000
# y,r,p >= 5
n = 0
print("예산을 입력해 주세요(최대 2000원)")
n = input("숫자를 입력해 주세요 : ")
print (f"입력하신 예산은 {n}원 입니다")
m = int(n)
if m >= 2001:
    print("예산을 초과하였습니다. 다시 입력해주세요(최대 2000원)")
    pass
r = 4
y = r*2
p = y/3
# p = (2000 - (r*80 + y*50)//36)
# p > 0

def flowercal():
    global r, y, p
    # if ((r*80 + y*50) < 2000):
    
        # if ((r*80 + y*50) < 2000):
            # continue   
            # p > 0
            # p = (2000-(r*80+y*50))//36
            # 0<p*36 <= 2000
    if ((r*80 + y*50) < 2000):
    # if p > 0 and ((r*80 + y*50) < 2000):
        for r in range(4, 15):
            r += 1
            for y in range(5, 20):
                y = r*2
                p = (2000-(r*80+y*50))//36
                # (r*80 + y*50 + p*36) <= 2000
            if p > 0 : 
                print(f"빨간꽃 : {r}, 노란꽃 : {y}, 보라꽃 : {p}")
    # if (p*36 + y*50) < 2000:
    #     p = y//3
    #     for r in range(4, 15):
    #         r += 1
    #         (r*80 + y*50 + p*36) < 2000
    #     if p > 0:
    #             print(f"빨간꽃 : {r}, 노란꽃 : {y}, 보라꽃 : {p}")

        # print('r: ', r)
        # print('y: ', y)
        # print('p: ', p)
    # for y in range(100): 
        # for p in range(100):
    # time.sleep(2)
        # pass
    # if r*80 + y*50 <=2000:
    #     for p in range(100):
    #         p = (2000-(r*80+y*50))//36
    #         time.sleep(1)

    # for i in range(3000):
         
    #     if ((r*80 + y*50 + p*36) < 2000):
    
    # # for o in range((r*80 + y*50 + p*36) < 2000):
        
    #         continue
        # return
    # if (r*80 + y*50 + p*36) <= 2000:
    #     print("여기까지")
    # for (r*80 + y*50 + p*36) < 2000:
    
    



while m:
    # r,y,p >= 5
    flowercal()

    # return
    # continue
    time.sleep(0.5)
    # (y = r*2) or (p = y/3) or (y = r*2 and p = y/3)
           
    # if (r*80 + y*50 + p*36) <= 2000:
    break