from pymavlink import mavutil

class connection:  ## this connection for TTL connection 
    def __init__(self):
        self.master = None
        self.connection_string = "/dev/ttyUSB0"
        self.baudrate = 115200  # Baudrate should be an integer

    def connect(self):
        # Establish MAVLink connection
        self.master = mavutil.mavlink_connection(self.connection_string, baud=self.baudrate)
        print("Waiting for heartbeat...")
        self.master.wait_heartbeat()
        print("Heartbeat received!")
        return self.master

    def loiter(self):
        self.uav = self.connect()
        if self.uav is not None:
            # Set mode to LOITER (ensure correct mode set function is used)
            self.uav.set_mode("LOITER")  # Correct function call format

# Create an instance of the connection class
uav_connect = connection()

# Connect to the UAV
uav_connect.connect()

# for loiter mode
uav_connect.loiter()
