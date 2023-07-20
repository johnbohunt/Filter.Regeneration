################################################
#### Author: Ilker Parmaksiz                ####
#### Date  : July 19 2023                   ####
################################################

from serial.tools.list_ports import comports
from serial.tools import hexlify_codec
import sys
import serial as sr
from serial import Serial # import Serial Library
import numpy  # Import numpy
import re
import glob
import matplotlib.pyplot as plt #import matplotlib library


from datetime import datetime


file=open("TermalCouple_3_18_2022.csv","a+")

show=0
arduinoData = Serial(ask_for_port() , 9600, bytesize=8, timeout=2, stopbits=sr.STOPBITS_ONE) #Creating our serial object named arduinoData



## This will get the port of arduino from windows or linux.
def ask_for_port():
    """\
    Show a list of ports and ask the user for a choice. To make selection
    easier on systems with long device names, also allow the input of an
    index.
    """
    
    print("\n\033[1;31;47m ---  Currently available devices to readout:\033[0m \n")
    ports = []
    global index
    for n, (port, desc, hwid) in enumerate(sorted(comports()), 1):
        sys.stderr.write('    {:7}      {:20} {}\n'.format("index","Port","Device"))
        sys.stderr.write('--- {:2}      {:20} {}\n\n\n\n\n'.format(n, port, desc))
        ports.append(port)
    if(len(ports)==0):
       print("\n\033[1;31;47m --- There are no ports available ---\033[0m \n") 
    while True:
        pr = input('--- Enter port index: ')
        try:
            index = int(pr) - 1
            if not 0 <= index < len(ports):
                sys.stderr.write('--- Invalid index!\n')
                continue
            
        except ValueError:
           ask_for_port()
            
        port=ports[index]
        return port


while True: # While loop that loops forever
    try:
       #Check=arduinoData.readline(10).decode("ascii").split(" ")
       while (False): #Wait here until there is data
          if(show==0):
             print("\n\033[1;31;40m Waiting to Receive Data from Arduino....\033[0m \n")
             print("\033[1;31;47m Press CTRL+C to CANCEL waiting\033[0m  \n")
             show=1
          pass
    except KeyboardInterrupt:
       file.close()
       break

    now= datetime.now()
    DataFromArduino=arduinoData.readline().decode("ascii")
    Splited=DataFromArduino.split(" ")

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    arduinoString = dt_string +" "+ str(DataFromArduino) #read the line of text from the serial port
    if(len(Splited)>=2 and DataFromArduino!=None):
      file.write(arduinoString)
      file.write("\n")
      file.flush()
      print (arduinoString)
 
