ROOSTER = 5                         # 수탉의 가격설정
HEN = 3                             # 암탉의 가격설정
CHIC = 1                            # 병아리의 가격설정
TOTAL_M = 100                       # 총비용 설정
MAX_COUNT = 100                     # 총 마릿수 설정

# RooC = 0
# HenC = 0
# ChikC = 0
MaxRooC = TOTAL_M // ROOSTER        #수탉의 최대 마릿수는 총비용 // 수닭값
MaxHenC = TOTAL_M // HEN            #암탉의 최대 마릿수는 총비용 // 암닭값
MaxChikC = TOTAL_M // CHIC          #병아리의 최대 마릿수는 총비용 // 병아리값


# TotalC = 0

for rooster in range(1, MaxRooC):   #rooster라는 값은 1부터 수닭의 최대 마릿수 까지
    # RooC += 1
    # TRc = RooC*Rooster
    for hen in range(1, MaxHenC):   #hen이라는 값은 1부터 암닭의 최대 마릿수 까지
        # HenC += 1
        # THc = HenC*Hen
        for chic in range(1, MaxChikC): #chic 이라는 값은 1부터 chic 최대 마릿수 까지
            # ChikC += 1
            # TCc = ChikC*Chic
            totalCost = rooster * ROOSTER + hen * HEN + chic*CHIC
            #totalCost 는 위의 값을 더한것
            totalC = rooster + hen + chic * 3
            # totalCost = 수 + 암 + 병아리*3
            if totalCost == TOTAL_M and MAX_COUNT == (rooster + hen + chic*3):
                #만약 토탈코스트가 최대비용과 같으며 총 마릿수가 수 + 암 + 병아리*3 마리수와 일치하면
                print(f"수탉{rooster}마리, 암탉{hen}마리, 병아리{chic*3}마리")
                #위를 실행











# while True:

#     CurrentM = TotalM
#     CurrentM -= Rooster
#     RooC += 1
#     TotalC += 1

#     if CurrentM <= 0 or TotalC >= 100:
#         break

#     while True:

#         TotalC2 = TotalC
#         CurrentM2 = CurrentM
#         CurrentM2 -= Hen
#         HenC += 1
#         TotalC2 += 1

#         if CurrentM2 <= 0 or TotalC2 >= 100:
#             break

#         while True:

#             CurrentM2 -= Chic
#             ChikC += 3
#             TotalC2 += 3

#             if CurrentM2 <= 0 or TotalC2 > 100:
#                 break
#             elif TotalC2 == 100:
        #         print(f'총 마릿수 : {TotalC2}, 수탉: {RooC}, 암탉: {HenC}, 병아리: {ChikC}')
        # if TotalC2 >= 100:
        #     break