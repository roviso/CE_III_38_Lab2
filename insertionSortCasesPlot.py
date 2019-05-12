import random
from time import time
from sorting import  insertionSort
import matplotlib.pyplot as plt

n=1000
insertionTimeArrayRandom = []
insertionTimeArrayBest = []
insertionTimeArrayWorst = []
sizeArr =[]

for i in range(n,n*11,n):
	sizeArr.append(i)
	randomValues = random.sample(range(i), i)
	bestCase = randomValues
	worstCase = randomValues
	startTime = time()
	insertionSort(randomValues)
	endTime = time()
	totalTime = endTime -startTime
	insertionTimeArrayRandom.append(totalTime)
	print("For",i,"the time is",totalTime)

	bestCase.sort()
	startTime = time()
	insertionSort(bestCase)
	endTime = time()
	totalTime = endTime -startTime
	insertionTimeArrayBest.append(totalTime)
	print("For",i,"the time is",totalTime)

	worstCase.sort(reverse = True)
	startTime = time()
	insertionSort(worstCase)
	endTime = time()
	totalTime = endTime -startTime
	insertionTimeArrayWorst.append(totalTime)
	print("For",i,"the time is",totalTime)



# Plot size vs time graph
fig, ax = plt.subplots(1, 1)
ax.plot(sizeArr,insertionTimeArrayRandom, label = 'InsertionSortRandom')
ax.plot(sizeArr,insertionTimeArrayBest, label = 'InsertionSortBest')
ax.plot(sizeArr,insertionTimeArrayWorst, label = 'InsertionSortWorst')
legend = ax.legend(loc = 'upper center', fontsize = 'large')
plt.show()
