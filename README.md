# Face_Detection

Contiene el trabajo  con las librerias face_recognition y deepface, para detección y reconocimeinto facial.

Se hizo una prueba técnica con deepface y face_recognition buscando desarrollar un sistema de reconocimiento facial, como caso de uso se tomo la autenticación en maquinas expendedoras, siendo el objetivo hacer a ahora la verificación de la persona con reconocimiento facial en vez de usar sus credenciales.

Se hacen pruebas con el framework de deepface para encontrar la mejor conbinación de detectores, modelos de procesamiento y metricas de comparación para nuestra aplicación. Adicionalmente se hace un programa de detección con face_recognition

![](https://github.com/Juan-Good/Face_Detection/blob/main/images/caras.gif)

## Configuración del entorno

Para la configuración del entorno es necesaria la instalación de CMake y Visual Studio, lo invitamos a revisar el siguiente archivo donde encontrara una guia mas detallada.

## Tutorial

En Guia_deepface.ipynb ecnotrara un cuaderno para ejecutar en google colaboratory, las imagenes necesarias para correr la guia  se encuentran en el folder "Recursos Guia", alli encontrara las imagenes para subir a google colaboratory y trabajar con el cuadernillo.

## Reconocimiento

Los archivos:

- reconocimiento.py
- reconocimiento_emociones.py

 Hacen la detección de rostros en una imagen y lo comparan con los rostros de las imagenes en input, si detecta un rostro ajeno lo clasifica como desconocido. Adicionalmente reconocimiento_emociones.py reaaliza analisis de emociones sobre los rostros detectados

## Extracción de Rostros

 Dentro de la carpeta imagen encontrara el archivo face_extractor.py, este le permite extraer rostros de las imagenes que encuentre en input, los rostros se almacenaran en la carpet faces(si la carpeta no existe el script la creara)
