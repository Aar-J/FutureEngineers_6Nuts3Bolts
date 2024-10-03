# Welcome to our GitHub!

# Introduction
We are team 6Nuts3Bolts, a dynamic trio of passionate robotics enthusiasts. 
Based off of the nature of the task, we divded the industry and each took on a key aspect of the challenge.

**Arham**: 

**Shauryaveer**:

**Ranveer**:

# Table of Contents
Car photos
Our Engineering Process
- Fundamental Parameters
- Mobility Management
  - How we achieved our target
  - Explanation
  - Iteration Process
  - Improvements
  - Parts list

- Power and Sense Management
  - How we achieved our target
  - Explanation
  - Iteration Process
  - Improvements
  - Parts list
    
- Obstacle Management
  - How we achieved our target
  - Explanation
  - Iteration Process
  - Future Improvements
  - Parts list
  
Acknowledgement to our mentor Sahil Gajera Sir

Thank you to the judges














    





  
  



# Our Engineering Process
We have used scoring criteria from the ruleblock as headings in our documentation to make it easy to navigate our repository.

It is vital to understand a problem and its features in depth before planning and undertaking its solution. Hence, we first spent a day analysing the challenge in depth and noting down a few principles, parameters, fundamental ideas off of which we could organize our thinking and streamline our ideation process to efficiently solve the challenge. 
Here are the principles we decided on:

## Fundamental Parameters
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

Here's how we went about turning our vision into reality

## **Mobility management**

### How we achieved our target

**How we made it Compact**

We began by visualizing how all the components could fit closely together, and we built around that idea. The space between parts is minimal, but we made sure it wouldn’t create any issues in performance or accessibility.
The overall length of the robot is limited by key components like the NEO 550 motor, bevel gears, and the steering system, while the width is determined by the size of the Spark MAX, ultrasonic sensor, servo, and battery. By carefully balancing the length and width, we were able to create a robot that is compact yet fully functional. The width isn't constrained by any specific part, it’s simply as wide as necessary to accommodate the essential components.

**How we ensured simplicity and practicality**

From the beginning, we adopted a mindset of keeping things simple. We've learned that complexity can quickly lead to chaos, especially when time is tight or you're troubleshooting under pressure. By focusing on simplicity, we narrowed our options and only considered ideas that were practical and easy to implement. If a solution met our goals without adding unnecessary complications, we ran with it. Simplicity also naturally led to practicality because fewer moving parts meant fewer things to go wrong, and every design choice was intentional and straightforward.

**How we made it Modular**

The entire robot is based around three main plates, with each subassembly between them individually 3D printed. This modular design gives us a lot of flexibility. If something goes wrong with a specific part, we don’t need to overhaul the entire system—just swap out the problem area. It makes troubleshooting and maintenance much quicker and less stressful.
We designed the robot to be broken down into three key systems: the drive system, the steering system, and the electronics assembly. Any part that doesn’t fall into one of these categories is mostly there to provide structural integrity and support to the main components. For instance, the bottom plate doesn’t serve any critical function other than strengthening the overall structure. This modular approach ensures that our robot remains easy to work on, upgrade, and maintain, which is key for long-term reliability.

### Explanation
**Electronics Mounting Plate** 
The electronics table offers ample space for organizing wiring effectively. It is spacious enough to accommodate most of the wiring, ensuring everything remains well-organized and accessible for easy maintenance and troubleshooting.

**Top Plate**
The top plate is the strongest and most robust part of the robot, serving as its backbone. It plays a vital role in every subsystem, providing structural integrity and supporting the entire design.

**Bottom Plate**
The bottom plate provides essential support and serves as a key aesthetic feature for the robot. It protects the belly of the robot from potential damage while also adding significant structural integrity to the overall foundation. By ensuring a strong base, the bottom plate helps maintain the robot's durability and stability during operation. Its role in reinforcing the lower framework makes it a critical component of the robot's design.

**Bevel Gears**  
The bevel gears are designed for durability, featuring a large diameter and sizable teeth. This design ensures they wear out more slowly, making them reliable and long-lasting components of the drive system.

