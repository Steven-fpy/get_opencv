import math
import time
import os


X = []  #예선점수 저장소
Y = []  #준결 점수 저장소
Z1 = []  #종합 성적 저장소
P = []
# P = Z.sort() 
# Z.sort()
HUMAN_COUNT = 0


def inPut():
    global X,Y,HUMAN_COUNT,Z ,x,y,z
    x, y = input ("예선점수와 준결승 점수를 입력하세요\n (공백으로 구분하여 입력해주세요)\n ex)90 90\n 여기에 입력해 주세요 : ").split()
    x1 = int(x)
    y1 = int(y)
    Z =x1*0.25+y1*0.75
    if x1 >= 0 and Z>=90:
        os.system("clear")
        # x2 = float(0.25)
        # y2 = float(0.75)
        z = float(Z)
        # print(f"예선점수 : {x} 점, 준결승점수 : {y}점, z값 : {z:.2f})")
        if x1 == 100 and y1 == 100:
            print("☆★아니 이렇게 완벽할수가 당신은 우승하였습니다★☆\n            :::You Are Perfect:::")   
        X.append(x1)
        Y.append(y1)
        Z1.append(z)
        P.append([x1,y1,z])
        
        # print("\n\n                  낫 파운드!!!")
    elif Z<90:
        print("조금 더 열심히 하세요 탈락입니다")
    elif x1 == 100 and y1 == 100:
        print("☆★아니 이렇게 완벽할수가 당신은 우승하였습니다★☆\n            :::You Are Perfect:::")
    
    elif x1 < 0:
        print("예선탈락.....안녕...!!!!!")
        time.sleep(1)
        os.system("exit()")
    time.sleep(1)
    HUMAN_COUNT +=1
    return x,y,z,HUMAN_COUNT,P

    
def sort(x,y,z,HUMAN_COUNT,P):
    # global P
    P.sort(key =lambda x:x[2])
    # global X,Y,Z1,P
    # print(X[1],Y[1],Z[1])
    os.system("clear")
    # print(P[0][0], P[0][1],     P[0][2])
    return x,y,z,HUMAN_COUNT,P

def next(x,y,z,HUMAN_COUNT,P):

    for i in range(0, len(P)):
        print(P[i][0], P[i][1], P[i][2])
    return x,y,z,HUMAN_COUNT,P

        
while True:
    inPut()
    sort(x,y,z,HUMAN_COUNT,P)
    next(x,y,z,HUMAN_COUNT,P)
    print("참가인원수: ", HUMAN_COUNT)
    # Z.sort()
    # Z.reverse()
    
    # print(f"{X}{Y}{Z}")
    # print(Z)
    # for i in range(0, 101):
    #     i += 1
    #     print(f"예선점수 : {X[i-1]}점, 준결점수 : {Y[i-1]}점, 평점 : {Z} 점")
    # print(Z.sort())
    if HUMAN_COUNT == 9:
        break 
    else:
        pass
