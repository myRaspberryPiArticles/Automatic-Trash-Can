# Automatic-Trash-Can
This is a repo for my RPI powered trash bin that sorts waste into trash and recyclable. Includes code pictures and a flow chart of how the code works. I will also put a list of parts and schematic if you want to recreate it!

Pictures of the project:

//


How it works:

<img width="609" height="506" alt="Screenshot 2026-07-16 at 14 30 47" src="https://github.com/user-attachments/assets/bb055d9f-6162-42f6-b44d-84dc6c2b95c9" />

This flow chart shows all the processes that the code goes through to classify the data. The Neopixel ring changes according to the status and when motion is detected, allowing the user to see the stages it is running through. Additionally, there is a 16x2 LCD to display small messages like 'Motion Detected!'. The ML Model is attached in the files as pictures and also the zip folder for you to put it on a Pi. The ML Model gives the percentage of what class it is to make sure it is accurate.