**Motor Bracket**  
The motor bracket is small and simple in design, effectively performing its function without occupying excessive space. It optimizes space utilization while ensuring the motor is securely mounted.

**Camera Mount**  
The camera mount is tall and adjustable, providing flexibility in positioning without taking up much flat space on the electronics table. It offers several customization options to fit various configurations as needed.

**Steering System**  
The steering system is compact and straightforward, featuring a linkage-based design. It allows for the maximum possible steering angle and is highly reliable, ensuring excellent maneuverability and performance.

### Iteration process
We went through 4 iterations of the design. Here's a bit about them.

**Version 1**

![image](https://github.com/user-attachments/assets/e290e997-33fd-44ed-8cd8-65e9d1fdec23)


We began with a simple, open chassis design that provided ample space for future electronics and cabling, offering flexibility to adjust the layout as needed.

The motor and electronics were placed centrally to maintain balance and reduce the risk of tipping during movement.

The flat and spacious base was designed to simplify assembly and allow easy access to key components.

For the steering system, we initially used an approximate Ackermann configuration to improve cornering performance by adjusting wheel angles based on turning radius.

After evaluating the robot’s performance, we switched to a linkage-based steering system, which offered more straightforward control with fewer mechanical components, minimizing potential points of failure.

We integrated the bulky Limelight camera, mounting it high on a custom bracket to ensure optimal visibility for the robot's vision systems.

Although the camera’s size was disproportionate to the compact robot, we relied on it for initial tests due to its accuracy in target detection and our team's familiarity with its setup.

The camera placement was chosen to minimize interference from the robot's body and ensure accurate visual data capture.

This design iteration allowed us to explore several improvements for future versions, including lowering the base height to reduce the robot's center of gravity and increase stability,
transitioning to a layered architecture for better component arrangement and improved separation of electronics, minimizing signal interference, and
trimming excess space in the length and width of the frame to create a more compact and efficient design, maximizing maneuverability without sacrificing functionality.


**Version 2**

![image](https://github.com/user-attachments/assets/f1b01775-2a7b-4f02-8e70-b24a9479e18b)


In this iteration, we focused on making the design more compact and practical, even if it introduced some complexity.

Unlike the modular and adjustable nature of Version 1, this design was fully customized for the specific requirements of the use case.

The first major decision was to align the motor with the length of the robot, significantly reducing the overall width.

To achieve this, we implemented a 90-degree power transmission system using custom-designed, 3D-printed bevel gears (approx. 2 cm in diameter).

The custom motor mount could also house a REV Through Bore Encoder to measure back wheel rotations, but we decided it wasn’t necessary for this version.

We introduced a layered structure with three levels:

The top layer was exclusively for the electronics.

The lower layers housed wiring, the SPARK MAX controller, and other components.

After finalizing the battery choice, we built the robot layout around it to ensure proper space allocation and balance.

The electronics board was designed to be hot-swappable, allowing it to snap into place without screws, so electronics development could be done separately and easily integrated.

We also implemented a simple linkage-based steering system, powered by the MG996R servo, improving steering control while keeping the design compact and efficient.
The transition from Version 1 to Version 2 marked a significant leap, making the robot more space-efficient and purpose-built for the specific application.


**Version 3 (Abandoned)**

![image](https://github.com/user-attachments/assets/25114585-e849-43af-b3c6-d246602221cb)


In this version, we aimed to make the robot as small as possible, accommodating every element efficiently.

The chassis width was reduced to 8.4 cm (down from 10 cm), significantly improving maneuverability.

The overall height was also reduced, and although ground clearance wasn’t a priority, it was slightly improved for potential ground-facing sensors.

Early in the design, we realized shrinking the dimensions came with trade-offs.

The maximum turning angle of the steering wheels was reduced by 10-15 degrees on either side.

The servo had to be placed in an unconventional manner.

To address these issues, we explored adding 5-6 layers to the design to distribute components while keeping the robot compact.

Despite our efforts, feedback from testing Version 2 showed that width wasn’t a major concern, and while this version was sleeker, it presented too many complications.
The layered structure created challenges in both assembly and component access, making the design overly complex.

From this iteration, we learned that the current dimensions were already optimized, and future designs would likely stay within a tolerance of ±2-3 cm.

Making the robot smaller worsened the wiring complexity, as the compact spaces made routing cables and connections more difficult to manage.

This realization helped us pivot back to a more practical sizing while still focusing on overall efficiency.


**Version 4**

![image](https://github.com/user-attachments/assets/daf366dc-e880-402c-9ab2-913b4e5f64ce)


In this version, we started from scratch, incorporating lessons from previous iterations.

The width remained unchanged, but the length was significantly reduced.

We transitioned from a 20:1 UltraPlanetary gearbox to a 5:1 system, which, along with steering modifications, allowed us to achieve our most compact design yet.

The electronics table at the top was made wider, extending beyond the chassis but staying within dimensional constraints.

We moved away from the hot-swappable top plate design, as the snap-on system weakened after repeated use and occasionally broke off.

The bottom plate was refined to remove unnecessary parts and featured our team name cut out for weight reduction and aesthetic appeal.

The middle plate now carried the bulk of the structural load, becoming the backbone of the robot. The thickness of both the bottom and middle plates was increased from 3mm to 4mm, greatly improving strength and eliminating flex.

A key improvement was in the drive subsystem, during test runs, we noticed vibrations while turning, due to the lack of a differential system.
The inside and outside wheels rotated at the same speed, causing a mismatch.
To fix this, we reduced the gap between the wheels, minimizing vibration in a simple manner.
We also upgraded the bevel gears, increasing their size from 2 cm to 3 cm in diameter.
This made the gears much stronger, eliminating wear-and-tear issues.

Previously, we had to replace the smaller gears after every five runs, but with the new design, frequent replacements were no longer necessary.

Overall, this design marked the culmination of all our ideas and refinements, making it the most optimized and efficient version yet, combining technical improvements with practical design choices.


**Key Differences between the versions**
| **Aspect**                   | **Version 1** | **Version 2** | **Version 3 (Abandoned)** | **Version 4** |
|------------------------------|---------------|---------------|---------------------------|---------------|
| **Chassis Design**            | Simple, open chassis with spacious flat base for flexibility | Compact and customized, 90-degree power transmission via bevel gears | Extremely compact, 8.4 cm width; 5-6 layered design; trade-offs in turning radius | More compact than v2, width unchanged, reduced length |
| **Motor Placement**           | Central for balance | Aligned with the length, bevel gears for 90-degree power transmission | Motor placement compromised for size | Same as v2, with more robust gearing system |
| **Steering System**           | Approximate Ackermann, later switched to linkage-based | Linkage-based, powered by MG996R servo | Reduced turning angle due to compactness | Linkage-based with further steering modifications to reduce size |
| **Electronics Layout**        | Spacious, simple arrangement on a general-purpose board | Layered design with three levels, hot-swappable electronics board | 5-6 layers proposed, overly complex, compact | Wider electronics table, no hot-swappable design due to durability issues |
| **Camera System**             | Limelight camera, large and mounted high for optimal visibility |Limelight Camera Swapped for RaspberryPi Camera| Not specifically mentioned | Not specifically mentioned |
| **Frame Dimensions**          | Spacious, flexible for adjustments | Narrower (due to motor alignment) and more layered | Extremely compact (8.4 cm width), but overly complex | Reduced length, width unchanged; optimized overall dimensions |
| **Gearbox**                   |20:1 UltraPlanetary gearbox |Same as v1 | Same as v2 | Switched to 5:1 UltraPlanetary gearbox for compactness and speed|
| **Bevel Gears**               | Not used | 2 cm diameter, custom 3D-printed | Same as v2, but layering increased difficulty | 3 cm diameter, stronger, reduced wear and tear |
| **Material Strength**         | Standard 3 mm plates | Standard 3 mm plates | Same as v2 | Plates increased from 3 mm to 4 mm for improved structural strength |
| **Vibration Control**         | Not addressed | No differential system, resulting in vibrations | Not addressed | Reduced wheel gap to minimize vibrations during turns |
| **Testing and Feedback**      | Preliminary tests with bulky camera setup | Refined design with specific components, partial finalization | Abandoned due to complexity, compromised steering, and wiring issues | Final optimized version, most refined in terms of design and performance |
| **Complexity**                | Simple and flexible | More complex but optimized for purpose | Extremely complex and impractical | Balanced complexity with practical refinements |



### Future Improvements
If we had more time, we would likely explore a more complex design that branches off from the v3 concepts while integrating elements from the v4 robot. This hybrid approach would allow us to capitalize on the strengths of both iterations, leading to an ideal robot that embodies our design philosophy. By merging the compact efficiency and structural integrity of v3 with the advanced features and refined functionality of v4, we could create a robot that maximizes performance while enhancing maneuverability and adaptability. This exploration could involve developing a more sophisticated drive system or experimenting with innovative materials and configurations to further reduce weight and improve responsiveness. Ultimately, this integration of ideas would help us push the boundaries of our design capabilities and achieve our vision of an optimal robot tailored to our specific needs.


### Hardware Components list:
- Rev Duo 60mm Traction Wheels https://www.revrobotics.com/DUO-Traction-Wheels/
- **Chassis**
  - **Top plate**
  - **Bottom Plate**
- **Steering Mechanism**
  - **Linkage**
  - **Left Front**
  - **Right Front**
- **Bevel Gears**
- **Motor Bracket**
- **Electronics Mount**
- **Camera Mount**
- **1 x Servo horn**
- **20 x m3 10mm bolts**
- **2 x m3 30mm bolts**
- **16 x m3 nyloc nuts**
- **1 x 75mm shaft**
- **1 x 20mm shaft**
- **2 x shaft collars**
- **4 x 60mm rev wheels**

## **Power and sense management**

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
Wago connectors were used for connections between the SparkMax and Neo ensuring a tight and insulated fitting.
    
### **How we made it convenient to assemble and dissasemble**

Ease of maintainence and assembly was another top priority. 

We soldered header pins onto the general purpose board in order to render the Arduino Nano, BNO055, and servo easily detachable and replaceable.
The screw in nature of the barrier terminal blocks not only added a layer of security to our electrical system but also served as a way to ensure quick maintanence. The wires can be removed and reattached by simply screwing and unscrewing the terminals. 
A similar story is for the the JST connectors, their ability to snap in place makes it easy to attach and detach the ultrasonic sensors.
Wago connectors are convenient to make connections with components where cutting the wiring and making solder joints is not preffered due to the wire being inbuilt into the component like the SparkMax and NEO550.
We also used crimp connectors for the switch, such that we could quickly remove and replace it if necessary since we had faced issues during practice of the switch being unreliable

## **Explanation**

### Reason for choice of parts

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

### Circuit Schematic

![WRO Future Engineers Circuit Schematic](https://github.com/user-attachments/assets/8665c30f-97d0-4199-9b31-89a5496f39e5)


### Iteration Process



### Future Improvements



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
  https://www.xcluma.com/0.9v-5v-to-5v-600ma-usb-output-charger-step-up-power-module-mini-dc-dcboostconvertergad_source=1&gclid=CjwKCAjwgfm3BhBeEiwAFfxrGwnZnr6HztAhUfIc8EmXiPdcBPvQhlMLFXXWHMaUp1jXnO9AhzcHORoCvscQAvD_BwE
  
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
  
-**Wago Connectors**
 https://www.flipkart.com/wago-2-conductor-compact-inline-splicing-connectors-electrical-wire-connector/p/itmd8735b383bb17?pid=WJCHYGCR7GEYHDBV&lid=LSTWJCHYGCR7GEYHDBVIEKFMH&marketplace=FLIPKART&cmpid=content_wire-joint-connector_8965229628_gmc




## **Obstacle management**


# Acno
































