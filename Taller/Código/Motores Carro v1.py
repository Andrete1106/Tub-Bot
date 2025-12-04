from machine import Pin, PWM
import time

# --------------------------
# Motor A (L298N #1)
# --------------------------
ena = PWM(Pin(25), freq=500)
in1 = Pin(12, Pin.OUT)
in2 = Pin(13, Pin.OUT)

# --------------------------
# Motor B (L298N #1)
# --------------------------
enb = PWM(Pin(26), freq=500)
in3 = Pin(14, Pin.OUT)
in4 = Pin(27, Pin.OUT)

# --------------------------
# Motor C (L298N #2)
# --------------------------
enc = PWM(Pin(33), freq=500)
in5 = Pin(32, Pin.OUT)
in6 = Pin(23, Pin.OUT)

# --------------------------
# Motor D (L298N #2)
# --------------------------
end = PWM(Pin(21), freq=500)
in7 = Pin(22, Pin.OUT)
in8 = Pin(19, Pin.OUT)

# --------------------------
# Funciones básicas
# --------------------------

def motors_forward(speed=700):
    print("4 motores avanzando...")

    # Motor A
    in1.value(0); in2.value(1); ena.duty(speed)
    # Motor B
    in3.value(0); in4.value(1); enb.duty(speed)
    # Motor C
    in5.value(1); in6.value(0); enc.duty(speed)
    # Motor D
    in7.value(1); in8.value(0); end.duty(speed)


def motors_backward(speed=700):
    print("4 motores retrocediendo...")

    # Motor A
    in1.value(1); in2.value(0); ena.duty(speed)
    # Motor B
    in3.value(1); in4.value(0); enb.duty(speed)
    # Motor C
    in5.value(0); in6.value(1); enc.duty(speed)
    # Motor D
    in7.value(0); in8.value(1); end.duty(speed)


def motors_stop():
    print("Deteniendo los 4 motores...")

    ena.duty(0); enb.duty(0); enc.duty(0); end.duty(0)

    in1.value(0); in2.value(0)
    in3.value(0); in4.value(0)
    in5.value(0); in6.value(0)
    in7.value(0); in8.value(0)

# --------------------------
# Prueba simple
# --------------------------

print("Prueba de 4 motores...")

motors_forward(700)
time.sleep(3)

motors_stop()
time.sleep(1)

motors_backward(700)
time.sleep(3)

motors_stop()
print("Fin de prueba.")