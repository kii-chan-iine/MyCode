#%%
import numpy as np
import matplotlib.pyplot as plt

# PID调节器参数
Kp = 2.0  # 比例增益
Ki = 0.5  # 积分增益
Kd = 0.1  # 微分增益

# 系统参数
setpoint = 1.0  # 目标值（阶跃信号的幅值）
process_value = 0.0  # 初始过程值
integral = 0.0  # 积分项初始值
previous_error = 0.0  # 上一次的误差
dt = 0.05  # 时间步长
simulation_time = 20  # 模拟总时间
time = np.arange(0, simulation_time, dt)  # 时间序列

# 时延参数
time_delay = 1.0  # 时延时间（秒）
delay_steps = int(time_delay / dt)  # 时延对应的步数

# 初始化时延缓冲区
delay_buffer = [0.0] * delay_steps  # 缓冲区长度根据时延和时间步长计算

# 用于存储过程值和控制输入
process_values = []
control_inputs = []

# PID调节器主循环
for t in time:
    # 计算误差
    error = setpoint - process_value
    integral += error * dt  # 更新积分项
    derivative = (error - previous_error) / dt if t > 0 else 0  # 计算微分项
    control_input = Kp * error + Ki * integral + Kd * derivative  # 计算控制输入

    # 更新时延缓冲区
    delay_buffer.append(control_input)  # 将当前控制输入加入缓冲区
    delayed_control_input = delay_buffer.pop(0)  # 获取最早加入的控制输入（延迟后的）

    # 更新过程值（考虑时延后的控制输入）
    process_value += delayed_control_input * dt

    # 更新上一次的误差
    previous_error = error

    # 存储数据用于绘图
    process_values.append(process_value)
    control_inputs.append(control_input)

# 绘制结果
plt.figure(figsize=(12, 6))

# 绘制过程值
plt.subplot(2, 1, 1)
plt.plot(time, process_values, label='Process Value', color='blue')
plt.axhline(y=setpoint, color='red', linestyle='--', label='Setpoint')
plt.axvline(x=time_delay, color='orange', linestyle='--', label='Time Delay')
plt.xlabel('Time (s)')
plt.ylabel('Process Value')
plt.title('PID Regulator Process Value with Time Delay')
plt.legend()

# 绘制控制输入
plt.subplot(2, 1, 2)
plt.plot(time, control_inputs, label='Control Input', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Control Input')
plt.title('PID Regulator Control Input')
plt.legend()

plt.tight_layout()
plt.show()