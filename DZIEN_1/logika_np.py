import numpy as np

import matplotlib.pyplot as plt

# points = np.arange(-5,5,0.01)
#
# xs,ys = np.meshgrid(points,points)
#
# z = np.sqrt(xs**2+ys**2)
#
# plt.imshow(z,cmap=plt.cm.gray)
# plt.colorbar()
# plt.title("Wykres funkcji $\sqrt{x^2+y^2}$ dla określonych wartości x i y")
# # plt.title("Wykres funkcji okrąg dla określonych wartości x i y")
# plt.draw()
# plt.show()

print("_____ logiczne operacje warunkowe jako operacje tablicowe _______ ")

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,False,True,True,False])

w = list(zip(xarr,yarr,cond))
print(w)

result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print(result)

print("a co na to numpy???")
result = np.where(cond,xarr,yarr)
print(result)

print("______________________________")
arr = np.random.randn(4,4)
print(arr)
print("______________________________")
print(arr>1)
print("______________________________")
print(np.where(arr>1,2,-2))
print("______________________________")
print(np.where(arr>1,2,arr))
