import ai_edge_litert.interpreter as tflite
import numpy as np
import cv2
from RPLCD.i2c import CharLCD
from time import sleep
from gpiozero import Button
from signal import pause
import os
import uuid

# Fixed typo: CharLCD
lcd = CharLCD('PCF8574', 0x27)

# Global variables for the model
interpreter = None
input_details = None
labels = []

# Base directories where pictures live
save_path_recycle = "/home/siddhu/pictures/recycle"
save_path_trash = "/home/siddhu/pictures/trash"

# Safety: Ensure the physical directories exist on the Pi so it doesn't crash
os.makedirs(save_path_recycle, exist_ok=True)
os.makedirs(save_path_trash, exist_ok=True)


def save_file(folder_type):
    """Updates the LCD to let the user know the file state."""
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Image saved in")
    
    lcd.cursor_pos = (1, 0)  # Row 1, Column 0
    lcd.write_string(f"folder {folder_type}")
    sleep(3)
    lcd.clear()


def actually_save_file_recycle(picam2):
    filename = f"img_{int(uuid.uuid1())}.jpg"
    full_destination = os.path.join(save_path_recycle, filename)
    
    picam2.capture_file(full_destination)
    print(f"Shell: Saved to Recycle -> {full_destination}")


def actually_save_file_trash(picam2):
    filename = f"img_{int(uuid.uuid4())}.jpg"
    full_destination = os.path.join(save_path_trash, filename)
    
    picam2.capture_file(full_destination)
    print(f"Shell: Saved to Trash -> {full_destination}")
    
    
def start_llama_server():
    global interpreter, input_details, labels
    path = "/home/siddhu/MLModel/labels.txt"
    model_path = "/home/siddhu/MLModel/model_unquant.tflite"
    
    with open(path, 'r') as f:
        labels = [line.strip().split(' ', 1)[-1].lower() for line in f.readlines()]

    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    print("AI Server Started.")
def ask_ai_about_image(picam2, lcd): 
    # Capture frame
    frame = picam2.capture_array()
    
    # 1. Get model dimensions
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    
    # 2. Resize and Normalize
    resized_frame = cv2.resize(frame, (width, height))
    normalized_image = (resized_frame.astype(np.float32) / 127.5) - 1.0
    input_data = np.expand_dims(normalized_image, axis=0)
    
    # 3. Run Inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # 4. Process Results
    output_data = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])[0]
    index = np.argmax(output_data)
    label = labels[index]
    confidence = output_data[index]
    
    # --- UPDATED LOGIC: HIGH% Threshold ---
    if confidence >= 0.985:
        # Success: High confidence match
        print(f">>> MATCH: {label.upper()} ({confidence*100:.2f}%)")
        
        # Update LCD
        display_text = f"{label[:10]} {confidence*100:.1f}%" # Sliced label to fit LCD width
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(display_text)
        sleep(1)

        return label
    else:
        # Failure: Below 96% - Straight to trash
        print(f"--- REJECTED: {label} @ {confidence*100:.1f}% -> TRASH ---")
        
        # Update LCD
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("trash - low")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("confidence")
        
        # Returning "trash" so your main loop knows to actuate the trash mechanism
        return "trash"
    
def stop_llama_server():
    print('AI session cleared.')
