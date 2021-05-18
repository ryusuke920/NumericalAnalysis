import numpy as np

# 行列Aの生成
a1_lis = [0, -3, 2]
a2_lis = [1, -1, -2]
a3_lis = [4, 1, -2] 
A_matrix=np.array([a1_lis, a2_lis, a3_lis])

# b vector
b = np.array([4, 5, 4]) # 行ベクトルとしてｂを生成し，それの転置行列として"列ベクトル”を生成する

x_vec = np.linalg.solve(A_matrix,b) # xベクトルを計算する。行列の積に@演算子を使っている(参考)

print(x_vec)

## >>> [ 1. -2. -1.]