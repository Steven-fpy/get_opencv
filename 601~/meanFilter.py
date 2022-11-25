import random 
import matplotlib.pyplot as plt
# import time

# 50~60범위안에서 랜덤으로 생성되는 1000개 샘플의, 실시간으로 평균필터된 값을 구하고(샘플이 추가될때마다) 최종 평균을 구하세요.

sampleCount = 1000

# samples = []
# mean = []
meanPlots = []
samplePlots = []

total = 0

# a, b = input("숫자를 입력하세요 : ").split()
# c = int(a)
# d = int(b) 

for i in range(sampleCount):
    # val = random.uniform(c,d)
    sample = random.uniform(50, 100)
    # samples.append(sample)
    print(f'[{i+1}]sample', sample)
    # print('val:', val)
    # **평균필터필터
    # for n in range(1, sampleCount):
        # gm = (sum(samples[n-1]+[n])/n)    #*((samples-i)/i)+ i(i-1/i)

    # 평균값 계산

    # mean = sum(samples)/len(samples)
    # t = 0
    # for v in samples:
    #     t += v

    # mean = t / (i+1)

    total += sample
    mean = total / (i+1)

    # mean = sample



        # print ("gm의 값 : ", gm)
    # sm = sum(samples)
    # print("sm의 값 : ", sm)
    # means = samples
    # mean = random.uniform(51, 50)
    # means.append(mean)

    samplePlots.append([sample])
    meanPlots.append([mean])
# meAn = sum(mean)/sum(samples)
# smpMean = sum(samples)/len(samples)
# l = len(samples)
# print("len_sam: ", l)
# print("meAn : ", meAn)
# print("smpMean :", smpMean)
plt.plot(samplePlots,color = 'b', label = 'sample')
plt.plot(meanPlots, color = 'r', label = 'mean', alpha = 0.5)
# plt.plot(smpMean, color = 'g', label = 'smpMean', alpha = 0.5)

# plt.plot(meAn, color = 'b', label = 'meAn')

plt.legend(loc = 'best')

plt.show()


# print('result mean', mean)







