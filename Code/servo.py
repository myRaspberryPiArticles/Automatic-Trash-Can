import pigpio
import time
import sys

# Initialize global pi object
pi = pigpio.pi()

# 1. Check connection at the very start
if not pi.connected:
    print("Could not connect to pigpiod! Run 'sudo pigpiod' in terminal.")
    sys.exit()

SERVO_ONE = 17
SERVO_TWO = 22

def trash_motion():
    # Ensure pi is connected before trying to use it
    if not pi or not pi.connected:
        print("Error: Servo connection is closed. Call start() first.")
        return
    
    print("Executing trash motion...")
    pi.set_servo_pulsewidth(SERVO_ONE, 1000)
    pi.set_servo_pulsewidth(SERVO_TWO, 2000)
    time.sleep(2)
    pi.set_servo_pulsewidth(SERVO_ONE, 1500)
    pi.set_servo_pulsewidth(SERVO_TWO, 1500)
    
def recycle_motion():
    # Ensure pi is connected before trying to use it
    if not pi or not pi.connected:
        print("Error: Servo connection is closed. Call start() first.")
        return
    
    print("Executing recycle motion...")
    pi.set_servo_pulsewidth(SERVO_ONE, 2000)
    pi.set_servo_pulsewidth(SERVO_TWO, 1000)
    time.sleep(2)
    pi.set_servo_pulsewidth(SERVO_ONE, 1500)
    pi.set_servo_pulsewidth(SERVO_TWO, 1500)

def stop():
    global pi
    print("Stopping servos and closing connection...")
    pi.set_servo_pulsewidth(SERVO_ONE, 0)
    pi.set_servo_pulsewidth(SERVO_TWO, 0)
    pi.stop() # This kills the connection object

def start():
    global pi # This tells Python to update the 'pi' outside this function
    print("Restarting connection...")
    pi = pigpio.pi()
    if not pi.connected:
        print("Failed to restart pigpiod.")

if __name__ == "__main__":
    try:
        trash_motion()
        
        # Example of how to stop and restart properly: 
        time.sleep(1)
        stop()
        time.sleep(1)
        start()
        recycle_motion()
        time.sleep(1)
        stop()
       # start() # Now this will actually refresh the global 'pi'
       # trash_motion()
        
    except KeyboardInterrupt:
        stop()
