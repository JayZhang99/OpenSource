import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import StandardScaler


file_paths = ['CC.csv', 'HV.csv', 'comment.csv', 'LOC.csv', 'function.csv', 'DDG.csv', 'CDG.csv']
output_paths = ['CC_normal.csv', 'HV_normal.csv', 'comment_normal.csv', 'LOC_normal.csv', 'function_normal.csv', 'DDG_normal.csv', 'CDG_normal.csv']

for input_path, output_path in zip(file_paths, output_paths):
    # 读取数据
    data = pd.read_csv(input_path)
    values = data.values.flatten()  
    transformed_data, _ = boxcox(values)
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data.reshape(-1, 1)).flatten() * (1/3) + 1
    output_df = pd.DataFrame(standardized_data, columns=['TransformedData'])
    # 将处理后的数据保存到CSV文件
    output_df.to_csv(output_path, index=False)

    print(f"Data from {input_path} transformed and saved to {output_path}")
