class ManualTransmission:
    def __init__(self):
        self.gear_ratios = [3.5, 2.2, 1.5, 1.0, 0.75]  # 5-speed gear ratios
        self.current_gear = 0
        self.clutch_engaged = False

    def engage_clutch(self):
        self.clutch_engaged = True

    def disengage_clutch(self):
        self.clutch_engaged = False

    def shift_gear(self, gear):
        if self.clutch_engaged and 0 <= gear < len(self.gear_ratios):
            self.current_gear = gear

    def get_current_ratio(self):
        return self.gear_ratios[self.current_gear]

class Drivetrain:
    def __init__(self):
        self.transmission = ManualTransmission()
        self.differential_ratio = 3.73  # Example differential ratio

    def get_final_drive_ratio(self):
        return self.transmission.get_current_ratio() * self.differential_ratio

class VehicleDynamics:
    def __init__(self, weight, drag_coefficient, frontal_area):
        self.weight = weight  # in kg
        self.drag_coefficient = drag_coefficient
        self.frontal_area = frontal_area  # in m^2
        self.rolling_resistance_coefficient = 0.015

    def calculate_drag_force(self, speed):
        return 0.5 * self.drag_coefficient * self.frontal_area * speed ** 2

    def calculate_rolling_resistance(self):
        return self.rolling_resistance_coefficient * self.weight * 9.81  # gravity in m/s^2

class Vehicle:
    def __init__(self, weight, drag_coefficient, frontal_area):
        self.dynamics = VehicleDynamics(weight, drag_coefficient, frontal_area)
        self.drivetrain = Drivetrain()
        self.engine_load = 0

    def update_engine_load(self, throttle_position):
        # Placeholder for engine load calculation based on throttle position
        self.engine_load = throttle_position * self.drivetrain.get_final_drive_ratio()

    def calculate_total_forces(self, speed):
        drag_force = self.dynamics.calculate_drag_force(speed)
        rolling_resistance = self.dynamics.calculate_rolling_resistance()
        total_force = drag_force + rolling_resistance
        return total_force

    def step(self, throttle_position, speed):
        self.update_engine_load(throttle_position)
        total_forces = self.calculate_total_forces(speed)
        # Additional vehicle dynamics simulation can go here
        return total_forces