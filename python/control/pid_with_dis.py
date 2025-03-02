#%%
import numpy as np
import matplotlib.pyplot as plt

# PID调节器参数
Kp = 1.2  # 比例增益
Ki = 0.1  # 积分增益
Kd = 0.05  # 微分增益

# 系统参数
setpoint = 10.0  # 目标值
process_value = 0.0  # 初始过程值
integral = 0.0  # 积分项初始值
previous_error = 0.0  # 上一次的误差
dt = 0.1  # 时间步长
simulation_time = 20  # 模拟总时间
time = np.arange(0, simulation_time, dt)  # 时间序列

# 扰动参数
disturbance_magnitude = 2.0  # 扰动幅度
disturbance_start_time = 5.0  # 扰动开始时间
disturbance_end_time = 15.0  # 扰动结束时间

# 用于存储过程值和控制输入
process_values = []
control_inputs = []
disturbances = []

# PID调节器主循环
for t in time:
    # 添加扰动
    disturbance = 0
    if disturbance_start_time <= t <= disturbance_end_time:
        disturbance = disturbance_magnitude * np.sin(2 * np.pi * t)  # 使用正弦波扰动
    disturbances.append(disturbance)

    # 计算误差
    error = setpoint - process_value
    integral += error * dt  # 更新积分项
    derivative = (error - previous_error) / dt if t > 0 else 0  # 计算微分项
    control_input = Kp * error + Ki * integral + Kd * derivative  # 计算控制输入

    # 更新过程值（考虑扰动）
    process_value += (control_input + disturbance) * dt

    # 更新上一次的误差
    previous_error = error

    # 存储数据用于绘图
    process_values.append(process_value)
    control_inputs.append(control_input)

# 绘制结果
plt.figure(figsize=(14, 8))

# 绘制过程值
plt.subplot(3, 1, 1)
plt.plot(time, process_values, label='Process Value', color='blue')
plt.axhline(y=setpoint, color='red', linestyle='--', label='Setpoint')
plt.xlabel('Time')
plt.ylabel('Process Value')
plt.title('PID Regulator Process Value with Disturbance')
plt.legend()

# 绘制控制输入
plt.subplot(3, 1, 2)
plt.plot(time, control_inputs, label='Control Input', color='green')
plt.xlabel('Time')
plt.ylabel('Control Input')
plt.title('PID Regulator Control Input')
plt.legend()

# 绘制扰动
plt.subplot(3, 1, 3)
plt.plot(time, disturbances, label='Disturbance', color='orange')
plt.xlabel('Time')
plt.ylabel('Disturbance')
plt.title('Disturbance Signal')
plt.legend()

plt.tight_layout()
plt.show()