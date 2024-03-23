# -*- coding: utf-8 -*-

# -- Sheet --

# # Podstawy pakietu Numpy
# Analiza podstawowych **struktur pakietu**, przykłady budowy <span style="color:red; font-size:16pt; font-family:Impact;">struktur danych</span>.
# <p>
# <img src="numpy.png">
# </p>


import numpy as np

def split_into_words(sentence):
    words = sentence.split()
    return words

# Test the function
test_sentence = "To jest przykładowe zdanie do podziału na słowa"
print(split_into_words(test_sentence))


def convert_num_to_str(num):
    """
    This function converts a number to a string.
    It accepts both integers and floats and returns them as a string.
    """
    return str(num)
    
# Test the function
test_number = 12345
print(convert_num_to_str(test_number))  # Expected output: "12345"


def create_array(data_list, desired_shape):
    """
    This function converts a list into a numpy array of a desired shape.
    """
    if np.prod(desired_shape) == len(data_list):
        return np.array(data_list).reshape(desired_shape)
    else:
        return "Error: List length doesn't fit the desired shape"

# Test the function
test_list = [1, 2, 3, 4, 6, 7, 8, 9]
test_shape = (2, 4)
print(create_array(test_list, test_shape))

np.zeros(8)

print(np.ones(11))

np.empty(10)

u = np.arange(1,77,3)
print(u)

print(type(u))

zlista = [5,3,5,26,25,8,37,7]
print(type(zlista))

k = np.linspace(0,10,num=5)
print(k)

mlista = np.array(zlista)
print(mlista)
print(type(mlista))

kl = (4,223,67,89,24,1,5)
znum = np.array(kl)
print(znum)
print(type(znum))

mlista = list(znum)
print(mlista)
print(type(mlista))

zb = {45,25,8,9,12,45,7,25}
znp = np.array(zb)
print(znp)
print(type(znp))

mlista.sort()
print(mlista)

l1 = [2,5,63,6,56]
l2 = [35,63,2,7,3]
l3 = [4,2,6,79,5]

l = l1+l2+l3
print(l)

a = np.array(l1)
b = np.array(l2)
c = np.array(l3)

f = a+b+c
print(f)

ca = np.concatenate((a,b,c))
print(ca)

z1 = [[56,4],[43,5]]
print(z1)

print(z1[0][1])

a1 = np.array(z1)
print(a1)

print(a1[0,1])

print(a1[0][1])

mm = np.array([[24,63,6],[64,25,6]])
print(mm)

x = np.array([[4,2,6],[7,5,2],[8,3,2]])
y = np.array([[9,9,4],[2,1,3],[1,1,5]])

print(x)

print(y)

p = np.concatenate((x,y),axis=1)
print(p)

q = np.concatenate((x,y),axis=0)
print(q)

prosta = np.arange(12)
print(prosta)

fp = prosta.reshape(3,4)
print(fp)

mac1 = np.array([[2,3],[4,5],[9,9]])
print(mac1)

print(mac1.shape)

w1 = mac1.reshape(6)
print(w1)

ar = np.array([1,7,3,89,32,5,89,0,7,12,4,6,23])
print(ar.shape)

print(ar[:7].shape)

print(ar[2:5].shape)

w = np.array([[1,2,3,4],[9,10,11,12],[23,78,43,65]])
print(w)

print(w[w<5])

pc = (w>=5)
print(w[pc])

print(w[w%2==0])

cv = (w>2)&(w<=21)
print(w[cv])

sv = (w<8)|(w>=33)
print(w[sv])

#operacje  na wektorach
dane = np.array([1,3,8])
one = np.ones(3,dtype=int)
tw = np.array([2,2,3])

print(dane+one)

print(dane-one)

print(dane*tw)

print(dane/tw)

print(dane*1.88)

on = np.ones(5,dtype=int)
print(on)

m1 = np.array([[443,545,2],[75,36,887],[1,2,1]])
m2 = np.array([[24,54,235],[5,35,2],[1,6,9]])
wynik = (m1+m2)*m1
print(wynik)

print(f'wartość najmniejsza: {wynik.min()}')
print(f'wartość największa: {wynik.max()}')
print(f'wartość średnia: {wynik.mean()}')
print(f'wartość odchylenia standardowego: {wynik.std()}')

