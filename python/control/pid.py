#%%
import numpy as np
import matplotlib.pyplot as plt

# PID调节器参数
Kp = 1.0  # 比例增益
Ki = 0.1  # 积分增益
Kd = 0.05  # 微分增益

# 系统参数
setpoint = 10.0  # 目标值
process_value = 0.0  # 初始过程值
integral = 0.0  # 积分项初始值
previous_error = 0.0  # 上一次的误差
dt = 0.1  # 时间步长
time = np.arange(0, 20, dt)  # 时间序列

# 用于存储过程值和控制输入
process_values = []
control_inputs = []

# PID调节器主循环
for t in time:
    error = setpoint - process_value  # 计算误差
    integral += error * dt  # 更新积分项
    derivative = (error - previous_error) / dt  # 计算微分项
    control_input = Kp * error + Ki * integral + Kd * derivative  # 计算控制输入
    process_value += control_input * dt  # 更新过程值

    # 更新上一次的误差
    previous_error = error

    # 存储数据用于绘图
    process_values.append(process_value)
    control_inputs.append(control_input)

# 绘制过程值和控制输入
plt.figure(figsize=(12, 6))

# 绘制过程值
plt.subplot(2, 1, 1)
plt.plot(time, process_values, label='Process Value', color='blue')
plt.axhline(y=setpoint, color='red', linestyle='--', label='Setpoint')
plt.xlabel('Time')
plt.ylabel('Process Value')
plt.title('PID Regulator Process Value')
plt.legend()

# 绘制控制输入
plt.subplot(2, 1, 2)
plt.plot(time, control_inputs, label='Control Input', color='green')
plt.xlabel('Time')
plt.ylabel('Control Input')
plt.title('PID Regulator Control Input')
plt.legend()

plt.tight_layout()
plt.show()