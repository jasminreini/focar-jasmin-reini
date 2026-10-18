from machine import Pin, PWM 
from time import sleep

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

m1.value(1)
m2.value(1)

# Tehot 50%
e1.duty_u16(32767) # Nopeus 50%
e2.duty_u16(32767)
