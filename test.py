import numpy as np

class PIController:
    def __init__(self, Kp, Ki, Ts):
        self.Kp = Kp
        self.Ki = Ki
        self.Ts = Ts
        self.integral = 0

    def update(self, error):
        self.integral += error * self.Ts
        return self.Kp * error + self.Ki * self.integral

class SmithPredictor:
    def __init__(self, controller, Kp, Tp, Td, Ts):
        self.controller = controller
        self.Kp = Kp
        self.Tp = Tp
        self.Td = Td
        self.Ts = Ts

        self.process_output = 0
        self.model_output = 0

    def update(self, setpoint, measured_output):
        model_error = self.process_output - self.model_output
        control_error = setpoint - (measured_output + model_error)
        control_signal = self.controller.update(control_error)

        # Simulate the true process (with delay)
        self.process_output += self.Ts * (-self.process_output / self.Tp + self.Kp * control_signal)

        # Simulate the model (without delay)
        self.model_output += self.Ts * (-self.model_output / self.Tp + self.Kp * control_signal)

        return control_signal

# Simulation parameters
Ts = 0.1  # Sampling time
simulation_time = 100

# Process and controller parameters
Kp = 2.0
Tp = 1.0
Td = 5.0

# PI controller parameters
Kp_PI = 0.9 * Kp
Ki_PI = 1.2 * Kp / Tp

# Initialize the controller and the Smith Predictor
controller = PIController(Kp_PI, Ki_PI, Ts)
smith_predictor = SmithPredictor(controller, Kp, Tp, Td, Ts)

# Simulation loop
setpoint = 1.0
measured_output = 0
outputs = []

for t in np.arange(0, simulation_time, Ts):
    control_signal = smith_predictor.update(setpoint, measured_output)
    measured_output += Ts * (-measured_output / Tp + Kp * control_signal)

    # Introduce the time delay in the measured output
    if t >= Td:
        measured_output_with_delay = outputs[-int(Td/Ts)]
    else:
        measured_output_with_delay = 0

    outputs.append(measured_output_with_delay)

# You can now plot or analyze the outputs as needed
