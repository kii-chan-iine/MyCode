import numpy as np
import matplotlib.pyplot as plt

class PI:
    def __init__(self, kp, ki, set_point):
        """
        初始化PI控制器
        :param kp: 比例增益
        :param ki: 积分增益
        :param set_point: 设定值（目标值）
        """
        self.kp = kp
        self.ki = ki
        self.set_point = set_point
        self.integral = 0
        self.last_error = 0

    def update(self, current_value, dt):
        """
        根据当前值更新PI控制器
        :param current_value: 当前值
        :param dt: 时间步长
        :return: 控制器输出
        """
        error = self.set_point - current_value  # 计算误差
        self.integral += error * dt  # 积分项
        output = self.kp * error + self.ki * self.integral  # 计算输出
        self.last_error = error  # 更新误差
        return output

# 模拟温度控制系统
def simulate_temperature_control(kp, ki, set_point, initial_temp, time_steps, dt):
    pid = PI(kp, ki, set_point)
    temperatures = [initial_temp]
    control_signals = []

    for _ in range(time_steps):
        current_temp = temperatures[-1]
        control_signal = pid.update(current_temp, dt)
        control_signals.append(control_signal)
        
        # 假设系统动态：温度变化与控制信号成正比
        temp_change = control_signal * dt
        new_temp = current_temp + temp_change
        temperatures.append(new_temp)

    return temperatures, control_signals

# 参数设置
kp = 0.1
ki = 0.01
set_point = 100  # 目标温度
initial_temp = 0  # 初始温度
time_steps = 100  # 模拟时间步数
dt = 0.1  # 时间步长

# 运行仿真
temperatures, control_signals = simulate_temperature_control(kp, ki, set_point, initial_temp, time_steps, dt)

# 绘制结果
time = np.arange(0, time_steps * dt, dt)
plt.figure(figsize=(10, 6))
plt.plot(time, temperatures, label="Temperature (°C)")
plt.axhline(y=set_point, color='r', linestyle='--', label="Set Point")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("PI Regulator Simulation")
plt.legend()
plt.grid(True)
plt.show()
