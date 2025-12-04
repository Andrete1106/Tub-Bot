import serial
import cv2
import numpy as np


PORT = "COM13"
BAUD = 921600

# Abrir puerto
ser = serial.Serial(PORT, BAUD, timeout=1)

buffer = b""

print("Esperando video del ESP32...")

while True:
    # Leer datos del ESP32
    data = ser.read(4096)
    if not data:
        continue

    buffer += data

    # Buscar delimitadores
    start = buffer.find(b"FRAME_START")
    end = buffer.find(b"FRAME_END")

    # Si encontramos un frame completo
    if start != -1 and end != -1 and end > start:
        # Extraer bytes del JPEG
        frame_bytes = buffer[start + len(b"FRAME_START") : end].strip()

        # Limpiar el buffer para el siguiente frame
        buffer = buffer[end + len(b"FRAME_END") : ]

        # Decodificar la imagen JPEG
        img_array = np.frombuffer(frame_bytes, dtype=np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is not None:
            cv2.imshow("Video USB - ESP32", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

ser.close()
cv2.destroyAllWindows()
