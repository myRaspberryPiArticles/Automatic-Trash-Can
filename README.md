# Automatic-Trash-Can
This is a repo for my RPI powered trash bin that sorts waste into trash and recyclable. Includes code pictures and a flow chart of how the code works. I will also put a list of parts you want to recreate it!

## Pictures of the project

<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 24 (2)" src="https://github.com/user-attachments/assets/c12250c2-a737-4fe2-8dd2-f8694362e664" />
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 24 (1)" src="https://github.com/user-attachments/assets/ea84ed18-ed79-4549-be2c-5c72f600e9e9" />
<br>
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 23 (3)" src="https://github.com/user-attachments/assets/050a2b43-8bd4-47a6-ac51-df6479f5b6e0" />
<img width="167" height="76" alt="WhatsApp Image 2026-07-16 at 19 56 21" src="https://github.com/user-attachments/assets/d8cdc08c-efc5-4632-b5cf-f0bc010bb24e" />
<br>
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 20 (1)" src="https://github.com/user-attachments/assets/cd391588-5b07-4eff-926f-93d17f334f90" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 23" src="https://github.com/user-attachments/assets/3a27b525-3780-483a-9e2c-b46a568d9543" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 23 (2)" src="https://github.com/user-attachments/assets/17bce2bb-e4fe-40bb-b398-504d4dbfb448" />
<img width="76" height="167" alt="WhatsApp Image 2026-07-16 at 19 56 22 (1)" src="https://github.com/user-attachments/assets/80627669-e05b-4296-a6c8-90f28469a911" />

## How it works


<img width="470" align="right" alt="Screenshot" src="https://github.com/user-attachments/assets/c1bc298a-543f-4ba3-a413-d672ba14d3a6" style="margin-left: 20px; margin-bottom: 10px; border: none !important; box-shadow: none !important;">

This flow chart shows all the processes that the code goes through to classify the data. The first stage is to detect motion, and once that starts it goes into the main loop that calssifies the waste. 

The main loop consist of 4 turning points, where there is a choice, and two of them come from the manual override feature which inverses the final decision of the ML Model. One of the other ones is the threshold which you can set as a percentage to change how strict you would like the ML Model to finalise the answer. 

After finally deciding, two servos tilt a cardboard base to dump the waste into the trash side or recycle side, and in my case the bin is just a shelf split by cardboard. Then, it can go back into the idling mode where it awaits motion.

Another important thing to mention is that the trash bin itself does not need a WiFi or Bluetooth connection to work! It can run anywhere as long as there is a stable power source to power everything!

## ML Model

The ML Model is attached in the files as pictures and also the ZIP folder for you to put it on a Pi. The ML Model gives the percentage of what class it is to make sure it is accurate. It uses real life photos inside the trash bin to improve accuracy of the model. 

I used [Teachable Machines](https://teachablemachine.withgoogle.com/train/image) to train the model, with photos from a premade dataset on [Kaggle](https://www.kaggle.com) as well as real examples of what the camera can see.

After every run of the trash bin, it also aves an image to the respective folder based on what the waste is, trash or recycle. These can them be put back into the model to collect even more real life scenarios of trash.

## Camera

I use a generic RPI Camera which does the job in both capturing photos and also detecting motion. 

## Neopixel

There is a 16 LED Neopixel ring that acts as a status light and flash light when taking the photo. Red is in progress state, when it runs through the ML Model and manual input. Green is free and idling state where it awaits motion. It quickly flashes white to take the photo for sending it to the ML Model and storing it.

## Buttons and their functions

There are two buttons, one for shutting down the Pi (the red one), and one that is the manual override if the ML Model is wrong (the green one). It is important to shutdown the Pi, and as it is not a Pi 5 with shutdown button, I put one myself to ensure safe power offs. The manual override button inverses the output and instead of saving the image to the folder the ML Model originally would, it saves it to the other one.

## Hardware

The outside frame is some wood bought form a local hardware store, and then cut and glued to for a wooden cuboid. Then, I cut paper to the right size to cover up the space, and glue it to the edge to keep it clean and tight. The Pi is mounted with the screw holes it has, and the rest of the components are hot glued on.

## Bill of Materials (Electric components)
| Part | Where to buy |
| :--- | :---: |
| Raspberry Pi 4 Model B | [PiHut](https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052674622) |
| SD Card | Anywhere |
| Pi Camera | [Amazon](https://www.amazon.co.uk/AZDelivery-⭐⭐⭐⭐⭐-Camera-Raspberry-Ebook/dp/B076FB1KCW/ref=sr_1_10?crid=3ATAF7NSL5FXN&dib=eyJ2IjoiMSJ9.bZhTDnrkgJSY2J8TROWarFFSp1GwyXcIU5DzCH4kws4nwXbN7_bUY-Fj0kCoYBaKkD0Z4lOO0x9DwXfIDerI2bUaXpSGyfq8VH1sSpmW3FqYXEBSPJENJyP6wMOZULvZ8Cf0ysGaQSU84kb8oHvSVn52QblJuj0daCmaWWzraLVxyJrN0b0TtNMykN_aNXd-HTPDbJeBv__MB9kmSkGordYE4rhubbqC-L8zslmi2n4.EcHSrhFO6fDHMrJyE3ZnrodMEY5ZD8vHrjphffWe0K8&dib_tag=se&keywords=pi%2Bcamera&qid=1784231364&sprefix=pi%2Bcamer%2Caps%2C117&sr=8-10&th=1) |
| Neopixel | [PiHut](https://thepihut.com/products/adafruit-neopixel-ring-16-x-5050-rgb-led-with-integrated-drivers) |
| LCD | [PiHut](https://thepihut.com/products/waveshare-blue-16x2-i2c-lcd-module-3-3v-5v-with-backlight-control) |
| Buttons | [PiHut](https://thepihut.com/products/colorful-round-tactile-button-switch-assortment-15-pack) |
| Servo (x2) | [PiHut](https://thepihut.com/products/towerpro-servo-motor-sg90-digital) |
| Wires and jumper cables | Anywhere |
