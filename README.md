# Welcome to our GitHub!

# Introduction
We are team 6Nuts3Bolts, a dynamic trio of passionate robotics enthusiasts. 
Based off of the nature of the task, we divded the industry and each took on a key aspect of the challenge.

**Arham**: 

He is in charge of the electronic systems as well as the documentation.

![WhatsApp Image 2024-10-04 at 6 19 59 PM](https://github.com/user-attachments/assets/f6241dd0-05e7-4534-9ef5-7cef05707d50)

**Shauryaveer**:

![WhatsApp Image 2024-10-04 at 6 20 24 PM](https://github.com/user-attachments/assets/1370b9de-b810-4a93-ac95-c5978004c1c2)

He is our main designer and constructor and worked on the car's mechanisms

**Ranveer**: 

![WhatsApp Image 2024-10-04 at 6 20 25 PM](https://github.com/user-attachments/assets/d438b62a-15f7-4e45-9bb9-086e6d58676f)

He is our programming lead, in responsible for all the code and processing on our robot.

**Team Photo**:


# Table of Contents
Car photos

Our Engineering Process

- Fundamental Parameters
- Mobility Management
  - Explanation
  - Iteration Process
  - How we achieved our target
  - Improvements
  - Parts list

- Power and Sense Management
  - Explanation
  - Iteration Process
  - How we achieved our target
  - Improvements
  - Parts list
    
- Obstacle Management
  - How we achieved our target
  - Explanation
  - How we achieved our target
  - Future Improvements
  
Acknowledgement to our mentor Sahil Gajera Sir

Thank you to the judges


# Car Photos

### Top View

![Untitled design (41)](https://github.com/user-attachments/assets/fa3ed176-4482-46d3-966b-5a507e9104ad)

### Bottom View

### Front View

### Back View

### Left side 

### Right Side

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
- Simple and organized
- Easy to navigate, debug and troubleshoot
- Flexible, able to evolve easily to overcome any issues or edge cases

Based off these fundamental ideas, we aimed to conceptualize our robot.
Next, we immediately begain the prototyping and iteration process.

Here's how we went about turning our vision into reality

## **Mobility management**

### Explanation

**Why we chose the RevRobotics NEO550**

![Untitled design (15)](https://github.com/user-attachments/assets/26456897-bea2-4da2-b72c-7a1d0638b2f2)


- It has an absolutely phenomenal power to weight ratio (weighing only 140grams) as well as very high acceleration and has a free running speed of upto 11000 RPM. We have geared it in a 5:1             ratio. 
- We had previously used this motor in FRC (FIRST Robotics Competition) and hence were comfortable operating with it.
- It has excellent speed control and is easy to integrate and program with the SparkMax motor controller.
- We had initially considered making a smaller robot and at the time had considered using an N20 500 RPM Encoder motor, however this placed a lot of restrictions on our other electronics and design. We also considered using a standard Johnson 500 RPM motor, or a TT Gearbox motor however we rejected these for similar reasons as well as the fact that the NEO 550 just outclassed all 3


  
**Why we chose MG996R Servo**

![Untitled design (17)](https://github.com/user-attachments/assets/4b56777f-e333-4446-bb65-d5e678c8a31b)

- It is a popular and reliable servo which for us is delivering about 9.5kgcm(since we are powering it through the RaspberryPi 5V pin)
- It is easily able to steer our robot even at high speeds.
- The position accuracy it is able to provide is relaible and it is able to steer at a rate of about 0.30 sec/60° degrees according to our measurements.

**Electronics Mounting Plate** 

![Untitled design (22)](https://github.com/user-attachments/assets/6e140fad-c1ad-48fc-a7ca-da6544f76aa2)

![Untitled design (29)](https://github.com/user-attachments/assets/c8a7be4b-8979-40d6-9d7e-6cbb1bf7db3d)


The electronics table offers ample space for organizing wiring effectively. It is spacious enough to accommodate most of the wiring, ensuring everything remains well-organized and accessible for easy maintenance and troubleshooting.


**Top Plate**

![Untitled design (23)](https://github.com/user-attachments/assets/2b114052-4044-4fd0-98a4-c4719d0c3e10)

![Untitled design (31)](https://github.com/user-attachments/assets/374ca9be-4cd0-41f4-9cbe-0662ce5149e8)


The top plate is the strongest and most robust part of the robot, serving as its backbone. 

It plays a vital role in every subsystem, providing structural integrity and supporting the entire design.

**Bottom Plate**

![Untitled design (24)](https://github.com/user-attachments/assets/9a76d7ae-a4c2-43fb-8ad1-1b5610d95315)

![Untitled design (30)](https://github.com/user-attachments/assets/6fa425bc-fd75-4b9b-a691-30875230e236)


The bottom plate provides essential support and serves as a key aesthetic feature for the robot. It protects the belly of the robot from potential damage while also adding significant structural integrity to the overall foundation. By ensuring a strong base, the bottom plate helps maintain the robot's durability and stability during operation. Its role in reinforcing the lower framework makes it a critical component of the robot's design.

**Bevel Gears**  

![Untitled design (25)](https://github.com/user-attachments/assets/82238a56-f46d-4b0a-8b3a-da0ba399a555)

![Untitled design (32)](https://github.com/user-attachments/assets/43d820ab-0fa4-4fe2-bbcb-ebc4e06b26f3)


The bevel gears are designed for durability, featuring a large diameter and sizable teeth. This design ensures they wear out more slowly, making them reliable and long-lasting components of the drive system.

**Motor Bracket**  

![Untitled design (26)](https://github.com/user-attachments/assets/b5ad1521-8ca4-4adb-aee0-2f33dcd7c8aa)

![Untitled design (33)](https://github.com/user-attachments/assets/b0957af5-fd1d-42b0-8536-dfd578967b24)

The motor bracket is small and simple in design, effectively performing its function without occupying excessive space. 
It optimizes space utilization while ensuring the motor is securely mounted.

**Camera Mount**  

![Untitled design (28)](https://github.com/user-attachments/assets/2788b94f-cce0-4507-904c-f9b6ee310ce2)


The camera mount is tall and adjustable, providing flexibility in positioning without taking up much flat space on the electronics table. It offers several customization options to fit various configurations as needed.

**Steering System**  

![Untitled design (27)](https://github.com/user-attachments/assets/10a2ad7f-63c1-40f5-80e1-b68228a2e334)

![Untitled design (34)](https://github.com/user-attachments/assets/a2025f5d-8f8d-4129-9199-837189ffacf2)


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

### How we achieved our target

**How we made it Compact**

We began by visualizing how all the components could fit closely together, and we built around that idea. The space between parts is minimal, but we made sure it wouldn’t create any issues in performance or accessibility.
The overall length of the robot is limited by key components like the NEO 550 motor, bevel gears, and the steering system, while the width is determined by the size of the Spark MAX, ultrasonic sensor, servo, and battery. By carefully balancing the length and width, we were able to create a robot that is compact yet fully functional. The width isn't constrained by any specific part, it’s simply as wide as necessary to accommodate the essential components.

**How we ensured simplicity and practicality**

From the beginning, we adopted a mindset of keeping things simple. We've learned that complexity can quickly lead to chaos, especially when time is tight or you're troubleshooting under pressure. By focusing on simplicity, we narrowed our options and only considered ideas that were practical and easy to implement. If a solution met our goals without adding unnecessary complications, we ran with it. Simplicity also naturally led to practicality because fewer moving parts meant fewer things to go wrong, and every design choice was intentional and straightforward.

**How we made it Modular**

The entire robot is based around three main plates, with each subassembly between them individually 3D printed. This modular design gives us a lot of flexibility. If something goes wrong with a specific part, we don’t need to overhaul the entire system—just swap out the problem area. It makes troubleshooting and maintenance much quicker and less stressful.
We designed the robot to be broken down into three key systems: the drive system, the steering system, and the electronics assembly. Any part that doesn’t fall into one of these categories is mostly there to provide structural integrity and support to the main components. For instance, the bottom plate doesn’t serve any critical function other than strengthening the overall structure. This modular approach ensures that our robot remains easy to work on, upgrade, and maintain, which is key for long-term reliability.


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
- **1 x Servo horn** (comes with servo)
- **20 x m3 10mm bolts** https://robokits.co.in/robot-parts/nut-bolts-standoffs/allen-cap-socket-head-bolts/m3-x-10-mm-socket-head-cap-stainless-steel-304-bolt-moq-15-pcs
- **2 x m3 30mm bolts** https://robokits.co.in/robot-parts/nut-bolts-standoffs/allen-cap-socket-head-bolts/m3-x-30-mm-socket-head-cap-stainless-steel-304-bolt-moq-15-pcs
- **16 x m3 nyloc nuts** https://robokits.co.in/robot-parts/nut-bolts-standoffs/nuts/m3-nyloc-nuts-304-stainless-steel-moq-25-pcs
- **1 x 90mm shaft** https://www.revrobotics.com/5mm-Hex-Shafts/#REV-41-1348-PK4
- **1 x 20mm shaft** (can be cut from longer shaft)
- **2 x shaft collars** https://www.revrobotics.com/rev-41-1327-pk10/
- **4 x 60mm rev wheels** https://www.revrobotics.com/DUO-Traction-Wheels/#REV-41-1350-PK4

## **Power and sense management**

## **Explanation**

### Reason for choice of parts

**RaspberryPi 4B**

![Untitled design (35)](https://github.com/user-attachments/assets/b268cea5-e015-4d46-8e09-3f54ef0ec3e7)


- With its quad-core ARM Cortex-A72 64-bit 1.5GHz processor and 8GB RAM it meant that we would never face a computationl bottleneck, even with the heavy task of image processing in the obstacle         challenge.
- Its ability to be programmed and controlled wirelessly was a boon during the testing and debugging phase as we could run the robot almost continuously without having to detach and reattach            the cable for uploading code.
- Its extensive use and testing was the reason we chose to go with the RaspberryPi 4B instead of the newer RaspberryPi 5. If there was ever an issue we faced, it could most likely be solved by          searching up the problem.

**RaspberryPi Camera Module 3 with Wide Angle lens**

![Untitled design (36)](https://github.com/user-attachments/assets/f20e7c32-37de-47a2-938a-2b0732e7ff77)


- We chose this mainly for its ease of integration and compatability with the RaspberryPi. 
- Its wide FOV (120 degrees), high resolution(12 megapixels), autofocus feature and ability to sense color in a wide range of lighting conditions allowed for efficent obstacle detection and             sensing from varying distances and angles even while moving at high speeds

**Arduino Nano**

![Untitled design (37)](https://github.com/user-attachments/assets/91d78d54-0efb-44dd-b30f-d73b39976214)

- The use of the Arduino Nano in our robot is solely to gather data from the ultrasonic sensors and relay it to the RaspberryPi. 
- Hence its compactness and low power consumption was the main reason we chose to use it.

**BNO055 IMU**

![Untitled design (38)](https://github.com/user-attachments/assets/82430926-f698-4311-973f-7d68fe5aa4e2)

- The BNO055 is a highly tested and reliable sensor. We had used it earlier in FTC(First Tech Challenge) as well as in a drone we made. We had also used it in Future Engineers the previous year.
- It has an inbuilt sensor fusion algorithm and it is easy to integrate with the RaspberryPi, communicating over I2C.

**RevRobotics SparkMax Motor Controller**

![Untitled design (18)](https://github.com/user-attachments/assets/f4c5dbf0-d33c-48a3-976f-3b59b8d2d880)

- Using the NEO550 meant we would have to use this since they are complimentary pieces of hardware.
- Its inbuilt current limiting feature also allows for the motor to remain safe from sudden power surges.

**HC-SRO4 Ultrasonic Sensors**

![Untitled design (14)](https://github.com/user-attachments/assets/da329699-54ac-43f2-8ef8-96a696106bcb)
- These are widely available and a popular choice of sensor although sometimes they may be unreliable, with good programming they can be made to work just fine. 
- There are many resources and libraries available online to control these effectively making both programming and troubleshooting easy to do.
- Their accuracy is reasonable, able to provide output within a 2-3mm range of error and are also able to maintain consistency at moderate speeds, providing data every 30ms.
- Apart from that, its also easy to integrate

**Xcluma USB Buck Converter**

![Untitled design (16)](https://github.com/user-attachments/assets/976be40f-9399-4871-acec-6abb57b4bccf)


- It was able to provide a more stable output of 5V than the buck converter we were previously using. It also made it such that we could easily power the RaspberryPi through its USBC port.
- It was also more compact than the previous buck.
- Its built in safety feature of preventing against overvoltage and overcurrent proved to be useful especially during testing.

**2200MAh 40C 12V LiPo Battery** 

![Untitled design (39)](https://github.com/user-attachments/assets/137684c1-1fef-4514-a98d-b9a49b995c0c)

- We needed a high power battery since the electronic components we used(RaspberryPi while image processing, NEO550) were quite power hungry.
- It was also capable of providing our robot with a long runtime. We can run our robot for 12 minutes continuously.

### Circuit Schematic

![WRO Future Engineers Circuit Schematic](https://github.com/user-attachments/assets/8665c30f-97d0-4199-9b31-89a5496f39e5)


### Iteration Process

**Version 1**

This was a prototyping version, simply to test the circuit and have a robot capable of moving while we worked on a better version.
It consisted of the Electronics mounted on a cardboard plate and the use of a prototyping board fundamentally composed on 4 buck converters. There were wires going everywhere, even outisde the perimeter of our bot. However, this was only ever meant to be a prototyping version. 

![Carboard Plate (1)](https://github.com/user-attachments/assets/1c7484e9-9b19-4533-9836-e13fd27eb4cd)

**Version 2**
This was also merely a prototyping version intended on having a functional robot to program. The differe

![More well positioned Cardboard Plate](https://github.com/user-attachments/assets/200de56e-0422-4285-8648-1b30d4dbfae6)



### **How we achieved Clean and Organized wiring**

To keep our wiring system easy to manage, we focused on clarity, organization and structure in all connections.

We used solid core wire for connections since they can be bent into shape making wiring neat and easy to solder.
We soldered all wire connections and mounted them on a general purpose board providing a solid foundation for the wiring, minimizing loose wires and clutter.
Every wire was labeled and color-coded, making it simple to track individual connections. This helped ensure quick identification of components during assembly and troubleshooting.
  
Red - VCC wires 🟥

Black - GND wires ⬛

Purple - PWM Signal (Pin 33 or GPIO 13 on RaspberryPi) 🟪

Yellow(Ultrasonic) - TRIG (Pins D3 and D7 on Nano) 🟨

Blue(Ultrasonic) - ECHO (Pins D4 and D6 on Nano) 🟦

Yellow(BNO055) - SDA (Pin 3 or GPIO 2 on RaspberryPi 🟨

Blue(BNO055) - SCL (Pin 5 or GPIO 3 on RaspberryPi) 🟦

Blue(Button) - SIGNAL (Pin 11 or GPIO 17 on RaspberryPi) 🟦 

Black and White Dual Wire(SparkMax Communication) - ⬛⬜ (Pin 33 GPIO 18 and Pin 34 or Ground)
    
### **How we ensured Reliability and Safety**



We took extra care in insulating all exposed connections to prevent shorts or malfunctions. 



This was done to all soldered connections by applying heat-shrink tubing, hot gluing wire ends and using 
electrical tape wherever required for additional protection and to reinforce connection stability.
We used barrier terminal blocks and JST connectors which hold the wires firmly in place thus preventing them from moving around and accidentally causing short circuits or bending of wires.
Wago connectors were used for connections between the SparkMax and Neo ensuring a tight and insulated fitting.
    
### **How we made it convenient to assemble and dissasemble**

![Untitled design (21)](https://github.com/user-attachments/assets/046e0c53-fc12-42d1-b049-2754668d87a7)

Ease of maintainence and assembly was another top priority. 

We soldered header pins onto the general purpose board in order to render the Arduino Nano, BNO055, and servo easily detachable and replaceable.
The screw in nature of the barrier terminal blocks not only added a layer of security to our electrical system but also served as a way to ensure quick maintanence. The wires can be removed and reattached by simply screwing and unscrewing the terminals. 
A similar story is for the the JST connectors, their ability to snap in place makes it easy to attach and detach the ultrasonic sensors.
Wago connectors are convenient to make connections with components where cutting the wiring and making solder joints is not preffered due to the wire being inbuilt into the component like the SparkMax and NEO550.
We also used crimp connectors for the switch, such that we could quickly remove and replace it if necessary since we had faced issues during practice of the switch being unreliable






### Future Improvements

- We plan on using PCB Design software to create a circuit design and then have that PCB printed and manufactured. This will almost completely eliminate     small wired connections and chance of circuit failure.
- We also plan on swapping out the HC-SR04 Ultrasonic sensors with faster and more reliable ones like the URM09 or SEN001.
- We may also swap out the RaspberryPi for a faster controller like the Jetson Nano
- 


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
In this sections first we will first discuss how we solved the obstacle challenge and then move onto the  solution for the open round challenge as well as a general explanation of our software and logic flow.

### How we achieved our target

- f
- f
- f

  
### Explanation

#### **Obstacle Challenge**

First we begin by importing all the libraries

<img width="286" alt="Screenshot 2024-10-04 at 10 26 26 AM" src="https://github.com/user-attachments/assets/9b523ad5-e819-4962-b974-f98ca9a56ad3">

import time 
- The time library, as the name suggests allows us to use time related functions like delays.

<img width="317" alt="Screenshot 2024-10-04 at 10 26 46 AM" src="https://github.com/user-attachments/assets/e0d4c704-40b0-4505-895b-d69310235720">

  
import board
- Its use is primarily to access pins on the RaspberryPi.

  
<img width="290" alt="Screenshot 2024-10-04 at 10 27 02 AM" src="https://github.com/user-attachments/assets/f96954ce-7e75-49d2-a168-eb188038d493">

import busio
- This library allows us to access external buses and serial protocols allowing for hardware acceleration on the RaspberryPi.

<img width="493" alt="Screenshot 2024-10-04 at 10 27 24 AM" src="https://github.com/user-attachments/assets/9c11009f-34e1-43ec-9f19-eb579e7152c0">

  
import adafruit_bno055   
- Library for BNO055 IMU sensor

<img width="234" alt="Screenshot 2024-10-04 at 10 27 43 AM" src="https://github.com/user-attachments/assets/1a237e78-b00b-419c-977a-ca158bd15b60">

import sys
-  This library basically allows us to run functions and call from different files and parts of code. Its gives us commands to access system related variables and functions.

<img width="322" alt="Screenshot 2024-10-04 at 10 28 02 AM" src="https://github.com/user-attachments/assets/b1e16ebd-71c5-45a4-ae34-e92b7a8b246a">


import serial  
- This allows for serial communication with external devices. We communicate with the Arduino Nano over serial

<img width="1058" alt="Screenshot 2024-10-04 at 10 28 16 AM" src="https://github.com/user-attachments/assets/452f1812-624b-43f3-9100-05828492ee0c">

sys.path.append('/usr/lib/python3/dist-packages')  
- We have created custom packages for the left journey and right journey of the open round. Both are called. The robot must decide which one to run.

<img width="321" alt="Screenshot 2024-10-04 at 10 28 35 AM" src="https://github.com/user-attachments/assets/63cf3fcf-23eb-4e27-89a3-3b8103e7e66c">
  
import pigpio   
- The RaspberryPi's software PWM signal is often unstable and unreliable. The pigpio library solves this issue generation a hardware PWM on the the         
  RaspberryPi.

<img width="888" alt="Screenshot 2024-10-04 at 10 28 54 AM" src="https://github.com/user-attachments/assets/6932beb2-6e1b-46d3-b998-727b8ece307d">

from picamera2 import Picamera2, Preview  
- Camera library for handling the Raspberry Pi camera
  

<img width="276" alt="Screenshot 2024-10-04 at 10 29 08 AM" src="https://github.com/user-attachments/assets/b2cda5f5-d644-4b27-bd74-fa5a713fc3a1">

import cv2  
- Here we are importing OpenCV for camera processing and display. This handles all of the vision processing.

  
<img width="187" alt="Screenshot 2024-10-04 at 12 44 34 PM" src="https://github.com/user-attachments/assets/17519582-7ef7-4c5b-8705-b1d725810680">

import numpy as np
- Here we import NumPy for numerical operations using it in conjunction with OpenCV for image data processing.

<img width="254" alt="Screenshot 2024-10-04 at 12 45 28 PM" src="https://github.com/user-attachments/assets/2696f684-fe59-4bfb-a302-ae6361609c2b">

import Blue_detected as b1
- This is a custom module containing functions for color detection.


Next we set up all the communication protocols, declare all the control variables in our program and initialise the necessary objects. 
We will use these to build our logic.

<img width="1134" alt="Screenshot 2024-10-04 at 12 49 01 PM" src="https://github.com/user-attachments/assets/db2cf8f7-8dae-430b-91ab-9edfce9b775e">

- We create a Picamera2 object to handle camera operations.
  
- The video configuration is set to a resolution of 640x480 pixels, with a frame duration limit of 33.33 milliseconds, which corresponds to 30 frames per second.
  
- The camera is then started, preparing it to capture images.

  

<img width="374" alt="Screenshot 2024-10-04 at 10 33 41 AM" src="https://github.com/user-attachments/assets/f6dd3423-100d-4e37-b27d-4e9919f3cc1a">

pi = pigpio.pi() 
- Initializes the pigpio library for GPIO control

<img width="638" alt="Screenshot 2024-10-04 at 10 35 23 AM" src="https://github.com/user-attachments/assets/12a88ba5-a541-4267-af91-9c5f45e24958">


pi.set_mode(18, pigpio.OUTPUT)  
- Set GPIO pin 18 as an output (for NEO550 Motor)
  
pi.set_mode(13, pigpio.OUTPUT) 
-  Set GPIO pin 13 as an output (for MG996R Servo)

<img width="799" alt="Screenshot 2024-10-04 at 10 34 47 AM" src="https://github.com/user-attachments/assets/e2287659-3f0e-46aa-b39f-dd8bf8c43c03">


i2c = busio.I2C(board.SCL, board.SDA)   
- Initializing I2C bus for communication with the IMU

<img width="882" alt="Screenshot 2024-10-04 at 10 35 39 AM" src="https://github.com/user-attachments/assets/801bd4ad-fec8-4a76-9be1-ef0bd4769a42">


ser = serial.Serial('/dev/ttyACM0', 9600)  
- Setting up a serial connection to an external device (Arduino Nano) at 9600 baud rate

<img width="865" alt="Screenshot 2024-10-04 at 10 35 58 AM" src="https://github.com/user-attachments/assets/620b533a-9c80-40fc-b4b8-90e75cb1e8f1">


sensor = adafruit_bno055.BNO055_I2C(i2c)  
- Initializing the BNO055 sensor using I2C

<img width="332" alt="Screenshot 2024-10-04 at 10 40 31 AM" src="https://github.com/user-attachments/assets/01ed42a0-ed34-4857-846a-040699c12ea5">

heading = 0.0   
- To store the heading (direction) from the IMU sensor

<img width="241" alt="Screenshot 2024-10-04 at 10 40 57 AM" src="https://github.com/user-attachments/assets/17669f1f-a5ea-4171-8361-3492d5cdd780">
  
dis = 0.0  
- To store the distance from the left sensor
  
<img width="280" alt="Screenshot 2024-10-04 at 10 41 05 AM" src="https://github.com/user-attachments/assets/716f0033-f278-442e-aa35-e1185f693b73">
 
value = 360 
- Value to control servo/motor position

<img width="272" alt="Screenshot 2024-10-04 at 10 41 30 AM" src="https://github.com/user-attachments/assets/cc566df5-3954-47f2-bc5c-78150a3de01d">

count = 0  
- A counter to count number of loop iterations

<img width="280" alt="Screenshot 2024-10-04 at 12 52 11 PM" src="https://github.com/user-attachments/assets/6d06f373-0de9-44b9-a6ea-5dc517a26d0a">

arR = arG = yy = xg = xr = 0
- These are variables for color detection areas.

<img width="169" alt="Screenshot 2024-10-04 at 12 56 35 PM" src="https://github.com/user-attachments/assets/c233dac5-5ccc-4420-905b-4e074948dde1">

orange = False
- Flag variable for if orange color is detected.

<img width="407" alt="Screenshot 2024-10-04 at 10 42 12 AM" src="https://github.com/user-attachments/assets/e6afde50-60e3-4bdb-920e-3bc3ed46e21b">

increment = False  
- Flag for controlling incremental behavior


  
<img width="265" alt="Screenshot 2024-10-04 at 10 42 44 AM" src="https://github.com/user-attachments/assets/9b53b124-32ec-4668-8d55-b86a3b865432">

flag = True  
- Flag variable to track state


  
<img width="276" alt="Screenshot 2024-10-04 at 10 43 01 AM" src="https://github.com/user-attachments/assets/ba531017-740c-4ef8-a204-986112c10f6c">

init = True  
- Flag variable to track initialization state

PID Controller

Here we initialise our PID function

<img width="232" alt="Screenshot 2024-10-04 at 11 54 26 AM" src="https://github.com/user-attachments/assets/222e70d4-4253-4bd9-986b-fc262bc11dfa">

The input parameters for the PID Controller are :

**y** 
- This is the target heading or the direction you want the robot to face.
  
**heading** 
- This stores the current heading of the robot, i.e., the direction the robot is currently facing, measured by the BNO055 sensor.
  
**kP**
- This represents the proportional constant used to determine how much correction to apply based on the error. The higher the constant, the more   
  aggressively the robot will correct its heading.
  
<img width="254" alt="Screenshot 2024-10-04 at 11 55 24 AM" src="https://github.com/user-attachments/assets/f34ac108-5ead-4c7c-9661-5fbef5adf656">

Here we normalize our "y" or target heading.
- This part ensures y is normalized within the range of -180 to 180 degrees.
  
- The idea is to convert the heading into a more manageable format that can be used for comparison and calculation.
  
- If y is less than 360 - y, it remains unchanged.
  
- If y == 360 - y, meaning it’s exactly opposite (180 degrees), it's set to 180 degrees.
  
- Otherwise, it subtracts y from 360, effectively flipping it to the opposite direction.

  <img width="300" alt="Screenshot 2024-10-04 at 11 57 05 AM" src="https://github.com/user-attachments/assets/9a7a47d5-0a5e-494e-a163-3af0ad753024">

Similarly, this block normalises our current heading.

In this block, we calculate our error.

<img width="291" alt="Screenshot 2024-10-04 at 11 59 03 AM" src="https://github.com/user-attachments/assets/3f4c3e00-2fa1-4119-820d-e97cc7df237e">

- Error is the difference between the current heading and the target heading.
  
- This error is used to determine how much the robot needs to adjust its steering to correct its path.
  
- There are three conditions:
  
  - Both headings are negative: The error is simply the difference between heading and y.
  - Heading is negative, but the target is positive: The error is the sum of y and heading.
  - In all other cases: The error is calculated as the difference between heading and y.
 

Based off this, we calculate our turn value and return it.

<img width="440" alt="Screenshot 2024-10-04 at 12 01 44 PM" src="https://github.com/user-attachments/assets/bd820241-a43c-4d82-b3b9-2aeb9c8c6f91">


- This line calculates the servo pulse width for the robot’s steering servo based on the error.

- The idea is to adjust the robot’s steering proportionally to the error, which means the bigger the error, the bigger the correction.

- The formula is: 1200 - error * kP, where 1200 is the neutral position (centered steering), and error * kP is the correction based on how far off the 
  heading is.

- To prevent extreme values, the min and max functions are used to clamp the output between 800 and 1600. These limits ensure that the servo doesn’t exceed 
  its physical range


This is the main control loop for image capture and processing.

<img width="1002" alt="Screenshot 2024-10-04 at 12 57 52 PM" src="https://github.com/user-attachments/assets/7aa072e8-2987-4bd3-a304-0a673850cbda">

Image Capture:

- The camera captures an image array into img.


Image Processing:

- Color Conversion: The image is converted from BGR to RGB format for compatibility with the OpenCV functions.
  
- Color Detection: The program calls color detection functions from the Blue_detected module:
  
- red_detect(img): Detects red areas in the image and returns the image with markings, along with the area (arR), and coordinates (xr, yr).
  
- green_detect(img): Similar function for detecting green areas.
  
- color_detect(img, lower, upper, "blue"): Detects blue areas with specified lower and upper color thresholds.
  
- A second call to color_detect is used to detect orange areas, with specific HSV values.

  
Display:

- A white rectangle is drawn on the top part of the image frame for visual guidance, and the processed image is displayed in a window titled “frame.”

In this block, we retrieve sensor data.

<img width="666" alt="Screenshot 2024-10-04 at 1 02 28 PM" src="https://github.com/user-attachments/assets/e1224380-c979-4763-bae6-287a753d728d">

- The robot finds its current heading, roll, and pitch from the BNO055 sensor's Euler angles.
  
- The heading is clamped to ensure it stays within the range of 0 to 360 degrees.
  
Distance Measurement:

- The program reads a line from the serial port, decoding it to a string. It expects distance data in a comma-separated format.
  
- The data is split into two float values, representing distance measurements (dis for one side and distanceRight for another side).
  
- If reading fails, both distance values are defaulted to 0.

This block contains the color processing logic.

<img width="339" alt="Screenshot 2024-10-04 at 1 04 45 PM" src="https://github.com/user-attachments/assets/bbbfc726-744d-4cfd-a595-bec4447ffe9a">

- The code checks the areas of detected colors:
  
- If the detected area for blue (yy) is between 100 and 250, it sets the flag blue1 to True.
  
- If yy exceeds 340, it sets another flag blue2 to True.
  
- The robot checks if both blue flags are set and if an orange area (yy2) is detected. If so, it sets the orange flag to True, indicating that it can 
  respond to the orange color.

Next we have the Servo control logic.

<img width="800" alt="Screenshot 2024-10-04 at 1 06 04 PM" src="https://github.com/user-attachments/assets/6ede5506-da72-4b9f-98ff-5ff0680117f8">

- If a significant red (arR) or green (arG) area is detected (both with area thresholds), it sets the flag to True and resets orange to False.
  
- If the orange flag is set and the distance (dis) is greater than 15, it executes specific logic for turning towards orange.
  
Default Case:

- If no significant colors are detected, it defaults to adjusting the servo's pulse width using the PID control function.
  
- If increment is True, it increments the count and resets the increment flag, allowing for controlled execution across multiple iterations.

Lastly we have the stopping procedures

<img width="307" alt="Screenshot 2024-10-04 at 1 10 49 PM" src="https://github.com/user-attachments/assets/c61ab59a-57af-469e-9c98-351cd4e081b8">

- This stops all active servo and motor operations by setting their pulse width to 0, effectively disabling them.
  
- All OpenCV windows are closed to free up resources.
  
- The camera is stopped, ensuring it is no longer capturing or processing images.
  
- The pigpio connection is released, completing the stopping process.

  This is how we solved the Obstacle Challenge.

#### **Open Round**


**Logic Flowchart**
  
![algorithm_flowchart](https://github.com/user-attachments/assets/f694ea93-8fb8-4353-9f17-779f5dc22ccb)


The setup of the libraries and pins and communication protocils for the Journey Right and Left programs is the same as the obstacle challenge, minus a few hence, explaining that once again would be redundancy.


Only the left and right journey programs need to be imported here seperately.

<img width="531" alt="Screenshot 2024-10-04 at 10 29 41 AM" src="https://github.com/user-attachments/assets/289d4a76-48d5-4726-9f7c-3b43684cac31">

import JourneyLeft as l  # Custom module to handle left-side journey logic
import JourneyRight as r  # Custom module to handle right-side journey logic
- These are the Journeys we made for either running the robot clockwise or counterclockwise. Their explanation is just after.

<img width="300" alt="Screenshot 2024-10-04 at 10 42 29 AM" src="https://github.com/user-attachments/assets/5c39fcd2-ea6d-4bd4-aa2b-2af77a657878">

logic = False  
- Flag variable for decision logic, to decide whether to run left journey or right journey


<img width="207" alt="Screenshot 2024-10-04 at 10 43 18 AM" src="https://github.com/user-attachments/assets/c8836b31-5e56-44e1-836d-2e129c2c44da">

left = 0  
- Flag variable to track whether the robot is turning left or right

  
<img width="312" alt="Screenshot 2024-10-04 at 10 43 31 AM" src="https://github.com/user-attachments/assets/8a86c8e7-864d-45f8-bc39-9b718ee1c5e6">

time.sleep(3)  
- Delay for 3 seconds before starting the main loop

Now we come to the main loop of our program.

<img width="674" alt="Screenshot 2024-10-04 at 10 45 54 AM" src="https://github.com/user-attachments/assets/d3182a30-1361-4b3a-a7c2-c5251f10c02e">

- The main loop runs as long as count is less than 3.
  
- sensor.euler: Reads the Euler angles from the BNO055 sensor, including the heading (yaw). We calculate our error based off this value

- The try-except block ensures the heading stays within the range of 0 to 360 degrees. If there's an error in reading the sensor, the heading is set to 0.
  
- ser.readline(): Reads a line of distance data from the Nano.
  
- The try-except block attempts to split the incoming data into two values (dis for the left distance and distanceRight for the right distance). If parsing 
  fails, both distances are set to 0.

Within this loop we have 3 logics:
1. Left and right journey Logic

   <img width="1080" alt="Screenshot 2024-10-04 at 10 49 57 AM" src="https://github.com/user-attachments/assets/47d5de99-ef38-4600-a9f7-b94648179db1">

- If the robot is set to move left, (left == 1), then it calls the L_journey() function from the JourneyLeft module, which handles the logic for left-side movement. The function returns updated values for value, logic, flag, etc.
  
- Similarly, if the robot is set to move right, (left == 2), it calls the R_journey() function from the JourneyRight module, which handles the logic for   
  right-side movement.
  
- The variable init ensures that certain behaviors only happen on the first run of the loop.


2. Distance Comparison Logic
   
   <img width="1079" alt="Screenshot 2024-10-04 at 10 50 55 AM" src="https://github.com/user-attachments/assets/2c2526c0-8cae-44a4-89f9-6a5ff3ff4a73">

- If the left distance (dis) is greater than the right distance and both are more than 100 cm, the robot turns left by calling the L_journey() function.
  
- Similarly if the right distance is greater than the left, the robot turns right by calling the R_journey() function.
  
- This logic ensures the robot chooses which direction to move based on sensor readings.


3. Default(Straight movement) and exit logic
   
   <img width="366" alt="Screenshot 2024-10-04 at 10 51 45 AM" src="https://github.com/user-attachments/assets/62bc5541-f199-410a-bae8-ca4bbff4b23c">

- If the robot is neither turning left nor right, it calls the default move() function from the JourneyLeft module, which handles straight-line movement.
- The cv2.waitKey(1) function listens for keyboard input. If the user presses 'Q' or 'q', the loop exits, stopping the robot.

Final actions after the loop:

<img width="306" alt="Screenshot 2024-10-04 at 10 54 39 AM" src="https://github.com/user-attachments/assets/26cc3a41-2878-4e97-a28a-66c3ed0005fd">

- After the loop ends, the robot performs a final stopping movement.
- pi.set_servo_pulsewidth(13, 0) stops the servo or motor connected to GPIO pin 13 by setting the pulse width to 0, ensuring the robot halts.

Here's an explanation of the journey logic explained using the example of the Journey Right program.

The setup of the libraries and pins for the Journey Right and Left programs is the same hence, explaining that once again would be redundancy.

Finally, this is the R_Journey function

<img width="774" alt="Screenshot 2024-10-04 at 12 05 05 PM" src="https://github.com/user-attachments/assets/b10602af-dab2-4c90-aad9-a318f6ba0a10">

This section resets the variables when the journey starts.
We also display our enthusiasm upon its initialisation.


In case we encounter a large right distance, we handle it in this block

<img width="369" alt="Screenshot 2024-10-04 at 12 09 07 PM" src="https://github.com/user-attachments/assets/feaa7a01-8649-49e7-bd73-f2aa8f6b572e">

- If the right distance is large (>= 120 units), or the robot is already turning (logic flag is True), it adjusts the desired heading (value) by 90 degrees.
  
- If value reaches 360, it is reset to 0.
  

Here is our Steering logic.

<img width="799" alt="Screenshot 2024-10-04 at 12 11 51 PM" src="https://github.com/user-attachments/assets/34329e69-7704-41e5-a68e-8e2c9572d7b3">

- If the current heading is not within a certain range of the desired heading, the robot adjusts its turn.
  
- The servo_pulsewidth for GPIO 18 controls the motor's speed for forward movement.
  
- pi.set_servo_pulsewidth(13, 1570) is set to control steering based on the difference between the current and desired heading.
  

Lastly we have the straight movement case.

<img width="542" alt="Screenshot 2024-10-04 at 12 16 36 PM" src="https://github.com/user-attachments/assets/15c9bd78-5791-411c-bc24-f054bd11896c">

- If the robot is not turning, it moves forward, and the PID controller is used to ensure the robot stays on course.
  
- Servo Control: The pid function is called to calculate the pulse width for steering correction.




### Future improvements

# Acknowledgement to our Mentor Sahil Gajera Sir


































