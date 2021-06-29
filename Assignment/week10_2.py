# https://qiita.com/Dr_ASA/items/d44560cf1367290aee6d

import matplotlib.pyplot as plt
import numpy as np

######################################################
# 微分方程式
def divf(x, y):
    return  (-1.245 * 10 ** (-4.0))* y

######################################################

# RK4法
def rk4(x, y, h, b):
  x_ap = [x]
  y_ap = [y]

  while x <= b:

    k1 = h * divf(x,y)
    k2 = h * divf((x + (h / 2.0)), (y + (k1 / 2.0)))
    k3 = h * divf((x + (h / 2.0)), (y + (k2 / 2.0)))
    k4 = h * divf((x + h), (y + k3))
    y += (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    x += h

    y_ap.append(y)
    x_ap.append(x)

  return x_ap, y_ap  

######################################################

# グラフ領域の定義
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

x0 = 0.0 # xの初期値
y0 = 6.68 # yの初期値
h = 1  # 刻み幅
b = 35000  # xの最大値

# ルンゲクッタ法のグラフ
x_a3 , y_a3 = rk4(x0, y0, h, b)
ax.scatter(x_a3, y_a3, c='red', label='RungeKutta')

# グラフタイトルなどの表示
ax.set_title('Euler')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='best')
ax.grid(True) 

plt.show()