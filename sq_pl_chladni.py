#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from mpl_toolkits.mplot3d.axes3d import Axes3D
import Tkinter as tk
import sys

l=2.0
r=0.1
#x = np.arange(0.0, 10.0, r)
#y = np.arange(0.0, 10.0, r)
x = np.arange(-2.0, 2.0, r)
y = np.arange(-2.0, 2.0, r)
X, Y = np.meshgrid(x, y)
def sel():
   n = float(var1.get())
   m = float(var2.get())
   print("n= ",n)
   print("m= ",m)
g = tk.Tk()
g.wm_title("Embedding in TK")

var1 = tk.DoubleVar()
var2 = tk.DoubleVar()
n0 = tk.Scale( g, orient=tk.HORIZONTAL, label="n =", length=250, variable=var1, from_=0)
n0.pack(anchor=tk.CENTER)

m0 = tk.Scale( g, orient=tk.HORIZONTAL, label="m =", length=250, variable=var2, from_=1)
m0.pack(anchor=tk.CENTER)

#button = Button(root, text="Get Scale Value", command=sel)
#button.pack(anchor=CENTER)
def pg():
 n = float(var1.get())
 m = float(var2.get())
 if n==m:
  print("modes n and m cannot equal")
 else:
  Z = np.cos(3.14*n*X/l)*np.cos(3.14*m*Y/l) - np.cos(3.14*m*X/l)*np.cos(3.14*n*Y/l)
  f = plt.figure()
  print('modes: n=', n, 'm=', m)
#  plt.title( n m, fontsize=20)
#  plt.xlabel('xlabel', fontsize=18)
#  plt.ylabel('ylabel', fontsize=16)
  plt.contourf(X, Y, Z, 100, rstride=1, cstride=1, cmap=cm.Spectral)
  plt.colorbar()
  plt.show(f)
button = tk.Button(g, text="Plot with selected modes", command=pg)
button.pack(anchor=tk.CENTER)
b1 = tk.Button(master=g, text='Quit', command=sys.exit)
b1.pack(side = tk.TOP)
g.mainloop()
#sys.exit()
