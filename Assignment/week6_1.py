# ガウスーザイデル法
import numpy as np
from scipy import optimize

# １次元配列を表示するための関数用意
def disp_vector(row):
    for col in row:
        print('%14.10f ' % col)
    print("")

# ガウス・ザイデル法
def gauss(N, a, b, xs): # b: y の部分、xs: 答えとなるベクトルの初期値
    loop_counter = 0
    w = 1.2 # SOR方で使うパラメータ(加速係数)
    while True:
        loop_counter += 1
        x1 = 0.0
        finish = True
        for i in range(N):
            x1 = 0.0
            xi_new = 0.0
            for j in range(N):
                if (j != i):
                    x1 += a[i][j] * xs[j]

            #xi_new = (b[i] - x1) / a[i][i]  # ガウス・ザイデル法の更新式
            xi_new =  w * (b[i] - x1) / a[i][i] + (1 - w) * xs[i]  #SOR法の更新式
            if (abs(xi_new - xs[i]) > 0.0000000001):
                finish = False
            xs[i] = xi_new

        if (finish |(loop_counter> 300)):
            return

        print("Loop:", loop_counter)
        disp_vector(xs)

def setmatrix(): #計算対象の行列データをここに書いておく
    # 例題１
    a1_lis = [2, 2, 6]
    a2_lis = [3, 5, 13]
    a3_lis = [5, 8, 24] 
    a = [a1_lis, a2_lis, a3_lis]
    b = [24, 52, 93] 
    c = [0, 0, 0] 

    # テスト問題
    #a = [[ 2.0, 2.0, 6.0], [3.0, 5.0, 13.0], [5.0, 8.0, 24.0]]
    #b =  [24.0, 52.0, 93.0]
    #c =  [0.0, 0.0, 0.0] 

    N = len(c) #4 #連立方程式の数 問題に応じて書き換えること
    return a,b,c, N

# ガウス・ザイデル法の実行部分

a, b, c, N = setmatrix()  #計算する行列データを取得
print("matrix A=", a)
print("vect b=", b)
print("initial X=", c)
print("number of expression=", N)
gauss(N, a,b,c)  #ガウス・ザイデル法を実行

print("Final Answer")
disp_vector(c)