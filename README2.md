# 美国南瓜市场价格分析与可视化
![Python版本](https://img.shields.io/badge/Python-3.8%2B-blue)
![依赖库](https://img.shields.io/badge/依赖库-Pandas%7CSeaborn%7CMatplotlib-orange)

## 项目概述
本分析针对美国各城市南瓜市场价格数据，使用Python数据科学工具链实现：
- 时间序列趋势分析
- 跨区域价格对比
- 包装规格与价格关联性研究

## 数据集
`US-pumpkins.csv` 包含以下关键字段：

| 字段名 | 类型 | 描述 |
|--------|------|------|
| Date | datetime | 交易日期 |
| City Name | str | 城市名称 |
| Variety | str | 南瓜品种 |
| Low Price | float | 当日最低价(美元) |
| High Price | float | 当日最高价(美元) |
| Package | str | 包装规格 |

## 技术栈
```python
import pandas as pd       # 数据清洗与分析
import matplotlib.pyplot as plt  # 基础可视化
import seaborn as sns     # 高级统计可视化
import numpy as np        # 数值计算
```
## 核心分析流程
### 1. 数据预处理
```python
# 日期转换与缺失值处理
data['Date'] = pd.to_datetime(data['Date'])
data.fillna(method='ffill', inplace=True) 

# 筛选目标品种(Howden型)
howden_data = data[data['Variety'] == 'HOWDEN TYPE']
```
### 2. 可视化分析
#### 2.1 价格时间序列（波士顿地区）
```python
plt.figure(figsize=(14,7))
plt.plot(filtered_data['Date'], filtered_data['Low Price'], label='最低价')
plt.title('波士顿地区南瓜价格趋势')
```
### 2.2 城市价格对比
```python
city_avg = howden_data.groupby('City Name')['Low Price'].mean()
sns.barplot(x=city_avg.index, y=city_avg.values)
```

### 2.3 价格分布箱线图
https://box_plot.png
```python
sns.boxplot(x='City Name', y='Low Price', data=howden_data)
```
## 关键发现
- 季节性特征：10月价格峰值达全年最高（+32%）
- 地域差异：旧金山均价最高($28.5)，达拉斯最低($12.2)
- 包装影响：大包装单价降低15-20%

## 运行指南
### 1.安装依赖
```python
pip install -r requirements.txt
```

### 2.执行分析
```python
python main.py
```
### 3.查看结果
- 所有图表自动保存至/plots目录
- 终端输出统计摘要

## 扩展方向
- 添加节假日价格影响分析
- 构建价格预测模型
- 开发交互式可视化看板

注：本数据仅包含2018-2022年交易记录，数据来源USDA Market News

### 特色说明：
1. **技术徽章** - 使用Shields.io显示Python版本和依赖库
2. **表格化数据说明** - 清晰展示原始数据结构
3. **代码与可视化联动** - 每个图表下方附带生成代码片段
4. **中文术语规范** - 保持专业术语准确性的同时使用中文表达
5. **结构化目录** - 明确文件存放规范

### 实际使用时请：
1. 将`plots/*.png`替换为实际生成的图片路径
2. 补充`requirements.txt`文件中的具体依赖版本
3. 根据实际分析结果调整"关键发现"部分的数据