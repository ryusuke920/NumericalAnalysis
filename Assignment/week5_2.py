import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def fit_func(parameter, x , y):
    a = parameter[0]
    b = parameter[1]
    residual = y - (a * x + b)
    return residual

# 20人の年齢と体重のデータセット
# 年齢は25歳以下に限定
xdata = np.array([9, 21, 6, 18, 5,
              6, 7, 12, 10, 20,
              17, 3, 24, 9, 18,
              23, 12, 13, 16, 13])

ydata = np.array([29.01, 78.1, 18.78, 57.94, 14.81,
              22.34, 26.31, 41.69, 35.25, 60.92,
              69.08, 16, 66.39, 27.06, 68.03,
              61.45, 42.07, 40.64, 59.62, 32.22])

# Figureを作成
fig = plt.figure(figsize = (8, 6))

# FigureにAxesを１つ追加
ax = fig.add_subplot(111)

# Axesのタイトルを設定
ax.set_title("Age vs. Weight", fontsize = 16)

# 目盛線を表示
ax.grid()

# 軸範囲を設定
ax.set_xlim([0, 25])
ax.set_ylim([0, 90])

# 軸ラベルを設定
ax.set_xlabel("Age", fontsize = 14)
ax.set_ylabel("Weight [kg]", fontsize = 14)

# 身長と体重データの散布図
ax.scatter(xdata, ydata, color = "blue")

plt.show()

parameter0 = [0.,0.]
result = optimize.leastsq(fit_func,parameter0,args=(xdata,ydata))
print(result)
a_fit=result[0][0]
b_fit=result[0][1]

print(a_fit,b_fit)



#PLot
plt.figure(figsize=(8,5))
plt.plot(xdata,ydata,'bo', label='Exp.')
plt.plot(xdata,a_fit*xdata+b_fit,'k-', label='fitted line', linewidth=3, alpha=0.3)
#plt.plot(xdata,f(xdata),'r-', label='mother line', linewidth=3)
plt.xlabel('Age')
plt.ylabel('Weight')
plt.legend(loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()

# x 才の時の推定体重
x=15
print(x, "-->", a_fit*x+b_fit)              