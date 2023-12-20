import numpy as np
import matplotlib.pyplot as plt

# def speedup(percent_encryption, rate = 30):
#     return 1 / (percent_encryption / rate + 1 - percent_encryption)

# percent_encryption = np.linspace(0, 1, 100)  # 生成0到1之间的100个等间距的数作为横坐标
# rate = 30  # 设置运算速度比正常执行模式快的值
# # print(speedup(0.69))
# output = speedup(percent_encryption, rate)  # 计算函数输出结果

# plt.plot(percent_encryption, output)  # 绘制图像
# plt.xlabel('percent_encryption')  # 设置横坐标标签
# plt.ylabel('new speedup')  # 设置纵坐标标签
# # plt.title('')  # 设置图像标题
# plt.grid(True)  # 添加网格线
# plt.savefig('speedup_with_percent.png', dpi = 600)
# plt.show()  # 显示图像

# 提供的点
points = [(1, 100), (3.84, 384), (10, 384)]

# 提取 x 和 y 坐标
x_values, y_values = zip(*points)

# 画折线图
plt.plot(x_values, y_values, marker='o', linestyle='-', color='c')
# 标注点的坐标
for point in points[:2]:
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', ha='left', va='bottom')

# 添加标签和标题
plt.xlabel('Flops/byte')
plt.ylabel('GFLOPS/s')
plt.title('Roofline Model')

# 显示图形
plt.savefig("roofline_hw3.png", dpi = 1000)
plt.show()
