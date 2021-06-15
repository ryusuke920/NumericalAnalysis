# モンテカルロ積分
import numpy as np
from random import random

def f(x):
    return 1.0/(1.0+x**2) # 関数の定義

"""
単純モンテカルロ積分法: 試行回数 Nを10から10^7まで変化させる
"""
N_calc_list = [10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7]

for N in  N_calc_list:
    count = 0.0
    for i in range(N):
        x = random()  # [0,1]までの一様乱数をxに格納
        y = random()  # [0,1]までの一様乱数をyに格納
        if y < f (x):   #もし”マト”に入ったらそれをカウントする
            count +=1.0
    area = 4*count/N # 積分結果。 π の評価

    print(N, ", ", area, ", ", abs((np.pi-area)/np.pi)) #結果の出力
        