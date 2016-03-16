import numpy as np
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt

A = np.zeros((15,40))
A = np.matrix(A)

# H
A[2:10,2:4] = 1 
A[2:10,6:8] = 1
A[5:7,3:8] = 1

# E
A[3:11,10:15] = 1
A[5,12:15] = 0
A[8,12:15] = 0

# L
A[4:11,17:19] = 1
A[10:12,17:23] = 1

# L
A[5:12,25:27] = 1
A[11:13,25:31] = 1

# O
A[6:14,33:39] = 1
A[8:12,35:37] = 0

u, s, v = np.linalg.svd(A)
x = np.linspace(1,len(s),len(s))

k = np.zeros((len(s), len(s)))
for i in xrange(len(s)):
    k[i,i] = s[i]

print(k[1:4,1:4])
    
for j in xrange(12):
    i = j+1
    print(i)
    rankiap = (np.dot(u[0:14,0:i],np.dot(k[0:i,0:i],
            np.transpose(v[0:40,0:i]))))
    plt.pcolor(np.array(rankiap),cmap = 'Greys')
    plt.ylim((14,2))
    plt.show()

    
#plt.plot(x,s)
#plt.semilogy(x,s)
#plt.show()
#pyl.spy(A)
#pyl.show()
