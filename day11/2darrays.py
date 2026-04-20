"""
Author: Carter Spenner
Date: 4/20/2026
Purpose: To practice using 2D arrays
"""

import numpy

#80% code
array1 = numpy.arange(1, 11)
array1 = numpy.outer(array1, array1)
print(f"Array 1:\n{array1}")

#90% code
array2 = numpy.random.randint(1, 101, (20, 20))
print(f"Array 2:\n{array2}")

totalSum = 0
for l in range(20):
    for w in range(20):
        totalSum = totalSum + array2[l][w]
print(f"Total Sum:\n{totalSum}")

#100% code
array2 = numpy.where(array2 % 2 == 0, 0, array2)
array2 = numpy.where(array2 % 3 == 0, 0, array2)
print(f"Filtered Array:\n{array2}")