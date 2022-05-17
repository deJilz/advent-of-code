import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
'''
14 May 2022
PART 2 - 1198704

Concepts: pyplot, skimage

this one was heavily inspired by a reddit comment, thought id learn some about skimage
'''

array = np.array([list(x.strip()) for x in open(os.path.basename(__file__).split('_')[0]+'.txt', 'r')],dtype=int)

# show the clusters to view
# original input
plt.figure(1,clear=True)
plt.imshow(array)
# show ridges
plt.figure(2, clear=True)
plt.imshow(array<9)

# find regions
labels = measure.label(array<9,connectivity=1)
plt.figure(3,clear=True)
plt.imshow(labels)

# creates array of size range with the sum of trues out of the comparison
areas = [np.sum(labels==i) for i in range(1,np.max(labels)+1)]
print('largest areas ',np.prod(np.sort(areas)[-3:]))

plt.show()