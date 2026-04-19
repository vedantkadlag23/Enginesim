import tkinter as tk
from tkinter import ttk
import random

class EngineSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title('Interactive Engine Simulator')

        # Set up the dashboard
        self.create_dashboard()

        # Initialize values
        self.rpm = 0
        self.torque = 0
        self.temperature = 70  # in celsius
        self.power = 0

        # Keyboard controls
        self.root.bind('<KeyPress>', self.key_press)

        # Start the simulator
        self.update_values()

    def create_dashboard(self):
        # Dashboard frame
        self.dashboard = ttk.Frame(self.root)
        self.dashboard.pack(padx=10, pady=10)

        # RPM Gauge
        self.rpm_label = ttk.Label(self.dashboard, text='RPM: 0')
        self.rpm_label.grid(row=0, column=0, padx=10)

        # Torque Gauge
        self.torque_label = ttk.Label(self.dashboard, text='Torque: 0 Nm')
        self.torque_label.grid(row=1, column=0, padx=10)

        # Temperature Gauge
        self.temp_label = ttk.Label(self.dashboard, text='Temperature: 70 °C')
        self.temp_label.grid(row=2, column=0, padx=10)

        # Power Gauge
        self.power_label = ttk.Label(self.dashboard, text='Power: 0 HP')
        self.power_label.grid(row=3, column=0, padx=10)

    def update_values(self):
        # Simulate engine data update
        self.rpm = random.randint(1000, 6000)
        self.torque = random.randint(100, 500)
        self.temperature = random.randint(70, 100)
        self.power = (self.rpm * self.torque) / 5252  # HP calculation

        # Update the dashboard labels
        self.rpm_label.config(text=f'RPM: {self.rpm}')
        self.torque_label.config(text=f'Torque: {self.torque} Nm')
        self.temp_label.config(text=f'Temperature: {self.temperature} °C')
        self.power_label.config(text=f'Power: {self.power:.2f} HP')

        # Repeat every 1000 ms
        self.root.after(1000, self.update_values)

    def key_press(self, event):
        # Simple control mapping
        if event.char == 'w':
            print('Throttle Increased')  # Throttle control
        elif event.char == 's':
            print('Throttle Decreased')
        elif event.char == 'a':
            print('Gear Down')
        elif event.char == 'd':
            print('Gear Up')
        elif event.char == 'x':
            print('Clutch Pressed')
        elif event.char == 'b':
            print('Brakes Applied')

if __name__ == '__main__':
    root = tk.Tk()
    app = EngineSimulator(root)
    root.mainloop()