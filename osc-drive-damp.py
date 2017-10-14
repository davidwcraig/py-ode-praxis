
# coding: utf-8

# # This is a test notebook

# In[9]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
get_ipython().magic('matplotlib inline')


# ## Driven damped harmonic oscillator 

# In[21]:

def dosc(y,t,b,w0,f):
    """driven dampled harmonic oscillator derivs
    for scipy.integrate.odeint
    y -start vals
    t - time array
    b - damp coeff
    w0 - nat freq
    f - driving function
    """
    x,v = y
    dydt = [v,f(t)-2*b*v - w0*w0*x]
    return dydt

def g(t):
    """ simple drive, amp 0.1, omega = 1.0"""
    return 0.05*np.sin(t)
# example call:
# t = np.linspace(0,30*np.pi, 1000)
# y0 = [0.0, 0.0]
# sol = odeint(dosc, y0,t,args=(0.1,1.1,g))
# plt.plot(t, sol[:,0])
# plt.savefig("osc.svg")


# In[22]:

t = np.linspace(0,30*np.pi, 1000)   #independent variable array


# In[23]:

y0 = [0.5, -0.04] # initial [x,v]


# In[26]:

sol = odeint(dosc, y0,t,args=(0.1,1.05,g))


# In[27]:

plt.plot(t, sol[:,0])


# In[28]:

def p(a, b):  #making sure I understand lambda functions.
    return a + b


# In[32]:

lp = lambda x : p(x, 4)


# In[33]:

lp(3)


# In[34]:

def drive(t,a,w):
    """driving function, indep var t, amplitude a, ang freq w"""
    return a*np.cos(w*t)


# In[43]:

y0 = [0,0] # initial [x,v]


# In[44]:

sol = odeint(dosc, y0,t,args=(0.02,1.05,lambda x: drive(x,0.05,1.03)))


# In[45]:

plt.plot(t, sol[:,0])


# In[ ]:



