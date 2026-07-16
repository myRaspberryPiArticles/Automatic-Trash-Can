from picamera2 import Picamera2
from pixel import pixels, green, red, white, off 
from ml import ask_ai_about_image, start_llama_server, stop_llama_server, save_file, actually_save_file_recycle, actually_save_file_trash
from motion import detect_motion, reset_reference
from ServoTest import trash_motion, recycle_motion, start, stop
from time import sleep
from gpiozero import Button
import os
from RPLCD.i2c import CharLCD
import subprocess

# --- 1. INITIALIZE HARDWARE ONCE ---
lcd = CharLCD('PCF8574', 0x27) 
button = Button(6, pull_up=True)
file_button = Button(16, pull_up=True, bounce_time=0.5)

# Tracks variables across events globally
override = False
folder_type = None

def handle_shutdown():
    """Triggered immediately on a single click"""
    print("Shutdown signal received via click.")
    try:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Shutting down!!!")
    except:
        pass 
    sleep(1)
    os.system("sudo shutdown -h now")

def handle_correction():
    global override, folder_type
    override = True
    
    # 1. Physically save the photo to the correct folder
    if folder_type == "recycle":
        actually_save_file_recycle(picam2)
    else:
        actually_save_file_trash(picam2)
        
    # 2. Update the LCD text notification
    save_file(folder_type)
    
    
# Assign the function to the 'when_pressed' event
button.when_pressed = handle_shutdown

# --- 2. SYSTEM INITIALIZATION ---
print("Initializing System...")
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (640, 480), "format": "RGB888"})
picam2.configure(config)
picam2.start()

start_llama_server()
start() # Initialize Servos

test = False

try:
    while True:
        if test:
            pixels.fill(white)
            sleep(2)
            
            print("Shell: AI is analyzing the frame...") 
            response = ask_ai_about_image(picam2, lcd)
            
            # Reset our override state for this new item evaluation
            override = False
            
            if "recycl" in response:
                folder_type = "trash"
                is_recycle = True
            elif "trash" in response:
                folder_type = "recycle"
                is_recycle = False
            else:
                folder_type = "unknown"
            
            if folder_type == "unknown":
                print("Shell: Confidence too low. No action taken.")
                sleep(1) 
            
            else:
                print(f"Shell: Match found [{response}]. Moving to {'RECYCLE' if is_recycle else 'TRASH'}.")
                pixels.fill(red)
                sleep(2)
                
                # Bind the button callback function BEFORE the countdown starts
                file_button.when_pressed = handle_correction
                
                # 3-Second Countdown Window
                for i in range(3, 0, -1):
                    if override:
                        break # Skip the rest of the countdown if they already pressed it
                        
                    lcd.clear()
                    lcd.cursor_pos = (0, 0)
                    lcd.write_string("If wrong hold")
                    lcd.cursor_pos = (1, 0)
                    lcd.write_string(f"button         {i}")
                    sleep(1)
                
                # --- SINGLE UNIFIED MECHANICAL MOVEMENT BLOCK ---
                if is_recycle and not override:
                    # AI guessed recycle, human did not intervene
                    pixels.fill(white)
                    sleep(0.2)
                    actually_save_file_recycle(picam2)
                    sleep(0.2)
                    recycle_motion()
                elif not is_recycle and not override:
                    # AI guessed trash, human did not intervene
                    pixels.fill(white)
                    sleep(0.2)
                    actually_save_file_trash(picam2)
                    sleep(0.2)
                    trash_motion()
                elif is_recycle and override:
                    # AI guessed recycle, but human overrode it -> Go to Trash
                    pixels.fill(white)
                    sleep(0.2)
                    actually_save_file_trash(picam2)
                    sleep(0.2)                    
                    trash_motion()
                elif not is_recycle and override:
                    # AI guessed trash, but human overrode it -> Go to Recycle
                    pixels.fill(white)
                    sleep(0.2)                    
                    actually_save_file_recycle(picam2)
                    sleep(0.2)
                    recycle_motion()
                    
                sleep(0.5)
            
            # --- CLEANUP AFTER ACTION ---
            file_button.when_pressed = None # Disarm button behavior until next cycle
            
            stop() 
            sleep(2)
            reset_reference()
            test = False
            start() 
            sleep(1)
            
        else:
            # --- MOTION PHASE ---
            pixels.fill(green)
            sleep(0.3)
            if detect_motion(picam2):
                print("Triggering AI...")
                test = True
            sleep(0.1)
        
except KeyboardInterrupt:
    print("Manual stop detected. Cleaning up...")
    picam2.stop()
    picam2.close()
    stop_llama_server()
