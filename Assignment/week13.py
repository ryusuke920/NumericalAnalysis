import matplotlib.pyplot as plt
import numpy as np
import math

######################################################

# RK4法
k0=[0,0]
k1=[0,0]
k2=[0,0]
k3=[0,0]

def rk4(t, x, y, h, b):
  x_ap = [x]
  y_ap = [y]
  t_ap = [t]

  while t <= b:

    k0= h * lotka(x, y);

    k1= h * lotka(x+k0[0]/2.0, y+k0[1]/2.0);

    k2= h * lotka(x+k1[0]/2.0, y+k1[1]/2.0); 

    k3= h * lotka(x+k2[0], y+k2[1]);

    dx =  (k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0;
    dy =  (k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0;

    x = x + dx
    y = y + dy 

   # write([t,x,y,z])
    #print(t,x,y)
    t = t + h

    y_ap.append(y)
    x_ap.append(x)
    t_ap.append(t)

  return x_ap, y_ap, t_ap  
  ######################################################

    ######################################################
# 微分方程式
#def lotka(x, y, a=8, b=3, c=4 ,d=18):
def lotka(x, y, a=1., b=0.10, c= 0.5 ,d=0.02):
    x_dot = x * (0.1 - 0.0007 * x - 0.001 * y)
    y_dot = y * (0.075 - 0.0007 * x - 0.0007 * y)
    return np.array([x_dot, y_dot])

######################################################


t=0
#x0 = [4]
#y0 = [10]
x0=[1.0, 2.0, 4.0, 5.0, 23.8] # xの初期値　問題文に合わせて設定せよ
y0=[25.0, 20.0, 10.0, 5.0, 83.3]  # yの初期値　問題文に合わせて設定せよ
##########################
b = 10000.0  # tの最大値  変化の方向を確かめるとともに，適切な値に設定せよ
##########################
h = 0.05  # 刻み幅


# グラフ領域の定義
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

fig2 = plt.figure(figsize=(20,10))
bx = fig2.add_subplot(1,1,1)

cl=['r', 'g', 'b', 'y', '#00fa9a']
for i in range(5):
  # ルンゲクッタ法のグラフ
  print(x0[i], y0[i])
  x_a3 , y_a3, t_a3 = rk4(t, x0[i], y0[i], h, b)
  ax.scatter(x_a3, y_a3, c=cl[i], label= str(i))
  bx.plot(t_a3, x_a3, marker="o", c=cl[i], label= str(i))
  bx.plot(t_a3, y_a3, marker="v", c=cl[i], label= str(i))

# 捕食者と被食者の相図 Phase Graph
ax.set_title('Lotka-Volterra Phase Graph')
ax.set_xlabel('N1')
ax.set_ylabel('N2')
ax.legend(loc='best')
ax.grid(True) 

#捕食者と被食者の個体数の時間変化をグラフ化
bx.set_title('Lotka-Volterra Time series')
bx.set_xlabel('t')
bx.set_ylabel('N1 and N2')
bx.legend(loc='best')

plt.show()
