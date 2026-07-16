import numpy as np
import cv2

ref_gray = None

def detect_motion(picam2):
    global ref_gray
    
    # Capture current frame
    current_frame = picam2.capture_array()
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_RGB2GRAY)
    current_gray = cv2.GaussianBlur(current_gray, (21, 21), 0)
    
    # Initialize reference frame if empty
    if ref_gray is None:
        ref_gray = current_gray
        return False

    # Compare frames
    frame_delta = cv2.absdiff(ref_gray, current_gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    change_amount = np.sum(thresh) / 255
    
    # Update reference (prevents getting stuck on static changes)
    if change_amount < 5000: # Only update if not massive motion
        cv2.addWeighted(current_gray, 0.1, ref_gray, 0.9, 0, ref_gray)

    if change_amount > 20000:
        print(f"MOTION DETECTED! Score: {int(change_amount)}")
        return True
    
    return False

def reset_reference():
    global ref_gray
    ref_gray = None
    print("Motion baseline reset.")
