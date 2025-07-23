# MediatorPlant
Plant Project mediator pattern

'''''!!!!!!!!!!to do __ video showing the movement. ,  water amount in ml with calculation , earth amount relative humitity setting the sensor to an expected dry specifically adapted for this plant. make nicer folders , names for git files  bottle being half full or less to not move in the grip
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 The Idea of this project was to make use of the robotic arm and a sensor to know when a plant needs water and then let the robot give the water. And to automate this with siple services that can be executed from the cpee.org.

 For this project an orangepi was used. The sensor made ready by soldering the pins, connecting it ocrrectly and a test programm to check for output and to callibrate the humitity sensitivity to a reasonable amount so that the plant can get water at apropiate times. The sensitivity in this case with an az delivery humidity sensor is adjusted with a screw on the sensor itself.
 
<img src="https://github.com/DrJohn17/MediatorPlant/blob/main/bodenfeuchtesensor-pflanzen-feuchte-messgerat-mit-korrosionsbestandiger-sonde-kompatibel-mit-arduino-und-raspberry-pi-331653.jpg" width="250" />

  The test file is awailable under: "test_gpio_input.py" it simply prints the current state called dry or wet frequently helping to detect changes fast.

 To hold the plant next to the table and to ensure it is always in the same position an individualized holder was designed and 3d printed, it can be seen in the file "Plantholder2.stl". This was performed using onshape.
 <img width="350" height="300" alt="grafik" src="https://github.com/user-attachments/assets/66c4ef1e-2bdc-4d81-92c0-947b41ae0b04" />


 Next the real program was written on the orangepi (see: "soil-sensor.py") and later including bottle, to connect the sensor and orangepi to the CPEE process engine, allowing communication and access to the current status with "https-get://lehre.bpm.in.tum.de/ports/19234/".

 In CPEE a process was modeled to represent the whole process divided into smaller steps calling the respective services. This initial proces can be accesed in the "PlantW(10).xml" file. 

 <img width="300" height="400" alt="Screenshot 2025-07-15 at 12-11-37 PlantW (53853)" src="https://github.com/user-attachments/assets/91a9f896-d2c6-465d-9d9c-7250d8fa1e8b" />

 so it is a loop that waits for the specified time (in minutes) using the "powernap.php" function, half a day for example (720 minutes) sounds reasonable but it can be personalised easily if needed. Then the sensor is called to get the current humidity state at the plant, in case this is dry we go and call the robot to perform a function "BurkatUlrichPlant.urp" that will take a specified bottle infornt of it (the one in the middle in this case) turn it using a special cap that holds a specific amout of liquid and then turns it  to give the water (in this case) to the plant and then returns the botle to its place in the same position to ensure the program can be repeated multiple times without a need of human intervention. To make it more customisable, this function includes a loop that holds the part were we turn the bottle and give water. A variable "water_amount" is defined and sent to the robot as a put, with this the numeber of times the action is repeaded can be decided ensureing the plant can get enough water, a small number would lead to the arm activating more often the next loop instances, and big number would give too much water, leaving the status as wet for the next days but also harming the plant probably. 

 Then in the spirit of simpler services, increasing modularity and making changes easier the robot arm code was adapted into smaller parts each eaquivalent to an important part of the previous all-in-one file. The files for this version can be found in the "CpeeModel" folder as "PlantW2". 

<img width="289" height="422" alt="grafik" src="https://github.com/user-attachments/assets/8169890b-fea5-4615-a0ff-21dd562c5140" />

<img width="760" height="1127" alt="grafik" src="https://github.com/user-attachments/assets/df7294e7-4236-48bf-a4e7-3b02dd68bd5d" />
<img width="350" height="560" alt="grafik" src="https://github.com/user-attachments/assets/df7294e7-4236-48bf-a4e7-3b02dd68bd5d" />


 In this split up setting we start by getting the robot in position infornt of the bottles, "b_base0.urp".
 Then we take the bottle in the middle, "b_bot1.urp".     
 next we go to the base position for refilling the cap with water/ giving water with "b_mbase2.urp".
 then the actual watering motion "b_watering3.urp".
 then giving back the bottle from and back to the base posittion "b_zback4.urp".
 and lastly the end, "b_zend5.urp" returning to the initial position from its base position.
The loop here instead of being a variable going to the arm stays in CPEE, and we also use "water_amount" but in an easier more robust way.

 Therefore here a modification can be easier as for example a small program for the bottle chosen can be replaced to pick up a different bottle and do the same proccess. Just changing the few steps in "b_bot1.urp" whithout risking to damage the other steps. Also when debugging it is easier to return the arm to the wished position without having to leave the remote control version and having to execute the code from the robot arm. This way executing the relevant part from the CPEE process can fix the problem in a more convenient way.  


