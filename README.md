# Welcome to our GitHub!

# Introduction
We are team 6Nuts3Bolts, a dynamic trio of passionate robotics enthusiasts. 
Based off of the nature of the task, we divded the industry and each took on a key aspect of the challenge.

**Arham**: 

**Shauryaveer**:

**Ranveer**:
# Table of Contents
Our Engineering Process

Car photos








    





  
  

**Obstacle management**

# Our Engineering Process
We have used scoring criteria from the ruleblock as headings in our documentation to make it easy to navigate our repository.

It is vital to understand a problem and its features in depth before planning and undertaking its solution. Hence, we first spent a day analysing the challenge in depth and noting down a few principles, parameters, fundamental ideas off of which we could organize our thinking and streamline our ideation process to efficiently solve the challenge. 
Here are the principles we decided on:

**Design and Construction**
- Compact, able to maneuver past obstacles even at high speeds
- Simple and practical, a design appropriate for the challenge, not overly complex
- Modular, quick and easy to assemble and disassemble

**Electrical Systems**
- Clean and orgranised, connections easy to keep track of
- Reliable and safe, eliminate any chances of a short or circuit failure
- Easy to assemble and dissassemble

**Logic and Programming**
- f
- f
- f

Based off these fundamental ideas, we aimed to conceptualize our robot.
Next, we immediately begain the prototyping and iteration process.

Here's how we went about achieving our target

## **Mobility management**
### Hardware Components list:
- Rev Duo 60mm Traction Wheels https://www.revrobotics.com/DUO-Traction-Wheels/
- Chassis
  - Top plate
  - Bottom Plate
- Steering Mechanism
  - Linkage
  - Left Front
  - Right Front
- Bevel Gears
- Motor Bracket
- Electronics Mount
- 
- M3 Screws
- Lock nuts

**How we made it Compact**

We began by visualizing how all the components could fit closely together, and we built around that idea. The space between parts is minimal, but we made sure it wouldn’t create any issues in performance or accessibility.
The overall length of the robot is limited by key components like the NEO 550 motor, bevel gears, and the steering system, while the width is determined by the size of the Spark MAX, ultrasonic sensor, servo, and battery. By carefully balancing the length and width, we were able to create a robot that is compact yet fully functional. The width isn't constrained by any specific part, it’s simply as wide as necessary to accommodate the essential components.

**How we ensured simplicity and practicality**

From the beginning, we adopted a mindset of keeping things simple. We've learned that complexity can quickly lead to chaos, especially when time is tight or you're troubleshooting under pressure. By focusing on simplicity, we narrowed our options and only considered ideas that were practical and easy to implement. If a solution met our goals without adding unnecessary complications, we ran with it. Simplicity also naturally led to practicality because fewer moving parts meant fewer things to go wrong, and every design choice was intentional and straightforward.

**How we made it Modular**

The entire robot is based around three main plates, with each subassembly between them individually 3D printed. This modular design gives us a lot of flexibility. If something goes wrong with a specific part, we don’t need to overhaul the entire system—just swap out the problem area. It makes troubleshooting and maintenance much quicker and less stressful.
We designed the robot to be broken down into three key systems: the drive system, the steering system, and the electronics assembly. Any part that doesn’t fall into one of these categories is mostly there to provide structural integrity and support to the main components. For instance, the bottom plate doesn’t serve any critical function other than strengthening the overall structure. This modular approach ensures that our robot remains easy to work on, upgrade, and maintain, which is key for long-term reliability.

## **Power and sense management**

### Electrical Components list:
- **RaspberryPi 4B**
  https://robu.in/product/raspberry-pi-4-model-b-with-4-gb-ram/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG0_X9z0IWl0GMOeDR9xo95aErRhqwMOBMpljfzc0rZcln-PEJ_WPNhoCWP4QAvD_BwE
  
- **Raspberry Pi Camera Module 3 with Wide Angle Lens**
   https://robu.in/product/raspberry-pi-camera-module-3-wide/
  
- **Arduino Nano**
  https://robu.in/product/arduino-nano-board-r3-with-ch340-chip-wo-usb-cable-solderedarduino-nano-r3-wo-usb-cable-soldered/?        
  gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG2RzmpzoTJQA5ThT4OKJQDOLGdDu_CcdCzMTJhiYnkzNB_LoFYl8ChoCa28QAvD_BwE
  
- **BNO055 IMU**
  https://evelta.com/7semi-bno055-9-dof-absolute-orientation-sensor-breakout-i2c-qwiic/?utm_campaign=PMax_7Semi_Brand&utm_source=google&utm_medium=cpc&utm_matchtype=&utm_term=&adgroupid=&gc_id=21448253640&h_ad_id=&gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG9t5I-iOiD0RwKp8cLeIIelVS6iZASKIyd3kG00_usR5Ykl3bWthoxoCxlUQAvD_BwE
  
