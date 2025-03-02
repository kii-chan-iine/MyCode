using ControlSystems
using Plots

# 定义系统的传递函数
numerator = [1.0]  # 分子多项式系数
denominator = [1.0, 2.0, 1.0]  # 分母多项式系数
sys = tf(numerator, denominator)  # 创建传递函数模型

# 计算阶跃响应
result = step(sys, 10)  # 模拟时间范围为 0 到 10 秒
# t, y = step(sys, 10)  # 模拟时间范围为 0 到 10 秒

plot(result)
println(result)
# println(typeof(result))



# A = 
#  -2.0  -1.0
#   1.0   0.0
# B =
#  1.0
#  0.0
# C =
#  0.0  1.0
# D = 
#  0.0