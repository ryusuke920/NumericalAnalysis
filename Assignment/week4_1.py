from scipy.interpolate import interp1d, lagrange
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, num=11)
y = 1.0 / (1.0 + x ** 2)
f_line = lagrange(x, y)
f_CS = interp1d(x,y, kind="cubic")  # ここを正しくプログラムすること　3次スプライン補間実行！

def yy(x):
    return 1.0 / (1.0 + x ** 2)  #資料を見て完成させてください

xnew = np.linspace(-5, 5, num=51)

y_lis_exact=[]
for j in xnew:
    y_lis_exact.append(yy(j))

plt.plot(x, y, 'x',   xnew, f_line(xnew), '-')
plt.plot(x, y, 'o',   xnew, f_CS(xnew), '-')

plt.legend(['Raw data', 'Lagrange', 'point','spline'], loc='best')

plt.xlim([-6, 6])
plt.ylim([-1, 2])
plt.show()