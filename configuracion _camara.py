#Este codigo permite identificar las diferentes camaras disponibles

import cv2

# Crea un objeto de captura de video
# El numero indica el numero de la camara, normalmente 0 webcam, 1 camara externa
cap = cv2.VideoCapture(1)

# Establece el ancho y alto del marco de captura
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Itera hasta que el usuario presione la tecla 'q'
while True:
    # Lee un marco de video
    ret, frame = cap.read()

    # Muestra el marco en una ventana
    cv2.imshow('Video Capture', frame)

    # Espera 1ms y comprueba si el usuario ha presionado la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra la ventana
cap.release()
cv2.destroyAllWindows()
