"""
シンプソン則とロンバーグ則
"""
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

err_trape, err_simps, err_romb = [], [], []

nn = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048] # 4から2048までのグリッド数をリストnnに格納

for j in nn:
    #num=j+1
    x = np.linspace(0, 1, j) # 積分範囲をj個で分割 ※ロンバーグの時は+1にする(numを使う)
    y = 4 / (1 + x ** 2)
    y_integrate_trape = integrate.cumtrapz(y, x) #台形則による数値積分計算
    y_integrate_simps = integrate.simps(y, x)     #シンプソン則による数値積分計算
    y_integrate_romb = integrate.romb(y, x[1] - x[0])        #ロンバーグ則による数値積分計算
    err_trape.append(abs(np.pi - y_integrate_trape[-1]) / np.pi)  # 台形則による数値積分の相対誤差評価
    err_simps.append(abs(np.pi - y_integrate_simps) / np.pi)     # シンプソン則による数値積分の相対誤差評価
    err_romb.append(abs(np.pi - y_integrate_romb) / np.pi)  #ロンバーグ則による数値積分の相対誤差
    #print("j:", j, " ", y_integrate_trape[-1], ", ", y_integrate_simps,'\n')
    print("j:", j, " ", y_integrate_trape[-1], ", ", y_integrate_simps,", ", y_integrate_romb,'\n')

# for plot
ax = plt.gca()
ax.set_yscale('log')  # y軸をlogスケールで描く
ax.set_xscale('log')  # x軸をlogスケールで描く
plt.plot(nn,err_trape,"-", color='blue', label='Trapezoid rule')
plt.plot(nn,err_simps,"-", color='red', label='Simpson rule')
plt.plot(nn,err_romb,"-", color='orange', label='Romberg rule')
plt.xlabel('Number of grids',fontsize=18)
plt.ylabel('Error (%)',fontsize=18)
plt.grid(which="both") # グリッド表示。"both"はxy軸両方にグリッドを描く。
plt.legend(loc='upper right')
plt.show()