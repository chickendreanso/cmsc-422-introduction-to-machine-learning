from imports import *

h = dumbClassifiers.AlwaysPredictOne({})
h
h.train(datasets.TennisData.X, datasets.TennisData.Y)
# h.predictAll(datasets.TennisData.X)
print(h.mostFrequentClass)