- **MG996R Servo**
  https://robu.in/product/towerpro-mg996r-digital-high-torque-servo-motor/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG5k2qGe0ascHdXMnf665lYrTuYaYGQ-buKZOUEIb1roxZUKqwj_jnBoCRrkQAvD_BwE
  
- **RevRobotics NEO550**
  https://www.revrobotics.com/rev-21-1651/
  
- **RevRobotics SparkMax Motor Controller**
  https://www.revrobotics.com/rev-11-2158/
  
- **HC-SR04 Ultrasonic Sensors**
  https://robu.in/product/hc-sr04-ultrasonic-range-finder/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG_EbtKfqxJVVLmNFvlb45ERmHGkg5ZeKwsyH0o36EEyIciF_qd2AgxoCbHIQAvD_BwE
  
- **Xcluma USB Buck Converter**
  https://www.xcluma.com/0.9v-5v-to-5v-600ma-usb-output-charger-step-up-power-module-mini-dc-dc-boost-converter?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrGwnZnr6HztAhUfIc8EmXiPdcBPvQhlMLFXXWHMaUp1jXnO9AhzcHORoCvscQAvD_BwE
  
- **2200MAh 40C 12V LiPo Battery**
  https://robokits.co.in/batteries-chargers/drone-batteries/genx-power-premium-lipo-battery/genxpower-11.1v-lipo-batteries/genx-11.1v-3s-2200mah-40c-80c-premium-lipo-lithium-polymer-battery?srsltid=AfmBOooZmP-jRWhm7kENYL9RMQMeitv-NZOYCRSYtrRlzXW_ab-SBCOg
  
- **Switch**
  https://robu.in/product/kcd5-101-mini-rocker-switch-2pinon-off/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG3xTcQJe-xwuf-VgMbq_GhRlw2xvdMJ_hcsEn1JaMIH2xizj02XIUBoC27gQAvD_BwE
  
- **Pushbutton**
https://robu.in/product/mc002076-terminal-block-barrier-3pos/
  
- **General Purpose Board**
  https://robu.in/product/8-x-12-cm-universal-pcb-prototype-board-single-sided-2-54mm-hole-pitch/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG-9HyNzYSmtE-KpMW2ga34XkH7SE7PdmuRkKmwuoX7r9kTfUCxHYYBoCkWEQAvD_BwE
  
- **JST Connectors**
  https://robu.in/product/4-pin-jst-xh-2-54mm-pitch-plug-and-socket-with-cable-5-pcs/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG3ThNvwgApN0K5ayPAHMNajE53OX_YYqjVMQp1rAzSzAncURmy8bChoC4KEQAvD_BwE
  
- **Jumper Wires**
  https://www.amazon.in/Electrobot-Jumper-Wires-120-Pieces/dp/B071VQLQQQ?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1P9ZW4IHIOLEJ
  
- **Solid Core Wires**
  https://robocraze.com/products/single-stranded-hook-up-wires-1m-each-5-colorsvariant=40193905590425&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=google&utm_medium=cpc&utm_campaign=BL+%7C+Pmax+%7C+Feed+Only+%7C+RoboCraze+%7C+Electronic+Components+%7C+31%2F05&utm_source=googleads&utm_medium=ppc&utm_campaign=21337209786&utm_content=_&utm_term=&campaignid=21337209786&adgroupid=&campaign=21337209786&gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrG3u9fNBU5QDhYD9Ucx_2wW2NyCeETx7FvXPxnjWEPRTooklT7cg9MhoCnbUQAvD_BwE
  
- **XT60 Connectors**
  https://robu.in/product/amass-xt60-male-connector-xt60-m-g-y/?gad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrGzPYPHGdOfB5ZcnJi-e7oqUFiNBjxtAciUPGctwt8o8nlXeyrNpHuBoCN7wQAvD_BwE
  
- **Crimp Connectors**
  https://www.tsktech.in/product/6-3mm-female-spade-connector-with-insulator-boot-crimp-terminal-thimbles-no-color-choice-pack-of-10nos/
  
### **Reason for choice of Electrical Components**

**RaspberryPi 4B**

      - With its quad-core ARM Cortex-A72 64-bit 1.5GHz processor and 8GB RAM it meant that we would never face a computationl bottleneck, even with the heavy task of image processing in the obstacle         challenge.
      - Its ability to be programmed and controlled wirelessly was a boon during the testing and debugging phase as we could run the robot almost continuously without having to detach and reattach            the cable for uploading code.
      - Its extensive use and testing was the reason we chose to go with the RaspberryPi 4B instead of the newer RaspberryPi 5. If there was ever an issue we faced, it could most likely be solved by          searching up the problem.

**RaspberryPi Camera Module 3 with Wide Angle lens**

      - We chose this mainly for its ease of integration and compatability with the RaspberryPi. 
      - Its wide FOV (120 degrees), high resolution(12 megapixels), autofocus feature and ability to sense color in a wide range of lighting conditions allowed for efficent obstacle detection and             sensing from varying distances and angles even while moving at high speeds

