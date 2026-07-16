# Automatic-Trash-Can
This is a repo for my RPI powered trash bin that sorts waste into trash and recyclable. Includes code pictures and a flow chart of how the code works. I will also put a list of parts and schematic if you want to recreate it!

## Pictures of the project:

//


## How it works:

<img width="389" height="314" alt="Screenshot 2026-07-16 at 14 40 36" src="https://github.com/user-attachments/assets/c1bc298a-543f-4ba3-a413-d672ba14d3a6" />

This flow chart shows all the processes that the code goes through to classify the data. The Neopixel ring changes according to the status and when motion is detected, allowing the user to see the stages it is running through. Additionally, there is a 16x2 LCD to display small messages like 'Motion Detected!'. 

## ML Model

The ML Model is attached in the files as pictures and also the zip folder for you to put it on a Pi. The ML Model gives the percentage of what class it is to make sure it is accurate. It uses real life photos inside the trash bin to improve accuracy of the model. 

## Neopixel

There is a 16 LED Neopixel ring that acts as a status light and flash light when taking the photo. Red is in progress state, when it runs through the ML Model and manual input. Green is free and idling state where it awaits motion.
