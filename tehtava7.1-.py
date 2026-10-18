from machine import Pin, PWM 
from time import sleep

#Tehot: 16384-25%| 32767-50%| 49515-75%| 65535-100%

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

#funktiot
def eteen():
    e1.duty_u16(32767) # Nopeus 50%
    e2.duty_u16(32767) # Nopeus 50%
    

def taakse():
    # nopeus 50% - 100%
    e1.duty_u16(32767)
    e2.duty_u16(32767)

def vasen(): 
    e1.duty_u16(65535) # Nopeus100% 
    e2.duty_u16(32767) # Nopeus 50%

def oikea():
    e1.duty_u16(32767) # Nopeus 50%
    e2.duty_u16(65535) # Nopeus 100%

def suuntaE():
    m1.value(1) # Eteenpäin
    m2.value(1) # Eteenpäin

def suuntaT():
    m1.value(0) #Taaksepäin
    m2.value(0) # Taaksepäin


# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

sleep(5)

# Liikumis suunta eteenpäin
m1.value(1)
m2.value(1)

# Tehot 50%
e1.duty_u16(32767) # Nopeus 50%
e2.duty_u16(32767) # Nopeus 50%

# Sekunnin kestävä tauko
sleep(3)

# Liikkumis suunta eteenpäin
m1.value(1)
m2.value(1)

# Kääntyminen
e1.duty_u16(16384) # Nopeus 25%
e2.duty_u16(49515) # Nopeus 75%

# Sekunnin kestävä tauko
sleep(1)

# Liikkumis suunta taaksepäin
m1.value(0)
m2.value(0)

e2.duty_u16(32767) # Nopeus 25%
e1.duty_u16(49515) # Nopeus 75%

# 1.5 Sekunnin kestävä tauko
sleep(1.5)

# Liikumis suunta eteenpäin
m1.value(1)
m2.value(1)

# Tehot 50%
e2.duty_u16(65535) # Nopeus 100%
e1.duty_u16(32767) # Nopeus 50%

# 1.55 sekunnin tauko
sleep (1.55)

# Liikumis suunta eteenpäin
m1.value(1)
m2.value(1)

# Tehot 50%
e1.duty_u16(32767) # Nopeus 50%
e2.duty_u16(32767) # Nopeus 50%

# 2 Sekunnin tauko
sleep(2)

# nopeus 0%
e1.duty_u16(0)
e2.duty_u16(0)

# Wait 1 second for motors to stop / Odota yksi sekunti moottoreiden pysähtymistä
sleep(1)