**Arduino Nano**

      - The use of the Arduino Nano in our robot is solely to gather data from the ultrasonic sensors and relay it to the RaspberryPi. 
      - Hence its compactness and low power consumption was the main reason we chose to use it.

**BNO055 IMU**

      - The BNO055 is a highly tested and reliable sensor. We had used it earlier in FTC(First Tech Challenge) as well as in a drone we made. We had also used it in Future Engineers the previous year.
      - It has an inbuilt sensor fusion algorithm and it is easy to integrate with the RaspberryPi, communicating over I2C.

**MG996R Servo**

      - It is a popular and reliable servo which for us is delivering about 9.5kgcm(since we are powering it through the RaspberryPi 5V pin)
      - It is easily able to steer our robot even at high speeds.
      - The position accuracy it is able to provide is relaible and it is able to steer at a rate of about 0.30 sec/60° degrees according to our measurements.

**RevRobotics NEO550**

      - It has an absolutely phenomenal power to weight ratio (weighing only 140grams) as well as very high acceleration and has a free running speed of upto 11000 RPM. We have geared it in a 5:1             ratio. 
      - We had previously used this motor in FRC (FIRST Robotics Competition) and hence were comfortable operating with it.
      - It has excellent speed control and is easy to integrate and program with the SparkMax motor controller.

**RevRobotics SparkMax Motor Controller**

      - Using the NEO550 meant we would have to use this since they are complimentary pieces of hardware.
      - Its inbuilt current limiting feature also allows for the motor to remain safe from sudden power surges.

**HC-SRO4 Ultrasonic Sensors**

      - These are widely available and a popular choice of sensor although sometimes they may be unreliable, with good programming they can be made to work just fine. 
      - There are many resources and libraries available online to control these effectively making both programming and troubleshooting easy to do.
      - Their accuracy is reasonable, able to provide output within a 2-3mm range of error and are also able to maintain consistency at moderate speeds, providing data every 30ms.
      - Apart from that, its also easy to integrate

**Xcluma USB Buck Converter**

      - It was able to provide a more stable output of 5V than the buck converter we were previously using. It also made it such that we could easily power the RaspberryPi through its USBC port.
      - It was also more compact than the previous buck.
      - Its built in safety feature of preventing against overvoltage and overcurrent proved to be useful especially during testing.

**2200MAh 40C 12V LiPo Battery**

      - We needed a high power battery since the electronic components we used(RaspberryPi while image processing, NEO550) were quite power hungry.
      - It was also capable of providing our robot with a long runtime. We can run our robot for 12 minutes continuously.

      
### **How we achieved Clean and Organized wiring**

To keep our wiring system easy to manage, we focused on clarity, organization and structure in all connections.

We used solid core wire for connections since they can be bent into shape making wiring neat and easy to solder.
We soldered all wire connections and mounted them on a general purpose board providing a solid foundation for the wiring, minimizing loose wires and clutter.
Every wire was labeled and color-coded, making it simple to track individual connections. This helped ensure quick identification of components during assembly and troubleshooting.
  
      Red - VCC wires
      Black - GND wires
      Purple - PWM Signal (Pin 33 or GPIO 13 on RaspberryPi)
      Yellow(Ultrasonic) - TRIG (Pins D3 and D7 on Nano)
      Blue(Ultrasonic) - ECHO (Pins D4 and D6 on Nano)
      Yellow(BNO055) - SDA (Pin 3 or GPIO 2 on RaspberryPi 
      Blue(BNO055) - SCL (Pin 5 or GPIO 3 on RaspberryPi)
      Blue(Button) - SIGNAL (Pin 11 or GPIO 17 on RaspberryPi)
      Black and White Dual Wire(SparkMax Communication) -
    
### **How we ensured Reliability and Safety**

We took extra care in insulating all exposed connections to prevent shorts or malfunctions. 

This was done to all soldered connections by applying heat-shrink tubing, hot gluing wire ends and using 
electrical tape wherever required for additional protection and to reinforce connection stability.
We used barrier terminal blocks and JST connectors which hold the wires firmly in place thus preventing them from moving around and accidentally causing short circuits or bending of wires.
    
### **How we made it convenient to assemble and dissasemble**

Ease of maintainence and assembly was another top priority. 

We soldered header pins onto the general purpose board in order to render the Arduino Nano, BNO055, and servo easily detachable and replaceable.
The screw in nature of the barrier terminal blocks not only added a layer of security to our electrical system but also served as a way to ensure quick maintanence. The wires can be removed and reattached by simply screwing and unscrewing the terminals. 
A similar story is for the the JST connectors, their ability to snap in place makes it easy to attach and detach the ultrasonic sensors
We also used crimp connectors for the switch, such that we could quickly remove and replace it if necessary since we had faced issues during practice of the switch being unreliable
    
































