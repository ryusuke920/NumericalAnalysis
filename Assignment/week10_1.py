# https://qiita.com/Dr_ASA/items/d44560cf1367290aee6d

import matplotlib.pyplot as plt
import numpy as np

######################################################
# 微分方程式
def divf(x, y):
    return  y

######################################################
# Euler法
def euler(x, y, h, b):
  x_ap = [x]
  y_ap = [y]

  while x <= b:

    y += h * divf(x,y)
    x += h
    y_ap.append(y)
    x_ap.append(x)

  return x_ap, y_ap

######################################################
# ホイン法
def imp_euler(x, y, h, b):
  x_ap = [x]
  y_ap = [y]

  while x <= b:

    y_1 = y + h * divf(x,y)
    y += (divf(x,y) + divf((x + h),  y_1)) * h / 2.
    x += h

    y_ap.append(y)
    x_ap.append(x)

  return x_ap, y_ap

######################################################

# RK4法(4次)
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
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)

x0 = 0.0 # xの初期値
y0 = 1.0  # yの初期値
h = 0.5  # 刻み幅
b = 20  # xの最大値

# オイラー法のグラフ
x_a1 , y_a1 = euler(x0, y0, h, b)
ax.scatter(x_a1, y_a1, c='purple', label='Euler')

# ホイン法のグラフ
x_a2 , y_a2 = imp_euler(x0, y0, h, b)
ax.scatter(x_a2, y_a2, c='blue', label='imp_Euler')

# ルンゲクッタ法のグラフ
x_a3 , y_a3 = rk4(x0, y0, h, b)
ax.scatter(x_a3, y_a3, c='red', label='RungeKutta')

# 厳密解のプロット
x_analytical = np.linspace(x0, b, 100)
y_analytical = np.exp(x_analytical)
ax.plot(x_analytical,y_analytical,label='analytical', c="green")

# グラフタイトルなどの表示
ax.set_title('Euler')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='best')
ax.grid(True)

plt.show()