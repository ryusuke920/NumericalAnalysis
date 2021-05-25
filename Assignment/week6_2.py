# SOR法
# http://fornext1119.web.fc2.com/NumericOperation/vol_06/Text/10_02_06.xhtml
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

N = 3

# １次元配列を表示
def disp_vector(row):
    for col in row:
        print('%14.10f ' % col)
    print("")

# SOR法
def SOR(a, b, x0, w):
    loop_counter=0
    #w=1.5
    while True:
        loop_counter+=1
        x1 = 0.0
        finish = True
        for i in range(N):
            x1 = 0
            for j in range(N):
                if (j != i):
                    x1 += a[i][j] * x0[j]

           # x1 = (b[i] - x1) / a[i][i]  # ガウス・ザイデル法
            x1 = w * (b[i] - x1) / a[i][i] + (1 - w) * x0[i]  #SOR法
            if (abs(x1 - x0[i]) > 0.0000000001):
                finish = False
            x0[i] = x1

        if (finish):
            return loop_counter

        #print("loop=",loop_counter )
        #disp_vector(x0)

def setmatrix():
    # 例題１
    #a1_lis = [2, 2, 6]
    #a2_lis = [3, 5, 13]
    #a3_lis = [5, 8, 24] 
    #a=[a1_lis, a2_lis, a3_lis]
    #b =  [24, 52, 93] 
    #c =  [ 0, 0, 0] 

    a = [[2.0, 2.0, 6.0], [3.0, 5.0, 13.0], [5.0, 8.0, 24.0]]
    b = [24.0, 52.0, 93.0]
    c = [0.0, 0.0, 0.0]
    return a, b, c


# SOR-Loop
w_array, w_result = [], []
w = 1.0
while w < 2.0:
    loop_counter = 0
    a,b,c=setmatrix()
    loop_counter =SOR(a,b,c, w)
    print("w=", w, "loop=", loop_counter)
    disp_vector(c)
    w_array.append(w)
    w_result.append(loop_counter)
    w += 0.1

plt.plot(w_array,w_result, 'o', color='Red',label='LoopC') #正解データのプロット
plt.legend(['w','LoopC'], loc='best')  # legendの指定
#plt.xlim([-7, 7])  # x軸のプロット範囲 
#plt.ylim([-4, 4]) # y軸のプロット範囲
plt.show()