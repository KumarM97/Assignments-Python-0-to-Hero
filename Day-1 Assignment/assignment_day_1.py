# -*- coding: utf-8 -*-
"""Assignment Day-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KfxeWKYmxSHOOM2KQvjwgMe7NSYBofBc
"""

# Assignment- Day-1
# Qustion:    Take multiple numbers through input and print the sum of the numbers.
total = 0
x = input('Enter Multiple Integer Values: ')
y = x.split()
lis= []
for i in y:
  lis.append(int(i))
for j in range(0, len(lis)):
    total = total + lis[j]
print("Sum of all Numbers: ", total)