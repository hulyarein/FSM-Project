import tkinter as tk

class TrafficLightFSM:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light FSM Demo")

        self.canvas = tk.Canvas(root, width=350, height=400, bg="black")
        self.canvas.pack()

       
        self.ns_light = self.create_light(50, "North-South (NS)")
        self.ew_light = self.create_light(200, "East-West (EW)")

        # Initialize state and input
        self.state = "S0"  # Start at state S0 (NS Green, EW Red)
        self.input_traffic = "00"  # Default input (no traffic for both)

        # Dictionary to define state transitions based on the input

        #states
        # S0: NS Green, EW Red (default start state).
        # S1: NS Yellow, EW Red.
        # S2: NS Red, EW Green.
        # S3: NS Red, EW Yellow.
        
        #inputs
        # 00: No traffic detected in both directions.
        # 01: Traffic detected in the NS direction.
        # 10: Traffic detected in the EW direction.
        # 11: Traffic detected in both directions.

        self.transitions = {
            "S0": {"00": "S0", "01": "S0", "10": "S1", "11": "S1"},
            "S1": {"00": "S2", "01": "S2", "10": "S2", "11": "S2"},
            "S2": {"00": "S2", "01": "S3", "10": "S2", "11": "S3"},
            "S3": {"00": "S0", "01": "S0", "10": "S0", "11": "S0"}
        }

       
        self.update_lights()

    def create_light(self, x, label):
        
        self.canvas.create_text(x + 50, 30, text=label, fill="white", font=("Arial", 14))
        red = self.canvas.create_oval(x, 50, x + 100, 150, fill="gray")
        yellow = self.canvas.create_oval(x, 150, x + 100, 250, fill="gray")
        green = self.canvas.create_oval(x, 250, x + 100, 350, fill="gray")
        return {"red": red, "yellow": yellow, "green": green}

    def update_lights(self):
        
        if self.state == "S0":  # NS Green, EW Red
            self.set_light(self.ns_light, "green")
            self.set_light(self.ew_light, "red")
            next_state_delay = 5000  # 5 seconds

        elif self.state == "S1":  # NS Yellow, EW Red
            self.set_light(self.ns_light, "yellow")
            self.set_light(self.ew_light, "red")
            next_state_delay = 1000  # 1 second

        elif self.state == "S2":  # NS Red, EW Green
            self.set_light(self.ns_light, "red")
            self.set_light(self.ew_light, "green")
            next_state_delay = 5000  # 5 seconds

        elif self.state == "S3":  # NS Red, EW Yellow
            self.set_light(self.ns_light, "red")
            self.set_light(self.ew_light, "yellow")
            next_state_delay = 1000  # 1 second

        
        self.root.after(next_state_delay, self.transition)

    def set_light(self, light, active_color):
        
        for color, item in light.items():
            fill_color = active_color if color == active_color else "gray"
            self.canvas.itemconfig(item, fill=fill_color)

    def transition(self):
        self.state = self.transitions[self.state][self.input_traffic]
        self.update_lights()

    def set_input(self, traffic_input):
        self.input_traffic = traffic_input

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightFSM(root)

    root.after(10000, lambda: app.set_input("10"))  # Simulate EW traffic #S2 (NS Red, EW Green) 
    root.after(20000, lambda: app.set_input("01"))  # Simulate NS traffic #S3 (NS Red, EW Yellow.)
    root.after(30000, lambda: app.set_input("11"))  # Simulate both directions traffic #S0 (NS Green, EW Red)

    root.mainloop()
