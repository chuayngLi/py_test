import matplotlib.pyplot as plt

# 数据
categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']
values = [10, 15, 7, 10, 5]

# 创建条形图
plt.bar(categories, values)

# 为每个条形添加数值标签
for i, v in enumerate(values):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10)  # 添加字号才能在对应的大小下看到数字

# 添加标题和标签
plt.title('My Bar Chart with Numbers')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图形
plt.show()
