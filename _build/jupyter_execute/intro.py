#!/usr/bin/env python
# coding: utf-8

# # Mathematik für DataScience

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (16,8))

# first plot
ax = fig.add_subplot(1, 2, 1)

x = np.linspace(-2,2,100)
eps = [1e-3, 1e-2, 5e-2, 1e-1, 3e-1, 1]


colors = color=plt.cm.PiYG(np.linspace(0,1,len(eps)))
# plot
for i in range(len(eps)):
    y = np.sin(x)/(np.abs(x) + 10*eps[i]) # * np.abs(y)
    ax.plot(x, y,linewidth=1, color = colors[i])
    
    y_diff = 0.05*np.ones_like(y)
    ax.fill_between(x, y - y_diff, y + y_diff, color = colors[i], alpha = 0.1)

ax.axis('off')

# second plot
ax2 = fig.add_subplot(1, 2, 2)

for i in range(len(eps)):
    y = np.exp(-0.01/eps[i] * x**2) * np.abs(x)**0.5# * np.abs(y)
    ax2.plot(x, y,linewidth=1, color = colors[i])
    
    y_diff = 0.05*np.ones_like(y)
    ax2.fill_between(x, y - y_diff, y + y_diff, color = colors[i], alpha = 0.1)

ax2.axis('off')

# show
plt.show()


# Diese Vorlesung gibt einen ersten Einblick in grundlegende mathematische Konzepte und
# Denkweisen, die in der heutigen Mathematikausbildung in Vorlesungen zur Analysis und
# linearen Algebra unterteilt werden. In dieser Vorlesung soll eine integrierte Darstellung
# der wichtigsten Inhalte, wie sie in mathematiknahen Studiengängen benötigt werden, gegeben werden.
