# MediatorPlant
Plant Project mediator pattern

 The Idea of this project was to make use of the robotic arm and a sensor to know when a plant needs water and then let the robot give the water. And to automate this with siple services that can be executed from the cpee.org.

 For this project an orangepi was used. The sensor made ready by soldering the pins, connecting it ocrrectly and a test programm to check for output and to callibrate the humitity sensitivity to a reasonable amount so that the plant can get water at apropiate times. The sensitivity in this case with an az delivery humidity sensor is adjusted with a screw on the sensor itself.

<img src="https://github.com/DrJohn17/MediatorPlant/blob/main/bodenfeuchtesensor-pflanzen-feuchte-messgerat-mit-korrosionsbestandiger-sonde-kompatibel-mit-arduino-und-raspberry-pi-331653.jpg" width="250" />

  The test file is awailable under:  xxxxxxxxxxxxxxxxxxxxx  it simply prints the current state called dry or wet frequently helping to detect changes fast.

 To hold the plant next to the table and to ensure it is always in the same position an individualized holder was designed and 3d printed, it can be seen in the file "Plantholder2.stl". This was performed using onshape.

 Next the real program was written on the orangepi (see: xxxxxxxxxxx) and later bottle, to connect the sensor and orangepi to the CPEE process engine, allowing communication and access to the current status with "https-get://lehre.bpm.in.tum.de/ports/19234/".

 In CPEE a process was modeled to represent the whole process divided into smaller steps calling the respective services. This initial proces can be accesed in the "PlantW(10).xml" file. 

 <img width="300" height="400" alt="Screenshot 2025-07-15 at 12-11-37 PlantW (53853)" src="https://github.com/user-attachments/assets/91a9f896-d2c6-465d-9d9c-7250d8fa1e8b" />


