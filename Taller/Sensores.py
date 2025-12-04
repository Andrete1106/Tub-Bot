from machine import Pin, PWM
from machine import Pin, time_pulse_us
import time


# === Pines del Sensor 1 ===
TRIG1 = Pin(16, Pin.OUT)
ECHO1 = Pin(34, Pin.IN)

# === Pines del Sensor 2 ===
TRIG2 = Pin(17, Pin.OUT)
ECHO2 = Pin(35, Pin.IN)

# Pin donde conectar la señal del servo
servo = PWM(Pin(4), freq=50)

# Función genérica para medir distancia en un sensor
def medir_distancia(TRIG, ECHO):
    # Asegurar TRIG en LOW
    TRIG.value(0)
    time.sleep_us(5)

    # Enviar pulso
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # Medir tiempo del pulso en ECHO
    duracion = time_pulse_us(ECHO, 1, 30000)

    if duracion < 0:
        return None

    distancia = (duracion / 2) * 0.343
    return distancia
# Conversión de grados a duty_us (microsegundos)
def set_angle(angle):
    # MG90S normalmente usa 500-2400 us
    min_us = 500
    max_us = 2400
    us = min_us + (angle / 180) * (max_us - min_us)
    servo.duty_u16(int(us * 65535 / 20000))  # 20 ms period
    time.sleep(0.02)
set_angle(0)
print("servo en angulo 0")
time.sleep(5)

def Show_SensorU():
    #Sensor 1
    d1 = medir_distancia(TRIG1, ECHO1)
    time.sleep_ms(20)  # pequeño delay para evitar interferencias

    #Sensor 2
    d2 = medir_distancia(TRIG2, ECHO2)
    time.sleep_ms(10)
    
    print("Sensor 1:", "Sin lectura" if d1 is None else f"{round(d1,2)} mm")
    print("Sensor 2:", "Sin lectura" if d2 is None else f"{round(d2,2)} mm")
    time.sleep(0.1)
# Movimiento de prueba
while True:
    for ang in range(0, 201, 5):
        set_angle(ang)
        time.sleep(0.02)
        Show_SensorU()
        print(ang)

    for ang in range(200, -1, -5):
        set_angle(ang)
        time.sleep(0.02)
        Show_SensorU()
        print(ang)