import random
from matplotlib import pyplot as plt


# samples = []
# mean = []

sampleCount = 100

samplePlots = []
meanPlots = []

total = 0

samples = []

x = 10
n = 0

def meanFilterBatch():
    global samples

    mean = sum(samples)/len(samples)

    return mean
def meanFilterBatch2(sample, numOfSample):
    global total

    total += sample
    mean = total / numOfSample
    return mean 

for i in range(sampleCount):

    if i % 10 == 0:
        n += 1

    sample = random.uniform(50 + n,51 + n)
    print(f'[{i + 1}] sample: ', sample)
      
    # mean = total/ (i + 1)
    samples.append(sample)

    if len(samples) > x:
        samples.pop(0)
    
    mean = meanFilterBatch()

    samplePlots.append([sample])
    meanPlots.append([mean])
print('result mean: ', mean)


plt.plot(samplePlots,color = 'b', label = 'sample')
plt.plot(meanPlots,color = 'r', label = 'mean', alpha = 0.5)

plt.legend(loc = 'best')

plt.show()
