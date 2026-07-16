# Automatic-Trash-Can
This is a repo for my RPI powered trash bin that sorts waste into trash and recyclable. Includes code pictures and a flow chart of how the code works. I will also put a list of parts you want to recreate it!

## Pictures of the project

<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 24 (2)" src="https://github.com/user-attachments/assets/c12250c2-a737-4fe2-8dd2-f8694362e664" />
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 24 (1)" src="https://github.com/user-attachments/assets/ea84ed18-ed79-4549-be2c-5c72f600e9e9" />
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 23 (3)" src="https://github.com/user-attachments/assets/050a2b43-8bd4-47a6-ac51-df6479f5b6e0" />
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 21" src="https://github.com/user-attachments/assets/d8cdc08c-efc5-4632-b5cf-f0bc010bb24e" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 20 (1)" src="https://github.com/user-attachments/assets/cd391588-5b07-4eff-926f-93d17f334f90" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 23" src="https://github.com/user-attachments/assets/3a27b525-3780-483a-9e2c-b46a568d9543" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 23 (2)" src="https://github.com/user-attachments/assets/17bce2bb-e4fe-40bb-b398-504d4dbfb448" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 22 (1)" src="https://github.com/user-attachments/assets/80627669-e05b-4296-a6c8-90f28469a911" />

## How it works

<img width="389" height="314" alt="Screenshot 2026-07-16 at 14 40 36" src="https://github.com/user-attachments/assets/c1bc298a-543f-4ba3-a413-d672ba14d3a6" />

This flow chart shows all the processes that the code goes through to classify the data. The Neopixel ring changes according to the status and when motion is detected, allowing the user to see the stages it is running through. Additionally, there is a 16x2 LCD to display small messages like 'Motion Detected!'. 

## ML Model

The ML Model is attached in the files as pictures and also the zip folder for you to put it on a Pi. The ML Model gives the percentage of what class it is to make sure it is accurate. It uses real life photos inside the trash bin to improve accuracy of the model. 

## Neopixel

There is a 16 LED Neopixel ring that acts as a status light and flash light when taking the photo. Red is in progress state, when it runs through the ML Model and manual input. Green is free and idling state where it awaits motion.

## Buttons and their functions

There are two buttons, one for shutting down the Pi (the red one), and one that is the manual override if the ML Model is wrong (the green one). It is important to shutdown the Pi, and as it is not a Pi 5 with shutdown button, I put one myself to ensure safe power offs. The manual override button inverses the output and instead of saving the image to the folder the ML Model originally would, it saves it to the other one.

## Hardware

The outside frame is some wood bought form a local hardware store, and then cut and glued to for a wooden cuboid. Then, I cut paper to the right size to cover up the space, and glue it to the edge to keep it clean and tight. The Pi is mounted with the screw holes it has, and the rest of the components are hot glued on.

## Bill of Materials
