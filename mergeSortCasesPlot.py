import random
from time import time
from sorting import  mergeSort
import matplotlib.pyplot as plt

n=1000
mergeTimeArrayRandom = []
mergeTimeArrayBest = []
mergeTimeArrayWorst = []
sizeArr =[]

for i in range(n,n*11,n):
	sizeArr.append(i)
	randomValues = random.sample(range(i), i)
	bestCase = randomValues
	worstCase = randomValues
	startTime = time()
	mergeSort(randomValues)
	endTime = time()
	totalTime = endTime -startTime
	mergeTimeArrayRandom.append(totalTime)
	print("For",i,"the time is",totalTime)

	bestCase.sort()
	startTime = time()
	mergeSort(bestCase)
	endTime = time()
	totalTime = endTime -startTime
	mergeTimeArrayBest.append(totalTime)
	print("For",i,"the time is",totalTime)

	worstCase.sort(reverse = True)
	startTime = time()
	mergeSort(worstCase)
	endTime = time()
	totalTime = endTime -startTime
	mergeTimeArrayWorst.append(totalTime)
	print("For",i,"the time is",totalTime)



# Plot size vs time graph
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArr,mergeTimeArrayRandom, label = 'MergeSortRandom')
ax.plot(sizeArr,mergeTimeArrayBest, label = 'mergeSortBest')
ax.plot(sizeArr,mergeTimeArrayWorst, label = 'mergeSortWorst')
legend = ax.legend(loc = 'upper center', fontsize = 'large')
plt.show()
