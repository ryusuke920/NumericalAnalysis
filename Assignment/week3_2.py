from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

# メイン
x = [-2, 2, 4]
y = [8, 4, 14]
f_Lag = lagrange(x, y) # ラグランジュ補間実行

def f(X):
    return (((X - x[1]) * (X - x[2])) / ((x[0] - x[1]) * (x[0] - x[2])) * y[0]) +\
        (((X - x[0]) * (X - x[2])) / ((x[1] - x[0]) * (x[1] - x[2])) * y[1]) +\
            (((X - x[0]) * (X - x[1])) / ((x[2] - x[0]) * (x[2] - x[1])) * y[2])

#for plot
xnew = np.linspace(-5, 5, num = 51) # [-5, 5]の範囲を51等分して xnew に格納

# 正解データの生成
y_lis_exact=[]
for j in xnew:
    y_lis_exact.append(f(j))

plt.plot(x, y, 'o',  xnew, f_Lag(xnew), '-')
plt.plot(xnew, y_lis_exact, color = 'Black',label = 'Exact')
plt.legend(['Raw data', 'Lagrange'], loc = 'best')
plt.xlim([-6, 6]) # x軸のプロット範囲 
plt.ylim([0, 16]) # y軸のプロット範囲
plt.show()