# m = 5 
# w = 3
# c = 1
# money = 100
# a = int()

# for x in range(20):
#     x += 1 
#     m*x <money
#     for y in range(40):
#         y += 1 
        
#         w*y < money
#         for z in range(100):
#             z += 1
#             c*z <money
#             # print (f"m = {type(m)},w = {type(w)},c = {type(c)}")
#             # print (f"x = {type(x)},y = {type(y)},z = {type(z)}")
#         if money > 0:
#             a = (max((5*x + 3*y +(z*3)) <= money))
            
#             print(a)            
#             # print (type(w))
#             # print (type(c))

#             # print (type(t))

Red = 80
Yellow = 50
Purple = 36
TotalCost = 2000
Min = 5

print("예산을 입력해 주세요(최대 2000원)")
n = input("숫자를 입력해 주세요 : ")
print (f"입력하신 예산은 {n}원 입니다")
m = int(n)
if m >= 2001:
    print("예산을 초과하였습니다. 다시 입력해주세요(최대 2000원)")
R,Y,P = 0,0,0

for R in range(Min,Red//TotalCost):
    R += 1
    # print("R",R)
for Y in range(Min,Yellow//TotalCost):
    Y += 1
for P in range(Min, Purple//TotalCost):
    P += 1
    if m <= TotalCost and (2*R == Y or P == R//3): # and ((R + Y) < TotalCost):
    # ((R + Y) < TotalCost)

        print(f"빨간꽃 = {R}, 노란꽃 = {Y}, 보라꽃 = {P}")




