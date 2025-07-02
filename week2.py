# 1.数据加载和预处理
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 加载数据
data = pd.read_csv('US-pumpkins.csv')

# 查看数据的前几行
print(data.head())

# 数据预处理：将日期列转换为 datetime 类型
data['Date'] = pd.to_datetime(data['Date'])

# 填充缺失值
data.fillna(method='ffill', inplace=True)

# 查看数据的基本信息
print(data.info())

# 2.使用 Matplotlib 创建可视化图表
# 2.1时间序列图：南瓜价格随时间的变化
# 选择特定的南瓜品种和城市
filtered_data = data[(data['Variety'] == 'HOWDEN TYPE') & (data['City Name'] == 'BOSTON')]

# 绘制时间序列图
plt.figure(figsize=(14, 7))
plt.plot(filtered_data['Date'], filtered_data['Low Price'], label='Low Price', color='blue')
plt.plot(filtered_data['Date'], filtered_data['High Price'], label='High Price', color='red')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Pumpkin Prices Over Time in Boston', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True)
plt.savefig('time_series_plot.png')  # 保存图片
plt.show()

# 2.2条形图：不同城市的价格比较
# 选择特定的南瓜品种
filtered_data = data[data['Variety'] == 'HOWDEN TYPE']

# 计算每个城市的平均价格
city_prices = filtered_data.groupby('City Name')['Low Price'].mean().reset_index()

# 绘制条形图
plt.figure(figsize=(14, 8))
plt.bar(city_prices['City Name'], city_prices['Low Price'], color='skyblue')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average Low Price ($)', fontsize=12)
plt.title('Average Low Price of Howden Type Pumpkins by City', fontsize=14)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.savefig('bar_chart.png')  # 保存图片
plt.show()

# 2.3箱线图：不同城市的南瓜价格分布
# 选择特定的南瓜品种
filtered_data = data[data['Variety'] == 'HOWDEN TYPE']

# 绘制箱线图
plt.figure(figsize=(14, 8))
plt.boxplot([filtered_data[filtered_data['City Name'] == city]['Low Price'].dropna() for city in filtered_data['City Name'].unique()],
            labels=filtered_data['City Name'].unique())
plt.xlabel('City', fontsize=12)
plt.ylabel('Low Price ($)', fontsize=12)
plt.title('Distribution of Low Prices for Howden Type Pumpkins by City', fontsize=14)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.savefig('box_plot.png')  # 保存图片
plt.show()

# 3.使用 Seaborn 创建可视化图表
# 3.1时间序列图：南瓜价格随时间的变化
# 选择特定的南瓜品种和城市
filtered_data = data[(data['Variety'] == 'HOWDEN TYPE') & (data['City Name'] == 'BOSTON')]

# 绘制时间序列图
plt.figure(figsize=(14, 7))
sns.lineplot(x='Date', y='Low Price', data=filtered_data, label='Low Price', color='blue')
sns.lineplot(x='Date', y='High Price', data=filtered_data, label='High Price', color='red')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Pumpkin Prices Over Time in Boston', fontsize=1)
plt.legend(fontsize=10)
plt.grid(True)
plt.savefig('seaborn_time_series_plot.png')  # 保存图片
plt.show()

# 3.2条形图：不同城市的价格比较
# 选择特定的南瓜品种
filtered_data = data[data['Variety'] == 'HOWDEN TYPE']

# 计算每个城市的平均价格
city_prices = filtered_data.groupby('City Name')['Low Price'].mean().reset_index()

# 绘制条形图
plt.figure(figsize=(14, 8))
sns.barplot(x='City Name', y='Low Price', data=city_prices, palette='viridis')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average Low Price ($)', fontsize=12)
plt.title('Average Low Price of Howden Type Pumpkins by City', fontsize=14)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.savefig('seaborn_bar_chart.png')  # 保存图片
plt.show()

# 3.3箱线图：不同城市的南瓜价格分布
# 选择特定的南瓜品种
filtered_data = data[data['Variety'] == 'HOWDEN TYPE']

# 绘制箱线图
plt.figure(figsize=(14, 8))
sns.boxplot(x='City Name', y='Low Price', data=filtered_data)
plt.xlabel('City', fontsize=12)
plt.ylabel('Low Price ($)', fontsize=12)
plt.title('Distribution of Low Prices for Howden Type Pumpkins by City', fontsize=14)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.savefig('seaborn_box_plot.png')  # 保存图片
plt.show()

# 4.进一步的可视化分析
# 4.1 热力图：不同城市和品种的价格关系
# 创建一个透视表
pivot_table = data.pivot_table(values='Low Price', index='City Name', columns='Variety', aggfunc=np.mean)

# 绘制热力图
plt.figure(figsize=(14, 10))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='coolwarm', linewidths=.5)
plt.xlabel('Variety', fontsize=12)
plt.ylabel('City', fontsize=12)
plt.title('Average Low Price of Different Pumpkin Varieties by City', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.savefig('heatmap.png')  # 保存图片
plt.show()

# 4.2散点图：南瓜价格与包装大小的关系
# 选择特定的南瓜品种
filtered_data = data[data['Variety'] == 'HOWDEN TYPE']

# 绘制散点图
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Package', y='Low Price', data=filtered_data, hue='City Name', palette='viridis', style='City Name', s=100)
plt.xlabel('Package Size', fontsize=12)
plt.ylabel('Low Price ($)', fontsize=12)
plt.title('Relationship Between Package Size and Low Price', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(title='City', fontsize=10, title_fontsize=12)
plt.savefig('scatter_plot.png')  # 保存图片
plt.show()
