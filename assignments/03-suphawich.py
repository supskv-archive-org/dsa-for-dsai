#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from time import time

nlist = np.linspace(0, 900000, 100)

def running_time(callback):
    print(f"Running {callback.__name__}...")
    result = []
    ts = []
    for n in nlist:
        x = np.logspace(0, 15, int(n), dtype=np.float128)
        start = time()
        result.append(callback(x))
        taken = time() - start
        ts.append(taken)
    return np.array(ts)

def constant(x):
    return 100

def n(x):
    return 1*x

def square(x):
    return x*x

def squareroot(x):
    return np.sqrt(x)

def nlogn(x):
    return x*np.log(x)

def cube(x):
    return x**3

def exponential(x):
    return 2**x

start = time()
print('Start record running time:', start)
y_1_ts = running_time(constant)
y_n_ts = running_time(n)
y_square_ts = running_time(square)
y_squareroot_ts = running_time(squareroot)
y_nlogn_ts = running_time(nlogn)
y_cude_ts = running_time(cube)
y_2n_ts = running_time(exponential)
taken = time() - start

nlist = nlist

fig = plt.figure()
p = fig.add_subplot(1,1,1)
# p.set_yscale('log')
# p.set_xscale('log')
# p.set_xlim(1,10**15)
p.set_ylim(-0.001, 0.03)
p.plot(nlist,y_1_ts,label='1')
p.plot(nlist,y_n_ts,label='n')
p.plot(nlist,y_square_ts,label='n^2')
p.plot(nlist,y_squareroot_ts,label='sqrt(n)')
p.plot(nlist,y_nlogn_ts,label='nlogn')
p.plot(nlist,y_cude_ts,label='n^3')
p.plot(nlist,y_2n_ts,label='2^n')

# Add a legend
plt.xlabel('input (number)')
plt.ylabel('time (s)')
plt.xticks([])

plt.legend()
plt.show()

print(f'Total time taken: {taken}s')

