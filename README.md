# MediatorPlant
Plant Project mediator pattern.

<img src="https://github.com/DrJohn17/MediatorPlant/blob/main/plant.jpg" width="250" />

 The idea of this project was to make use of the robotic arm and a sensor to know when a plant needs water, and then let the robot give the water. And to automate this with simple services that can be executed from cpee.org.

 For this project, an orangepi was used. The sensor was made ready by soldering the pins, connecting it correctly and a test program to check for output and to calibrate the humidity sensitivity to a reasonable amount so that the plant can get water at appropriate times. The sensitivity in this case, with an AZ delivery humidity sensor, is adjusted with a screw on the sensor itself.
 
<img src="https://github.com/DrJohn17/MediatorPlant/blob/main/bodenfeuchtesensor-pflanzen-feuchte-messgerat-mit-korrosionsbestandiger-sonde-kompatibel-mit-arduino-und-raspberry-pi-331653.jpg" width="250" />

 The special bottle cap holds an amount of water of 12 gramms or 12mL.
It is generally the case that between 0% and 20% of soil moisture (≈ 57 mL water for this plant) corresponds to a “dry” condition where the plant should be watered.
Humidity from 20% to 40% (≈ 114 mL) is seen as optimal for most houseplants.
The current calibration of the sensor is set to return "dry" too when the earth is expected to be at 20% moisture.

 The plant receives about 12 mL per watering motion of the arm controlable with the "water_amount" vaiable in CPEE, so regular monitoring to see if the current settings fit the plant, especially if it is a different plant, effect must be considered this calibration ensures the sensor responds accurately to real plant needs, avoiding both under- and overwatering.

The bottle should not be too full as the weight shifting could make it move a bit in the robot grip, higher friction could be needed if problems occur.

With the estimated amout of water of under 57mL for the current estiamted earth amount the currect setting of water_amount of 2 seems reasonable with 24mL per activation. This could also be increased to 3 or 4 if the goal is to water it less regularly.

<img src="https://github.com/DrJohn17/MediatorPlant/blob/main/sensor.jpg" width="250" />  <img src="https://github.com/DrJohn17/MediatorPlant/blob/main/screw.jpg" width="250" />


  The test file is available under: "test_gpio_input.py." It simply prints the current state, which is called dry or wet, frequently helping to detect changes quickly.

 To hold the plant next to the table and to ensure it is always in the same position, an individualised holder was designed and 3d printed. It can be seen in the file "Plantholder2.stl". This was performed using Onshape.
 
 <img width="350" height="300" alt="grafik" src="https://github.com/user-attachments/assets/66c4ef1e-2bdc-4d81-92c0-947b41ae0b04" />
 
 Next, the real program was written on the orangepi (see: "soil-sensor.py") and later including Bottle, to connect the sensor and orangepi to the CPEE process engine, allowing communication and access to the current status with "https-get://lehre.bpm.in.tum.de/ports/19234/".

 In CPEE, a process was modelled to represent the whole process divided into smaller steps, calling the respective services. This initial process can be accessed in the "PlantW.xml" file. 
 
 <img width="300" height="400" alt="Screenshot 2025-07-15 at 12-11-37 PlantW (53853)" src="https://github.com/user-attachments/assets/91a9f896-d2c6-465d-9d9c-7250d8fa1e8b" />

 So it is a loop that waits for the specified time (in minutes) using the "powernap.php" function. Half a day, for example (720 minutes), sounds reasonable, but it can be personalised easily if needed. To modify this interval a change of its value in minutes is needed.
 
 <img width="937" height="171" alt="grafik" src="https://github.com/user-attachments/assets/00229ada-14b6-47e7-b6b6-4dbf50959e22" />
 
 Then the sensor is called to get the current humidity state at the plant, in case this is dry we go and call the robot to perform a function "BurkatUlrichPlant.urp" that will take a specified bottle infornt of it (the one in the middle in this case) turn it using a special cap that holds a specific amout of liquid and then turns it to give the water (in this case) to the plant and then returns the botle to its place in the same position to ensure the program can be repeated multiple times without a need of human intervention. To make it more customisable, this function includes a loop that holds the part where we turn the bottle and give water. A variable "water_amount" is defined and sent to the robot as a put, with this the numeber of times the action is repeaded can be decided ensureing the plant can get enough water, a small number would lead to the arm activating more often the next loop instances, and big number would give too much water, leaving the status as "wet" for a longer time but also harming the plant probably. 

 Then, in the spirit of simpler services, increasing modularity and making changes easier, the robot arm code was adapted into smaller parts, each equivalent to an important part of the previous all-in-one file. The files for this version can be found in the "CpeeModel" folder as "PlantW2". 

<img width="350" height="560" alt="grafik" src="https://github.com/user-attachments/assets/df7294e7-4236-48bf-a4e7-3b02dd68bd5d" />

The "PlantW3" files, in the folder "mL input CPPE code", include one more step where a mL input in the CPEE data is possible. As estimated for this plant 57 mL of water in the earth still count as dry but as we water regularly I would recommend a value that is not higher that 57mL to ensure it does not get too much water at one time.

<img width="300" height="490" alt="grafik" src="https://github.com/user-attachments/assets/935fd7ee-ff25-4976-83f6-8673076a7bad" />


So the data objects look like the image below, and "water_ml" should be the only one changed. Representing the estimated amount, in milliliters, per watering session desired. It will be converted to a valid integer ("water_amount") in the new script to be used for the watering loop as "count".

<img width="428" height="183" alt="grafik" src="https://github.com/user-attachments/assets/67ee901f-bfee-44e0-9b82-02ebca179b9c" />

 In these last two CPEE programs with the different actions dispersed into different services, we start by getting the robot in position in front of the bottles, "b_base0.urp".   
Then we take the bottle in the middle, "b_bot1.urp".     
Next, we go to the base position for refilling the cap with water/ giving water with "b_mbase2.urp".
Then the actual watering motion "b_watering3.urp".
Then giving back the bottle from and back to the base position "b_zback4.urp".
And lastly, the end, "b_zend5.urp", returning to the initial position from its base position.
The loop here stays in CPEE, instead of running in the arm with a variable being sent to it, and we also use "water_amount" but in an easier, more robust way.

 Therefore, modification can be easier here, as, for example, a small program for the bottle chosen can be replaced to pick up a different bottle and go through the same process. Just changing the few steps in "b_bot1.urp" without risking damaging the other steps. Also, when debugging, it is easier to return the arm to the desired position without having to leave the remote control version and having to execute the code from the robot arm. This way, executing the relevant part of the CPEE process can fix the problem more conveniently. 

The whole procces in action can be seen in this video:
https://youtube.com/shorts/iOo_pSGZa18

