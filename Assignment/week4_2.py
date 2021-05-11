import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

#ここにマップから読み取った座標（緯度経度）を記入
# 未来大前の坂
x1 = [140.762557, 140.763327, 140.763671, 140.764038, 140.764463, 140.764953, 140.766006, 140.766695, 140.767796, 140.768864, 140.769961, 140.770678]
y1 = [41.835948, 41.836224, 41.836943, 41.837835, 41.838449, 41.838817, 41.838932, 41.839332, 41.840625, 41.841709, 41.842456, 41.842883]

f1 = interp1d(x1, y1, kind='cubic') # ３次スプライン補間, cubicは自然スプライン
x1_new = np.linspace(min(x1), max(x1), num=100, endpoint=True) # x軸の端から端を100分割

plt.plot(x1, y1, "o") # プロットした点の描画
plt.plot(x1_new, f1(x1_new), "-") # スプライン補間による描画
plt.xlim([min(x1), max(x1)])
plt.ylim([min(y1), max(y1)])
plt.legend(["Point", "Spline"], loc="best")
plt.show()