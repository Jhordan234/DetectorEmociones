import cv2
import numpy as np
import tensorflow as tf
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Cargar modelo entrenado
modelo = tf.keras.models.load_model('D:\Entregable\modelo_emociones2.h5')

# Cargar clasificador de rostros de OpenCV
detector_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Clases de emociones (ajusta según tus carpetas reales)
clases = ['Enojado', 'Disgusto', 'Miedo', 'Feliz', 'Neutral', 'Triste', 'Sorprendido']

# Colores para cada emoción
colores = {
    'Enojado': (0, 0, 255),      # Rojo
    'Disgusto': (42, 42, 165),   # Marrón
    'Miedo': (128, 0, 128),      # Morado
    'Feliz': (0, 255, 0),        # Verde
    'Neutral': (128, 128, 128),  # Gris
    'Triste': (255, 0, 0),       # Azul
    'Sorprendido': (0, 165, 255) # Naranja
}

# Iniciar webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    rostros = detector_rostros.detectMultiScale(gris, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in rostros:
        # Recortar rostro, redimensionar e igualar al tamaño que espera el modelo
        rostro = gris[y:y+h, x:x+w]
        rostro_redimensionado = cv2.resize(rostro, (48, 48))
        rostro_normalizado = rostro_redimensionado / 255.0
        rostro_reshapeado = np.reshape(rostro_normalizado, (1, 48, 48, 1))

        # Predecir emoción
        prediccion = modelo.predict(rostro_reshapeado)
        emocion = clases[np.argmax(prediccion)]

        # Seleccionar color según la emoción
        color = colores.get(emocion, (255, 255, 255))  # Blanco por defecto si no encuentra la emoción

        # Dibujar rectángulo alrededor del rostro con el color correspondiente
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        # Mostrar emoción sobre el rostro
        cv2.putText(frame, emocion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Mostrar imagen en ventana
    cv2.imshow('Detector de Emociones', frame)

    # Salir con tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar y cerrar
cap.release()
cv2.destroyAllWindows()