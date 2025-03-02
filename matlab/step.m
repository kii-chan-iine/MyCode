% 定义系统的传递函数
numerator = [1]; % 分子多项式系数
denominator = [1, 2, 1]; % 分母多项式系数
sys = tf(numerator, denominator); % 创建传递函数模型

% 绘制阶跃响应
figure; % 创建一个新图形窗口
step(sys); % 绘制阶跃响应
title('阶跃响应'); % 添加标题
grid on; % 添加网格
