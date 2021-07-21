import matplotlib.pyplot as plt
import numpy as np
import math

######################################################
# 微分方程式
def divf1(x, z, ux, uz):
    return  ux # 

def divf2(x, z, ux, uz):
    return  uz  # ここを完成させる

def divf3(x, z, ux, uz):
  if math.sqrt(ux*ux + uz*uz) > 0.0001:
    Dx = -1.0 * D * ux/math.sqrt(ux*ux + uz*uz)
    return Dx/m
  else:
    return 0.

def divf4(x, z, ux, uz):
  if math.sqrt(ux*ux + uz*uz) > 0.0001 : 
    Dz= -1.0 * D * uz/math.sqrt(ux*ux + uz*uz)
    return  Dz/m - g  ##### ここを完成させる
  else:
    return - g

######################################################

# RK4法
def rk4(t, x, z, ux, uz, h, b):
  x_ap = [x]
  z_ap = [z]


  while t <= b:

    D = 0.5 * 1.176 * (ux * ux + uz * uz) * 3.13159 * 0.036 * 0.44

    k0[0]= h * divf1(x, z, ux, uz);
    k0[1]= h * divf2(x, z, ux, uz);
    k0[2]= h * divf3(x, z, ux, uz);
    k0[3]= h * divf4(x, z, ux, uz);   

    k1[0]= h * divf1(x+k0[0]/2.0, z+k0[1]/2.0, ux+k0[2]/2.0, uz+k0[3]/2.0);
    k1[1]= h * divf2(x+k0[0]/2.0, z+k0[1]/2.0, ux+k0[2]/2.0, uz+k0[3]/2.0);
    k1[2]= h * divf3(x+k0[0]/2.0, z+k0[1]/2.0, ux+k0[2]/2.0, uz+k0[3]/2.0);
    k1[3]= h * divf4(x+k0[0]/2.0, z+k0[1]/2.0, ux+k0[2]/2.0, uz+k0[3]/2.0);

    k2[0]= h * divf1(x+k1[0]/2.0, z+k1[1]/2.0, ux+k1[2]/2.0, uz+k1[3]/2.0);
    k2[1]= h * divf2(x+k1[0]/2.0, z+k1[1]/2.0, ux+k1[2]/2.0, uz+k1[3]/2.0);
    k2[2]= h * divf3(x+k1[0]/2.0, z+k1[1]/2.0, ux+k1[2]/2.0, uz+k1[3]/2.0);
    k2[3]= h * divf4(x+k1[0]/2.0, z+k1[1]/2.0, ux+k1[2]/2.0, uz+k1[3]/2.0);

    k3[0]= h * divf1(x+k2[0], z+k2[1], ux+k2[2], uz+k2[3]);
    k3[1]= h * divf2(x+k2[0], z+k2[1], ux+k2[2], uz+k2[3]);
    k3[2]= h * divf3(x+k2[0], z+k2[1], ux+k2[2], uz+k2[3]);
    k3[3]= h * divf4(x+k2[0], z+k2[1], ux+k2[2], uz+k2[3]);

    dx =  (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0
    dz =  (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0
    dux = (k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0
    duz = (k0[3]+2.0*k1[3]+2.0*k2[3]+k3[3])/6.0    

    x = x + dx
    z = z + dz
    ux = ux + dux
    uz = uz + duz    

   # write([t,x,y,z])
   # print(t,x,y,z, k0,k1,k2,k3)
    t = t + h

    z_ap.append(z)
    x_ap.append(x)

  return x_ap, z_ap  
######################################################
# グラフ領域の定義
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

t=0
x0= -18.44+1.8 # xの初期値
z0= 2.2 # yの初期値
##########################
# 以下３つをを適当に変更する
theta= -2.7
Velocity = 165  #速度 km/s # 
b = 0.4  # tの最大値（秒）
##########################
sVelocity = Velocity * 1000/3600 # 速度　m/s 大谷　45.833 m/s
ux0 =  sVelocity* math.cos(theta/180. * 3.14159) # 45.833
uz0 = sVelocity * math.sin(theta/180. * 3.14159)
h = 0.01  # 刻み幅

m = 0.145
g = 9.80665
D = 0 
k0 = [0,0,0,0]
k1 = [0,0,0,0]
k2 = [0,0,0,0]
k3 = [0,0,0,0]


# ルンゲクッタ法のグラフ
x_a3 , z_a3 = rk4(t, x0, z0, ux0, uz0, h, b)
ax.scatter(x_a3, z_a3, c='red', label='RungeKutta')

# グラフタイトルなどの表示
ax.set_title('RungeKutta')
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.legend(loc='best')
ax.plot([-18.44+1.8, 0.0], [2.2, 0.8], 'k-', lw=2)

ax.grid(True) 
plt.show()