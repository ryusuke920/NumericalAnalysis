# https://qiita.com/Dr_ASA/items/d44560cf1367290aee6d
import matplotlib.pyplot as plt
import numpy as np

# 微分方程式
def divf(x, y):
    return  x * y

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

# ホイン法
def imp_euler(x, y, h, b):
  x_ap = [x]
  y_ap = [y]

  while x <= b:
    y_1 = y + h * divf(x,y)
    y += (divf(x,y) + divf((x + h),  y_1)) * h / 2
    x += h
    y_ap.append(y)
    x_ap.append(x)

  return x_ap, y_ap    

# グラフ領域の定義
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)

x0 = 0.0 # xの初期値
y0 = 1.0 # yの初期値
h = 0.01 # 刻み幅
b = 0.5 # xの最大値

# オイラー法のグラフ
x_a, y_a = euler(x0, y0, h, b)
ax.scatter(x_a, y_a, c='purple', label='Euler')

# ホイン法のグラフ
x_a , y_a = imp_euler(x0, y0, h, b)
ax.scatter(x_a, y_a, c='blue', label='imp_Euler')

# 厳密解のプロット
x_analytical = np.linspace(0, b, 100)
y_analytical = np.exp(x_analytical * x_analytical * 0.5)
ax.plot(x_analytical,y_analytical,label='analytical', c="green")

# グラフタイトルなどの表示
ax.set_title('Euler')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='best')
ax.grid(True) 
plt.show()  