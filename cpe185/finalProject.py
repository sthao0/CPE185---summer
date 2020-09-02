from sense_hat import SenseHat
import time
import sys 
from ISStreamer.Streamer import Streamer


#import math functions 
import numpy as np
from scipy.integrate import quad


sense = SenseHat()
sense.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 102, 255)
red = (255, 0, 0)
nothing = (0,0,0)
orange = (255, 153, 51)



def moon_animation_1():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    B, B, O, O, O, O, O, O,
    B, B, O, O, O, O, O, O,
    ]
    return logo
    
def moon_animation_2():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, B, B, O, O, O, O,
    O, O, B, B, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def moon_animation_3():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def moon_animation_4():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, B, B, O, O,
    O, O, O, O, B, B, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def moon_animation_5():
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, B, B,
    O, O, O, O, O, O, B, B,
    ]
    return logo

def sun_animation_1():
    Y = yellow
    O = nothing
    OR = orange
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    Y, OR, O, O, O, O, O, O,
    OR, Y, O, O, O, O, O, O,
    ]
    return logo
    
def sun_animation_2():
    Y = yellow
    O = nothing
    OR = orange
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, Y, OR, O, O, O, O,
    O, O, OR, Y, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def sun_animation_3():
    Y = yellow
    O = nothing
    OR = orange
    logo = [
    O, O, O, OR, OR, O, O, O,
    O, O, OR, OR, OR, OR, O, O,
    O, OR, OR, Y, Y, OR, OR, O,
    O, OR, OR, Y, Y, OR, OR, O,
    O, O, OR, OR, OR, OR, O, O,
    O, O, O, OR, OR, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def sun_animation_4():
    Y = yellow
    O = nothing
    logo = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    ]
    return logo

def sun_animation_5():
    Y = yellow
    O = nothing
    logo = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, O, O, O, O, O, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    ]
    return logo
    
def sun_animation_6():
    Y = yellow
    O = nothing
    logo = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, Y, O, O, O, O, Y, Y,
    ]
    return logo
    
def sun_animation_7():
    Y = yellow
    O = nothing
    logo = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, O, Y,
    Y, O, O, Y, Y, Y, O, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    Y, Y, O, O, O, O, Y, Y,
    ]
    return logo
images = [moon_animation_1, moon_animation_2, moon_animation_3, moon_animation_4, moon_animation_5, sun_animation_1
, sun_animation_2, sun_animation_3, sun_animation_4, sun_animation_5, sun_animation_6, sun_animation_7, sun_animation_6]
count = 0
for x in images:
    sense.set_pixels(images[count % len(images)]())
    time.sleep(.25)
    count += 1

number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hour_color = [208,79,210] # Pink
minute_color = [0,255,255] # Cyan
empty = [0,0,0] # Black

clock_image = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="ist_77LSNhp5y6IKw47yt-RzhpIwsHQnnfTc")
sense.clear()

#start the infinite loop of logging data real time 
try:
    while True:
        temp = sense.get_temperature()
        Ftemp = (temp * 1.8) + 32
        temp = round(Ftemp, 1)
        logger.log("Temperature in F:",temp) 

        tempHum = sense.get_temperature()
        FtempHum = (tempHum * 1.8) + 32
        tempHum = round(FtempHum, 1)
        logger.log("Temperature in F from Humidity:",tempHum)
 
        tempPress = sense.get_temperature()

        logger.log("Temperature in F from Pressure:",tempPress) 
    
        humidity = sense.get_humidity()  
        humidity = round(humidity, 1)  
        logger.log("Humidity:",humidity)  

        #get the sensehat to sense the pressure
        pressure = sense.get_pressure()
        logger.log("\nPressure: %s Millibars" , pressure)
        
        time.sleep(1)
        #make it so when you do crtl c you get out the the logging
except KeyboardInterrupt:
    pass

