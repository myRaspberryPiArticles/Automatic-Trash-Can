import ai_edge_litert.interpreter as tflite
import numpy as np
import time
import os
from picamera2 import Picamera2
from PIL import Image

# Global variables so functions can share the model/labels
interpreter = None
input_details = None
labels = []

def start_llama_server():
    global interpreter, input_details, labels
    print("Initializing TFLite Engine...")
    
    # 1. Load Labels
    label_path = "/home/siddhu/MLModel/labels.txt"
    with open(label_path, 'r') as f:
        labels = [line.strip().split(' ', 1)[-1].lower() for line in f.readlines()]

    # 2. Load Model
    model_path = "/home/siddhu/MLModel/model_unquant.tflite"
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    
    print("TFLite Model Loaded Successfully!")
    return True # Returning true to keep your 'if' logic happy

def capture_image_pi(filename="test.jpg"):
    os.system("sudo pkill -9 libcamera")
    picam2 = Picamera2()
    # Using a standard capture resolution
    config = picam2.create_preview_configuration(main={"size": (640, 480)})
    picam2.configure(config)
    picam2.start()
    time.sleep(1.2) 
    picam2.capture_file(filename)
    picam2.stop()
    picam2.close()
    return True

def encode_image(image_path):
    """Prepares the image for the TFLite tensor."""
    # Get model requirements (usually 224x224)
    _, height, width, _ = input_details[0]['shape']
    
    # Load, resize, and convert to array
    img = Image.open(image_path).convert('RGB').resize((width, height))
    img_array = np.array(img, dtype=np.float32)
    
    # Normalization (Crucial for Teachable Machine models)
    img_array = (img_array / 127.5) - 1.0
    return np.expand_dims(img_array, axis=0)

def ask_ai_about_image(image_path):
    # 1. Prepare image
    input_data = encode_image(image_path)

    # 2. Run Inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # 3. Get results
    output_details = interpreter.get_output_details()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    
    index = np.argmax(output_data)
    result = labels[index]
    
    print(f"\n--- TFLITE Analysis: {result} ({output_data[index]*100:.1f}%) ---")
    return result

def stop_llama_server():
    print('TFLite session cleared.')

# Your existing main loop will now work perfectly with these replacements!
