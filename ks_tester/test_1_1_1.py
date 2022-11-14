import time

# y = 5
p = 5
r = 5
n = 0
y = r*2

if p > 0:
    p = y/3
print("예산을 입력해 주세요(최대 2000원, 숫자만 입력해주세요)")
n = input("숫자를 입력해 주세요 : ")
# if not input(int):
#     continue
print (f"입력하신 예산은 {n}원 입니다")
m = int(n)
if m >= 2001:
    print("예산을 초과하였습니다. 다시 입력해주세요(최대 2000원)")
    pass
def flower():
    global r, y, p
       
# def flowerpay():
    for p in range(4,30):
        p > 0
        p += 1
        p = (2000-(r*80+y*50))//36
        if p >=31:
            p = 5
            continue
        for y in range(4,30):
            y += 1
            for r in range(4,30):
                r += 1
                if (r*80 + y*50 + p*36) < 2000 : #and (r*80 + y*50)<2000:#and (p*80 + y*50)<2000):

                    # if (r*80 + y*50 + p*36) < 2000 and (((r*80 
                    # + y*50) < 2000) or (((p*36 + y*50) < 2000)and (p = y/3))):
                    print(f"r:{r}  y:{y}  p:{p}")
                    time.sleep(0.05)
# flowerpay()
while m:
    # p>0
    flower()

    break