while True:
    #set imu configuration for x,y,z
    sense.set_imu_config(False, True, False)

    #get orientation in radians
    orientation_rad = sense.get_orientation_radians()
    print("\np: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))


    #get current orientation in degress
    orientation = sense.get_orientation_degrees()
    print("\np: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

    #get the gyroscope
    gyro_only = sense.get_gyroscope()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

    raw = sense.get_compass_raw()   #get the x,y,z magentometer data
    print("\nx: {x}, y: {y}, z: {z}".format(**raw))
        
    #get how far away it is from north in percentage
    north = sense.get_compass()
    print("North: %s" % north)
          # Take readings from all three sensors
    t = sense.get_temperature()
    h = sense.get_humidity()
    a = sense.get_orientation_radians()
    b = sense.get_compass()
    c = sense.get_orientation_degrees()
    d = sense.get_pressure()

    # Round the values to one decimal place
    t = round(t, 1)
    h = round(h, 1)
    d = round(d, 1)
   
  
    # Create the message
    # str() converts the value to a string so it can be concatenated
    message = "Temp: " + str(t) + " Humidity: " + str(h) + "Pressure" + str(d)
  
    if t > 18.3 and t < 26.7:
        bg = green
    else:
        bg = red

    # Display the scrolling message
    sense.show_message(message, scroll_speed=0.15, back_colour=bg)


    time.sleep(1)
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min

    # Map digits to the clock_image array
    pixel_offset = 0
    index = 0
    for index_loop in range(0, 4):
        for counter_loop in range(0, 4):
            if (hour >= 10):
                clock_image[index] = number[int(hour/10)*16+pixel_offset]
            clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
            clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
            clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4

    # Color the hours and minutes
    for index in range(0, 64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = hour_color
            else:
                clock_image[index] = minute_color
        else:
            clock_image[index] = empty

    # Display the time
    sense.low_light = True # Optional
    sense.set_pixels(clock_image)
    time.sleep(1)
    #from sense_hat import SenseHat

#Shawns wind speed

    start = time.time()
#states the list outside of the loop so it does not get reset 
    listX=[]
    listY=[]
    listZ=[]
    count=0
    while (count < 3): 
    

 

        raw = sense.get_accelerometer_raw()

 
#gets the raw accelerations in each direction 
        x = raw['x']

        y = raw['y']

        z = raw['z']

 

  
#round and convert the values from g's to m/s^2
        xR=round(x *9.8,1)

        yR=round(y*9.8,1)

        zR=round(z*9.8,1)

        numbX=float(xR)
#creates X value memory
        if(len(listX)==2):

            listX.insert(1,xR)
            y2y1=listX[0]-listX[1]

            m= y2y1/changeInTime  
            def f(x):
                return m*x**1 + y2y1
            
            i=quad(f,0,changeInTime)
            
            print(" windX: "+str(i[0]))
    
    
    #initial insert at list[0]
        listX.insert(0,xR)
    #size of the list
        listX=listX[:2] 

 

        numbY=float(yR)
    #creates y memory
        if(len(listY)==2):
            listY.insert(1,yR)
        #y2-y1/x2-x1=m
            y2y1=listY[0]-listY[1]
            m= y2y1/changeInTime  
            def f(x):
                return m*x**1 + y2y1 
            i=quad(f,0,changeInTime)            
            print(" windY: "+str(i[0]))
        listY.insert(0,yR)
        listY=listY[:2]
    
        numbZ=float(zR)
    #creates z memory 
        if(len(listZ)==2):
            listZ.insert(1,zR)
            y2y1=listZ[0]-listZ[1]
            m= y2y1/changeInTime
        #creates a linear function and then takes the integral
            def f(x):
                return m*x**1 + y2y1 
            i=quad(f,0,changeInTime)            
            print(" windZ: "+ str(i[0]))
    #initial insert of the list
        listZ.insert(0,zR)
    #size of the list 
        listZ=listZ[:2]
    #stop timer 
        end = time.time()
    #getting the chnage in ti,e
        changeInTime= end - start
    
        count=count+1
    #acceleration in X,Y,and Z
        print(" x: "+str(numbX) +" y: "+str(numbY) +" z: "+str(numbZ))
    
 
