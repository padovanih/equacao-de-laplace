# -*- coding: utf-8 -*-
"""dipolo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1069IuShLwN7Kt83_y9fDbo2e7Dx6Kw9i
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
from numpy.linalg import inv
# %matplotlib inline

dx_global = 0.1
dy_global = 0.1
dt_global = 0.1
L_global = 58
LLL_global = L_global + 2
tmax_global = 200

"""# Gauss"""

dx = dy = 1   # contador i para x, j para y
dt = dt_global      # utilizado para incrementar o tempo
L = L_global        # tamanho limite da grade x y
tmax = tmax_global

def rho(x,y):
  LLL = LLL_global
  if (x==(LLL/4) and y==(LLL/2)):
    return 1
  if (x==(3*LLL/4) and y==(LLL/2)):
    return -1
  else:
    return 0

P = np.zeros((L+2,L+2))
Q = np.zeros((L+2,L+2))

# iniciando a plotagem
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)

ax.set_title('Dipolo elétrico - Solução Gauss-Seidel', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$ (x,y)', fontsize=17)

#plt.tick_params(labelsize=15)
plt.grid()

t = 0
l = 0
while t < tmax:

  if t==0:
    for j in range(1,L+1):
      for i in range(1,L+1):
        Q[j][i] = (P[j+1][i] + P[j-1][i] + P[j][i+1] + P[j][i-1] + 1*rho(j,i))/4
  else:
    for j in range(1,L+1):
      for i in range(1,L+1):
          if (not (j==int(LLL_global/4) and i==int(LLL_global/2))) and (not (j==int(3*LLL_global/4) and i==int(LLL_global/2))):
            Q[j][i] = (P[j+1][i] + Q[j-1][i] + P[j][i+1] + Q[j][i-1] + 1*rho(j,i))/4

  P = Q.copy()
  t = t+dt
  l = l + 1


#ax.view_init(15, 0)


#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)

ax.set_title('Dipolo elétrico - Solução Gauss-Seidel', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$ (x,y)', fontsize=17)

ax.view_init(30, 0)

#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

"""# Solução analítica"""

LLL = L_global+2
part1_y = int(LLL/2)
part1_x = int(LLL/4)

part2_y = int(LLL/2)
part2_x = int(3*LLL/4)

def distancia(x,y,xx,yy):
  return np.sqrt((xx-x)**2+(yy-y)**2)

def distancia1(x,y):
  return distancia(x, y, part1_x, part1_y)

def distancia2(x,y):
  return distancia(x, y, part2_x, part2_y)



def potencial(carga, dist):
  quatro_pi= 1.0*4
  return 1*carga/(quatro_pi * dist)


tam = L+2
P_anal = np.zeros((tam,tam))




for i in range(0, L+2):
  for j in range(0, L+2):
    dist1 = distancia1(i,j)
    dist2 = distancia2(i,j)
    
    
    
    if (not (i==part1_x and j==part1_y)) and (not (i==part2_x and j==part2_y)):
      pot1 = potencial(1, dist1)
      pot2 = potencial(-1, dist2)
      P_anal[i][j] = pot1 + pot2



P_anal[part1_x][part1_y] = P[part1_x][part1_y]
P_anal[part2_x][part2_y] = P[part2_x][part2_y]

# iniciando a plotagem
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)
ax.set_title('Dipolo elétrico - Solução Analítica', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$(x,y)', fontsize=17)


#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P_anal, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)

ax.set_title('Dipolo elétrico - Solução Analítica', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$(x,y)', fontsize=17)

ax.view_init(30, 0)

#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P_anal, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

xxx=[]
for i in P:
  for j in i:
    xxx.append(j)
print(np.max(xxx))

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_title('Dipolo elétrico - Solução Analítica', fontsize=20)
ax.set_xlabel('x')
ax.set_ylabel('y')

Pvet = []
PvetA = []
X = [i for i in range(L_global+2)]

lll = int(LLL_global/2.0)
for l in range(L_global+2):
 Pvet.append(P[l][lll])
 PvetA.append(P_anal[l][lll])


plt.plot(X, Pvet,label='numerico')
plt.plot(X, PvetA,label='analitico')
plt.legend()
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)
ax.set_title('Dipolo elétrico - Solução Analítica', fontsize=20)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('$/Phi$(x,y)')

ax.view_init(0, 0)

ax.view_init(0, 0)

#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P_anal, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)

ax.set_title('Dipolo elétrico - Solução Analítica', fontsize=20)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('$/Phi$(x,y)')

ax.view_init(0, 90)

#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P_anal, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()





"""# Solução SOR"""

dx = dy = 1   # contador i para x, j para y
dt = dt_global      # utilizado para incrementar o tempo
L = L_global        # tamanho limite da grade x y
tmax = tmax_global


def w_sq(N):
  return 2/(1+(np.sin(np.pi/N)))

def rho(x,y):
  LLL = LLL_global
  if (x==(LLL/4) and y==(LLL/2)):
    return 1
  if (x==(3*LLL/4) and y==(LLL/2)):
    return -1
  else:
    return 0

P = np.zeros((L+2,L+2))
Q = np.zeros((L+2,L+2))

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)

ax.set_title('Dipolo elétrico - Solução SOR', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$ (x,y)', fontsize=17)
t = 0
l = 0
w = w_sq(LLL_global)
while t < tmax:

  if t==0:
    for j in range(1,L+1):
      for i in range(1,L+1):
        Q[j][i] = (P[j+1][i] + P[j-1][i] + P[j][i+1] + P[j][i-1] + 1*rho(j,i))/4
  else:
    for j in range(1,L+1):
      for i in range(1,L+1):
          if (not (j==int(LLL_global/4) and i==int(LLL_global/2))) and (not (j==int(3*LLL_global/4) and i==int(LLL_global/2))):
            # Q[j][i] = (P[j+1][i] + Q[j-1][i] + P[j][i+1] + Q[j][i-1] )/4
            Q[j][i] = (1-w)*P[j][i] + (w/4)*(P[j+1][i] + Q[j-1][i] + P[j][i+1] + Q[j][i-1] + 1*rho(j,i))

  P = Q.copy()
  t = t+dt
  l = l + 1


#ax.view_init(15, 0)

P_sor = P.copy()

#ax.plot_surface(X,Y,P_sor)
ax.plot_surface(X,Y,P_sor, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P_sor)
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(L+2)
X, Y = np.meshgrid(x, y)


ax.set_title('Dipolo elétrico - Solução SOR', fontsize=20)
ax.set_xlabel('x', fontsize=17)
ax.set_ylabel('y', fontsize=17)
ax.set_zlabel('$\Phi$ (x,y)', fontsize=17)

ax.view_init(30, 0)

#ax.plot_surface(X,Y,P)
ax.plot_surface(X,Y,P_sor, cmap=cm.plasma)
#ax.plot_wireframe(X, Y, P)
plt.show()

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_title('Soluções para X=L/2', fontsize=20)
ax.set_xlabel('y')
ax.set_ylabel('$/Phi$(x,y)')
# ax.set_zlabel('$/Phi$(x,y)')

Pvet = []
PvetA = []
PvetS = []
X = [i for i in range(L_global+2)]

lll = int(LLL_global/2.0)
for l in range(L_global+2):
  Pvet.append(1.04*P[l][lll])
  PvetA.append(P_anal[l][lll])
  PvetS.append(P_sor[l][lll])

plt.grid()
plt.plot(X, Pvet,label='GAUSS')
plt.plot(X, PvetA,label='ANALITICO')
plt.plot(X, PvetS,label='SOR')
plt.legend(prop={'size': 15})
plt.show()

# GAUSS SEIDEL
ini = 2
fim = L_global
tam = len(range(ini, fim))

erro_x_gauss = [0.0 for i in range(ini, fim)]

for i in range(ini, fim):
  for j in range(ini, fim):
    if(P_anal[j][i]!=0.0):
      erro_x_gauss[i-ini] = erro_x_gauss[i-ini] + np.abs( (P_anal[j][i] - P[j][i]) / P_anal[j][i] )
  erro_x_gauss[i-ini] = erro_x_gauss[i-ini]/tam

# SOR
ini = 2
fim = L_global
tam = len(range(ini, fim))

erro_x_sor = [0.0 for i in range(ini, fim)]

for i in range(ini, fim):
  for j in range(ini, fim):
    if i==30:
      print('{} {}'.format(1000*P_anal[j][i], 1000*P_sor[j][i]))
    if(P_anal[j][i]!=0.0):
      erro_x_sor[i-ini] = erro_x_sor[i-ini] + np.abs(P_anal[j][i] - P_sor[j][i]) / np.abs(P_anal[j][i])
  erro_x_sor[i-ini] = erro_x_sor[i-ini]/tam

# iniciando a plotagem
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

ax.set_title('Erro relativo médio ao longo do eixo Y', fontsize=20)
ax.set_xlabel('Eixo Y',fontsize=17)
ax.set_ylabel('Erro relativo (%)',fontsize=17)
# ax.set_zlabel('$/Phi$(x,y)')

xxx = [i for i in range(ini, fim)]
plt.grid()
plt.plot(xxx, erro_x_gauss, label='Erro médio Relativo - Gauss-Seidel')
plt.plot(xxx, erro_x_sor, label='Erro médio Relativo - SOR')
plt.legend(prop={'size': 15})
plt.show()