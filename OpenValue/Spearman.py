import pandas as pd
from scipy.stats import spearmanr

# 读取数据
data1 = pd.read_csv('OpenValue.csv')
data2 = pd.read_csv('Real.csv')

# 确保数据一致性，这里假设数据文件中各自只有一列数据
if len(data1) != len(data2):
    raise ValueError("数据集长度不一致，无法计算相关性！")

# 计算Spearman相关性
spearman_correlation, p_value = spearmanr(data1.iloc[:, 0], data2.iloc[:, 0])

# 存储结果到CSV文件
results = pd.DataFrame({
    'Spearman_Correlation': [spearman_correlation],
    'P_Value': [p_value]
})
results.to_csv('spearman_correlation_results.csv', index=False)

print("Spearman相关性计算完成，结果已存储到 'spearman_correlation_results.csv'。")
