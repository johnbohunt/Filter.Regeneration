# Filter.Regeneration  
Liquid Argon Filter Regeneration Process  
[Instructions](https://github.com/johnbohunt/Filter.Regeneration/tree/main/John#instructions)  
### Overview of Steps:  
1. Evacuate the Vessel
2. Run the Heater Tapes
3. Turbo Evacuate the System and Prep the RGA  
4. Attach the Argon/Hydrogen Tanks and Vents
5. Regenerate the Filters  
  
## Warnings  
### Evacuating the Vessel
The "bleed in valve" is a percision valve should be handled very delicately and will need to be turned several times to open and close it all the way  
When the screw is all the way at the bottom the valve is CLOSED  
When the screw is at the top the valve is all the way OPEN  
Ensure all valves are closed when starting the pump with the exception of those outlined  
Avoid opening the system to outside pressure. Carefully check and double check when you are opening up valves to evacuate the vessel  
### Running the Heater Tape   
When attaching the tape, the tape should not be overlapping at any point  
The thermocouple regulator must be installed inbetween the heater tape and the steel  
The temperature can be set on the current regulator. The limit should be no higher than 225 C  
Ventilate the fumes that come off of the heater tape.  
### Turbo Evactuating System  
The turbo runs at very high rpm. If the system were to suddenly be exposed to high pressure (atmosphere) or be shaken there is a risk that the vacuum could fail catastrophically (blow up)  
Take special care not to disturb the vacuum too much when the turbo is on and be extra careful not to accidentally open a valve that you shouldn’t  
When in doubt, turn the turbo off, wait till the blades spin all the way down, then perform whatever task you need to do  
You NEVER want to operate the Ion Gauge if the pressure in the system is above 5 mTorr  
The ion gauge SHOULD NOT be left on for long periods of time (e.g. > 1 hour) as it will destroy the gauge
The goal is to run the turbo until the system achieves at least 10-5 torr  
  
- 9.0 10-5 torr is fine  
- 2.0 10-5 torr is better  
- 10-6 torr is best 

This can take up to 6 hours if the system hasn’t been pumped down for a while.  
It is ok to leave the system unattended while it pumps  
Be sure to turn the ion gauge off  
Press the menu button  
Use the arrows to select “IG off”  
Press enter  
### Attach Ar/H Tanks and Vents  
**IMPORTANT: THE Ar/H BOTTLE MUST BE ATTACHED TO EITHER THE WALL, THE BOTTLE CART, OR SOME OTHER STURDY STRUCTURE TO PREVENT THE BOTTLE FROM FALLING OVER. NEVER USE A BOTTLE UNLESS IT IS ANCHORED!!!**  
The threads on this adapter to the bottle are “left handed” threads. This means that you rotate counterclockwise to tighten and clockwise to loosen (opposite of normal)  
Be Careful not to strip the threads, brass can deform very easily  
These hoses are VCR ¼ inch hoses and need VCR ¼ inch gaskets (small metal disks) at the joints and to be tightened very well.  
You will not want to leave the system closed for long (> 30 mins) with the heater tapes on and the system isolated like this  
Only turn on the RGA if the pressure reads < 10-4 torr on the ion gauge  
### Starting the Regeneration Process
When starting the regeneration process, you will want to be sure the valve which allows the Ar/H to flow into the system to be open  
This pressure should be below 700 torr  
Pressure near the filter between 400 - 700 Torr (500 torr is ideal)
Pressure near the turbo pump below 10-4 Torr (somewhere around 10-5 Torr is ideal)
The Ar/H flow rate between 10 and 30 CFH (20 - 25 CFH is ideal)
The goal is to get the water level to ~10-6
Oxygen should stay below 10-6
### Steps to end the run
Shut off the Ar/H (close the regulator)  
Close the Ar/H bottle  
Close the rig to the outside world  
stop run and turn off filament   
isolate the RGA from the system  
turn off the heater tapes (unplug them)  
Open the Ar/H (open the regulator)  
Letting the pressure in the system pump out  
Turn off the ion gauge  
Shut off the system   
Turn off the Motor pump  
Turn off the RGA  
Shut off the Pumping Station  
  
  ---
## Instructions  
### Evacuating the Vessel  
There are two vacuum pumps we use to evacuate the system  

- Turbo Pump  
 <img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4810.png?raw=true" width=400>   
  
- Roughing Pump  
![Roughing Pump](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Roughing%20pump.jpg?raw=true)

These two pumps shouldn't be used on the same volume at the same time, i.e. we want to avoid the two pumps pulling opposite ways on the same section of pipe. Our current system runs the pumps inline, with the roughing pump extracting the "exhaust" of the turbo pump when the turbo is running. This is fine since the two pumps aren't acting against each other on the same volume. However, if both pumps are running and V5 and V6 on the valve diagram are both open, they WILL be pulling against each other, which will heat the system and risk damaging the pumps. This is the sort of thing we want to avoid.  
_!add diagram for clarity_  
Connect the Filter system to the roughing pump if not connected  
Should already be connected as shown in photo  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4814.png?raw=true" width=400>  
At the time of writing, they can be connected via Kwik Flange (KF) 25 hose _!verify_    
Close the valve nearest the roughing pump to isolate the roughing pump from everything else  
Make sure any other systems hooked up are closed off as well (e.g. the selenium evaporator needs to be closed off here)  
The valve labeled SV1 (refer to valve diagram below) is a precision valve and should be handled VERY DELICATELY  
![Valve Diagram](https://github.com/johnbohunt/Filter.Regeneration/blob/main/Alfredo/Images/Diagram.png?raw=true)  
Make sure this valve is also closed before pumping  
You will have to turn this valve quite a few times to close it all the way  
Make sure that “023 Motor Pump” is set to the “off” configuration.  
Make sure that the blade speed reads at “0” Hz  
Begin with every non specified valve on the filter rig in the CLOSED position  
Turn on the roughing pump _!specify procedure_  
Note, You DO NOT want to accidentally open the system to the outside atmosphere!!!! Please check and double check what you are about to do at these steps!  
Slowly open up valves in order of nearest to furthest from roughing pump, waiting for the system pressure to drop to 2-10 torr.

---
### Run the Heater Tape  
#### Time to complete 6 - 24 hours depending on how long its been since the last time this was done and the state of the filters  
The heater tapes are the plastic looking cords which are wrapped around the filters to provide heat to them and allow us to regenerate the filters  
![Heater Tape](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/heater%20tape.jpg?raw=true)  

They are controlled through two current regulators  
- One with a knob attached to the heater tape itself...  
![Current Regulator](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/current%20regulator.jpg?raw=true)  
- ...and one with a screen that actually plugs in to the oulet    
![Current Regulator 2: Electric Boogaloo](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/current%20regulator%20with%20thermocouple.jpg?raw=true)  

__Two important checks:__ These are most important when first setting up the heater tape  
1. Do NOT plug in Thermocouple regulators until these checks are performed, as temperature immediately starts to rise  
2. The cords need to be firmly attached to the steel tubes with little to no air gaps and CAN NOT be touching each other or be touching themselves in any spot 

The Thermocouple (thing that measures the temperature) needs to be installed between the heater tape and the steel  
![Tape Thermocouple](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/thermocouple%20cable%202.jpg?raw=true)  
There should be some form of insulation covering the tape. Currently, we are using a hard material that is wrapped in a one-sided reflective foil, but fiberglass and aluminum foil have been used in the past.  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4893.JPG?raw=true" width=400>   
__Make sure to ventilate the top of the filter.__ When the tape gets hot, some coating or adhesive it has burns off and forms smoke. In the future, we'd like this to go away, but for now, proper ventilation helps a lot.  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4895.JPG?raw=true" width=400>  
Plug both cables from the current regulators with the thermocouples into the power strip on the filter skid. We currently have this set up so the regulators plug into a seperate power strip which we can use to switch them on and off to more easily control the power. Otherwise, the tape will start heating as soon as it's plugged in.  
![Regulator Cable](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/current%20regulator%20cables.jpg?raw=true)  
If everything is setup, the screens on the current regulators will look like the ones shown here  
![Regulator Screens Powered On](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/current%20regulator%20screens.jpg?raw=true)  

The number here shows the current temperature as read by the thermocouple  
- If this tiny little red dot is illuminated, it means the current regulator is allowing current to flow to increase the temperature  

The system will automatically shut off when the temperature goes over the preset limit    
- The system will turn on again when the temperature goes below the preset limit too  

To change the temperature you want to target, press the “SET” button until a number appears  
- Then use the arrows to adjust the temperature to whatever value you want  

Note: There may only be one heater tape in use, so there may only be one regulator.  
We are currently using 180C as the set point for the tape. This is needed for the copper to regenerate.   

Once the desired temperature is set, simply leave the device alone and it will return to operations mode (this takes a while)  
The pressure in the system will slowly rise (as is expected when the gas+water+oxygen gets hotter)
Now we simply wait for some prescribed period of time  
- 6 hours is likely the minimum   
- 12+ hours will be needed if the system has been used / open to the air  

The system can be left “unattended” as long as you post on the group SLACK account in the “general” category letting people know that this is running and the heater tapes are on  
__No one should touch these heater tapes since they can get quite hot__  

---
### Turbo Evacuate the System  
#### Time to Complete: 1-4 Hours  
```
Since the this step and the next step will be where we actually start regenerating the filters,  
we will want to move the system to the location where it can vent the Argon/Hydrogen mixture out of the building  
We will move the system before turning on the turbo pump  
and the system SHOULD NOT BE MOVED WHEN THE TURBO PUMP IS OPERATING  
The first step is to unplug the heater tapes (this is how you turn them off)  
Then close the valve to the roughing pump  
Turn off the roughing pump  
Press and hold the red button on the roughing pump  
Disconnect the KF 25 hose from the roughing pump  
Note: You will hear a sound as the vacuum is broken in the hose  
Now move the purification skid to wherever you will be doing the regeneration  
Near the vent tubes in the lab is preferred  
```
_!Does the system still need to be disconnected and moved? It's set up in a place where it can ventilate currently_  
Ensure the system is below 20 mtorr before turning on the Turbo pump. The blades are delicate and will be damaged if operated outside of a near vaccum.    
The Turbo Pump is controlled by an independent voltage source. Flip the switch to turn on the pump.  
You should hear a “whirring” sound as the blades spin up to 1500 Hz and takes ~3 mins to come all the way up to speed  
Note: There are now blades spinning around 1500 times per second!  
If the system were to suddenly be exposed to high pressure (atmosphere) or be shooken there is a risk that the vacuum could fail catastrophically (blow up)  
Take special care not to disturb the vacuum too much when the turbo is on and be extra careful not to accidentally open a valve that you shouldn’t  
When in doubt, turn the turbo off, wait till the blades spin all the way down, then perform whatever task you need to do  
Once the vacuum gauge nearest the turbo reads ~3 milliTorr (mTorr) you have reached the limit of that gauge’s sensitivity  
To monitor further you will need to use the ion gauge (IG) which is mounted on top of the turbo station   
#### Using the Ion Gauge  
Note: You NEVER want to operate the Ion Gauge if the pressure in the system is above 5 mTorr  
The ion gauge SHOULD NOT be left on for long periods of time (e.g. > 1 hour) as it will destroy the gauge  
To turn on the ion gauge press the “menu” button  
![Ion Gauge](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/ion%20gauge%201.jpg?raw=true)  
Select the “IG On” from the menu and press “enter”  
![Turning On the Ion Gauge](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/ion%20gauge%202.jpg?raw=true)  
After a brief period of “warming up” the gauge should turn on and display the pressure  
![Ion Gauge Displays the Pressure Dutifully](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/ion%20gauge%203.jpg?raw=true)  
The goal is to run the turbo until the system achieves at least 10-5 torr  
Note:  
- 9.0 10-5 torr is fine  
- 2.0 10-5 torr is better  
- 10-6 torr is best  

This can take up to 6 hours if the system hasn’t been pumped down for a while.   
It is ok to leave the system unattended while it pumps  
__Be sure to turn the ion gauge off if you leave it unattended__  
- Press the menu button  
- Use the arrows to select “IG off”  
- Press enter  

---
### Attach Ar/H Tanks and Vents
#### Time to complete < 1 hour
The gas flow regulator (shown below) should be attached to the Argon/Hydrogen (Ar/H) bottle  
![Well Behaved Gas Flow Regulator](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/gas%20flow%20regulator.jpg?raw=true)![Attached Thusly](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/gas%20flow%20regulator%20and%20arh%20bottle%20are%20best%20friends.jpg?raw=true)   
__IMPORTANT: THE Ar/H BOTTLE MUST BE ATTACHED TO EITHER THE WALL, THE BOTTLE CART, OR SOME OTHER STURDY STRUCTURE TO PREVENT THE BOTTLE FROM FALLING OVER. NEVER USE A BOTTLE UNLESS IT IS ANCHORED!!!__  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4819.png?raw=true" width=400>  
There is an adapter which allows the connection between the two and needs to be installed prior to attaching (if it is not already there)
- Note: The threads on this adapter to the bottle are “left handed” threads. This means that you rotate counterclockwise to tighten and clockwise to loosen (opposite of normal)  

Be Careful not to strip the threads, brass can deform very easily  
The Ar/H hose connects to the port shown in the picture which is closest to the Copper filters  
Note: These hoses are VCR ¼ inch hoses and need VCR ¼ inch gaskets (small metal disks) at the joints and to be tightened very well.  
The other end should be securely fastened to the exhaust vent  
This is typically done with a combination of foam/tape/strain relief for the hose  

Now all that is needed is to connect the Residual Gas Analyzer (RGA) to the Windows computer station  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4816.png?raw=true" width=400>  
The RGA is connected via a USB cable coming out of the back of the RGA  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4824.png?raw=true" width=400><img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4825.png?raw=true" width=400>  
The computer is very small. The power button is on the right side  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4807.png?raw=true" width=400>  
The username and password should be attached to the monitor  
_!Can I put a photo of username and password? Is that a security issue?_   

---
### Regenerating the filters
#### Time to complete ≅ many hours
With all this done and the system connected you should be ready to start the regeneration process.  
#### Checklist of things  
The system has had time to “bake out” with the heater tapes running and the larger roughing pump attached  
The entire system has had time to be evacuated using the turbo pump and you were able to achieve ~10-5 Torr  
The Ar/H tanks and vent to exhaust is hooked up  
All the valves are open (excluding ones which would expose the system to the atmosphere) and the system has pumped down  
#### What should be the current state of the system?
Motor Pump: On  
Turbo Pump: On  
Heater Tapes: Off  
Ion Gauge: Off  
RGA: Off (but hooked up to the computer)  
Computer: On and logged in  
#### What should the pressures read?
Both the stinger gauges should be reading low mTorr levels   
Numbers need to be established based on more experience  
Ion Gauge for the full system should read close to 10-5 Torr  
[Using the Ion Gauge](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/README.md#using-the-ion-gauge)    
You will want to close the “bleed in valve” which separates the turbo pump from the filters (this should cause the pressure to drop very quickly)  
Next you will want to plug in the heater tapes for the filter material  
You will not want to leave the system closed for long (> 30 mins) with the heater tapes on and the system isolated like this...so we will be moving fast through the next steps!  
You will want to monitor the pressure gauge near the filters throughout the process  
Now you will want to prepare the Residual Gas Analyzer (RGA) system  
The RGA is very delicate. Only turn this on if the pressure reads < 10-4 torr on the ion gauge  
Turn on the RGA using the switch on the back  
<img src="https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/IMG_4808.png?raw=true" width=400>    
Open the application by clicking on the highlighted icon “RGA”  
_!Photo of RGA icon_  
Click the button at the top of the screen (shown to the left)  
![COM Icon](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/RGA%20COM%20icon.png?raw=true)   
A window will pop up (bottom left).  
Select the connector with the ID text and hit “connect”  
![Connecting the RGA](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Getting%20the%20RGA%20connected%20.png?raw=true)    
From the “Mode” menu, select “P vs. T” graph   
![PvT Graph](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/rga%20pvt.png?raw=true)  
This is pressure versus time  
__Double check to ensure the pressure is below 10^-4 torr. This next step is where we can damage the RGA if the pressure is too high.__  
Now you will want to turn on the filament by clicking the button shown  
![RGA Filament icon](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/RGA%20Filament%20icon.png?raw=true)  
A message window will appear telling you this will take a few seconds and then disappear   
  
Then select the “Scan Parameters” button  
If you cannot click it, simply select “Scan Parameters” from the “Scan” menu  
This will bring up a menu where you can add each channel and specify what you want to measure  
![Scan Parameters](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/scan%20perameters%201.png?raw=true)  

Argon, Water, and Oxygen are good places to start  
![Entered Parameters](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/scan%20parameters%202.png?raw=true)  
You can always type the element or specify the atomic mass  

Be sure to check each channel as you add them  
Now you can start the scan by pressing the “Go” button at the top  
![Go Button](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Go%20button%20icon.png?raw=true)  
The plot should start to populate with the measurement of these elements  
We will be monitoring this plot  
You can change the range of the “x” and “y” axis by going to the “Graph” menu and selecting “x-axis…” or “y-axis” and typing in the range you want  
  
You will now want to open the Argon/Hydrogen bottle and build pressure at the regulator  
You will turn the large valve on the bottle  
Make sure the regulator valve (gold valve on the regulator) is closed  
This valve is closed if it is unscrewed all the way out  
![Regulator Valves and How They Work](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Regulator%20valves%20and%20how%20they%20work.png?raw=true)  
  
Once opened, you should see pressure built in the regulator  
![Pressure Reg Gauge](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Pressure%20regulator%20gauge%20shows%20pressure%20in%20the%20regulator%20.png?raw=true)  
Note, you will want to be sure the valve which allows the Ar/H to flow into the system to be open (V1 on the diagram)  

Now you will want to allow the Ar/H to flow by rotating the valve on the regulator clockwise   
![Regulator Valve Opening](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Regulator%20valves%20and%20how%20it%20opens%20.png?raw=true)  
The goal is to get a flow rate between 10 and 30 Cubic Feet per Hour (CFH)  
![Flow Rate Gauge](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/Flow%20rate%20gauge%20shows%20the%20flow%20rate.png?raw=true)  
Once the process has started you will want to closely monitor the pressure gauge closest to the filters  
This pressure should be below 700 torr  
Once the flow has started, you will open the bleed in valve which allows the Ar/H to vent to the outside world  
The vent will go up the chimney out of the lab  
Initially you will only want to open this valve somewhere between ¼ and ⅓ of fully open  
Please be careful when opening this valve  
Be checking the pressure on the gauge nearest the filters  
Once stable flow is established, we will want to flow in a small amount of Ar/H mixture which has passed through the filters and monitor the Water and Oxygen content  
You can SLOWLY OPEN the bleed in valve monitoring the pressure on the ion gauge  
__THE PRESSURE ON THE ION GAUGE SHOULD STAY ~10-5 TORR__  
___NEVER GO ABOVE 10-4 TORR___  
#### A Balancing Act
What you will do now is a balancing act to get the flow rate of Ar/H into the system well matched to the venting valve and the flow into the RGA   
This typically takes 1 hour of tweaking, letting things run, and tweaking again  
#### What are we aiming for
##### Pressure near the filter between 400 - 700 Torr (500 torr is ideal)  
What do we do if this is out of spec?  
- If the pressure is too low, further close the vent valve and increase the flow rate  
- If the pressure is too high, open the vent valve and decrease the flow rate  
- If things go crazy, close the bottle valve!  

##### Pressure near the turbo pump below 10-4 Torr (somewhere around 10-5 Torr is ideal)  
What do we do if this is out of spec?  
- If the pressure is too low, carefully and slowly open the bleed in valve and/or increase the flow rate  
- If the pressure is too high, quickly close the bleed in valve and turn off the ion gauge  

##### The Ar/H flow rate between 10 and 30 CFH (20 - 25 CFH is ideal)  
What do we do if this is out of spec?  
- If the flow rate is too low, open the valve (turn clockwise)  
- If the flow rate is too high, close the valve (turn counterclockwise)  
- If things get really crazy, close the bottle valve  
- If the bottle runs out...see change over slides later (to be developed)  

##### Monitoring the Water, Oxygen, and Argon in the RGA  
What you should see on the RGA:  
![RGA Looks Like](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/rga%20regen%202.png?raw=true)  

##### Temperature
_!We're expecting a temperature spike when adding the Hydrogen/Argon mixture. It's likely this will need to be balanced as well._  
The temperature needs to be at least 175 C and shouldn't exceed 225 C. Note that spikes as high as 300 C are okay as long as the temperature is maintained below 225 C. Refer to the Copper Catalyst reduction guidline [here](https://github.com/johnbohunt/Filter.Regeneration/blob/8888a869bf07075ab53d143642b467c4da9cf445/Alfredo/Filter.Guidelines/Reduction%20Guidelines%20for%20Copper%20Catalysts.pdf) for more details.  
#### Waiting Game  
Now we will let the filter regeneration happen!  
We will want to monitor this closely over the first 2-3 hours and then less frequently later  
Monitoring closely the pressure everywhere and the flow rate on the bottle  
The regeneration will likely take 10+ hours (depending on how bad the filters are contaminated)  
The system can be left unattended for extended periods of time as long as the Ar/H bottle is relatively full  
If the bottle runs out, you will have to switch the bottle and we should develop the procedure to do this.  
The goal is to get the water level to ~10-6  
Oxygen should stay below 10-6  
#### What the end result starts to look like
![Completed Regen](https://github.com/johnbohunt/Filter.Regeneration/blob/main/John/images/rga%20regen%203.png?raw=true)    
This regeneration was allowed to run for almost 24 hours from the start and we can start to see very low levels of water and oxygen!  
#### Steps to end the run
1. Shut off the Ar/H (close the regulator)  
2. Close the Ar/H bottle  
3. Close the rig to the outside world  
4. Stop run and turn off filament  
5. Isolate the RGA from the system  
6. Turn off the heater tapes (unplug them)  
7. Open the Ar/H (open the regulator)  
8. Letting the pressure in the system pump out  
9. Turn off the ion gauge  
10. Shut off the system   
11. Turn off the Motor pump  
12. Turn off the RGA  
13. Shut off the Pumping Station  
