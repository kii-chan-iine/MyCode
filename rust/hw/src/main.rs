struct PIController {
    kp: f64,  // 比例增益
    ki: f64,  // 积分增益
    integral: f64,  // 积分项
    prev_error: f64,  // 上一次的误差
}

impl PIController {
    fn new(kp: f64, ki: f64) -> Self {
        PIController {
            kp,
            ki,
            integral: 0.0,
            prev_error: 0.0,
        }
    }

    fn update(&mut self, error: f64, dt: f64) -> f64 {
        // 更新积分项
        self.integral += error * dt;

        // 计算控制输出
        let output = self.kp * error + self.ki * self.integral;

        // 更新上一次的误差
        self.prev_error = error;

        output
    }
}

fn main() {
    // 定义PI控制器参数
    let kp = 1.0;
    let ki = 0.1;

    // 创建PI控制器实例
    let mut pi_controller = PIController::new(kp, ki);

    // 模拟目标值和实际值
    let target = 10.0;
    let mut actual = 0.0;

    // 模拟时间步长
    let dt = 0.1;

    // 存储数据用于绘图
    let mut times = Vec::new();
    let mut errors = Vec::new();
    let mut outputs = Vec::new();
    let mut actuals = Vec::new();

    // 模拟过程
    for i in 0..100 {
        let time = i as f64 * dt;
        let error = target - actual;

        // 更新PI控制器
        let output = pi_controller.update(error, dt);

        // 更新实际值（简单的一阶系统响应）
        actual += output * dt;

        // 存储数据
        times.push(time);
        errors.push(error);
        outputs.push(output);
        actuals.push(actual);
    }

    // 将数据保存到文件中，供Python绘图使用
    use std::fs::File;
    use std::io::Write;

    let mut file = File::create("data.csv").unwrap();
    writeln!(file, "Time,Error,Output,Actual").unwrap();
    for i in 0..times.len() {
        writeln!(
            file,
            "{},{},{},{}",
            times[i], errors[i], outputs[i], actuals[i]
        )
        .unwrap();
    }

    println!("Simulation complete. Data saved to data.csv");
}