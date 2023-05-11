import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import face_recognition
from deepface import DeepFace

# Crear encoders para cada rostos
imageFacesPath = "faces"
facesEncodings = []
facesNames = []
for file_name in os.listdir(imageFacesPath):
     image = cv2.imread(imageFacesPath + "/" + file_name)
     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
     facesEncodings.append(f_coding)
     facesNames.append(file_name.split(".")[0])
i=0
# Capturar VIdeo
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Detector facial
#faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Declarar una detección previa
predicciones=[{'age': 34,
  'region': {'x': 160, 'y': 368, 'w': 445, 'h': 528},
  'gender': {'Woman': 3.5714250057935715, 'Man': 96.42857313156128},
  'dominant_gender': 'Man',
  'emotion': {'angry': 78.03442943301377,
   'disgust': 0.0005738243886354714,
   'fear': 2.0223939134117312,
   'happy': 4.533291630281201e-05,
   'sad': 19.299734789117263,
   'surprise': 7.413091915861416e-07,
   'neutral': 0.6428263067648594},
  'dominant_emotion': 'angry'}]
x=10
w=10
y=20
h=200
while True:
     ret, frame = cap.read()
     if ret == False:
          break
     frame = cv2.flip(frame, 1)
     orig = frame.copy()

     #Declarar el detector
     face_locations = face_recognition.face_locations(frame, model="cnn")
     if face_locations != []:
        

        for face_location in face_locations:
            actual_face_encoding = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
            result = face_recognition.compare_faces(facesEncodings, actual_face_encoding)

            #print(result)
            if True in result:
               index = result.index(True)
               name = facesNames[index]
               color = (125, 220, 0)
               
               #Cada cuantos cuadros se realiza un analisis de emociones
               if (i%20 == 0):
                    predicciones = DeepFace.analyze(frame, enforce_detection=False, actions = ['age', 'emotion'])
                    print(predicciones[0]['dominant_emotion'])
                    
               

            else:
               name = "Desconocido"
               color = (50, 50, 255)
            
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 50), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
            cv2.putText(frame, name, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
            if len(predicciones):
               cv2.putText(frame, predicciones[0]['dominant_emotion'], (face_location[3], face_location[2] + 40), 2, 0.7, (255, 255, 255), 1)
            i=i+1
     
     #Imprimir el analisis de emociones
     if (1):
          #ordenar emociones
          emotion = predicciones[0]['emotion']
          emotion_df = pd.DataFrame(emotion.items(), columns=['emotion', 'score'])
          emotion_df = emotion_df.sort_values(by=["score"], ascending=False ).reset_index(drop=True)
          #copiar
          overlay=frame.copy()
          opacity = 0.2
          cv2.rectangle(frame, (x + w, y-5), (x + w + 112, y + h), (10, 10, 0), cv2.FILLED)
          frame = cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame )
          cv2.putText( frame, 'Emotions', (x + w, y + 20),
                           cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 155, 255), 1)
          for index, instance in emotion_df.iterrows():
               current_emotion = instance['emotion']
               emotion_label = f"{current_emotion} "
               emotion_score = instance['score'] / 100
               bar_x = 35  # Tamaño si una emoción esta en 100%
               bar_x = int(bar_x * emotion_score)

               text_location_y = y + 20 + (index + 1) * 20
               text_location_x = x + w 
               cv2.putText( frame, emotion_label, (text_location_x, text_location_y),
                           cv2.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255), 1)
               cv2.rectangle(frame,(x + w + 70, y + 13 + (index + 1) * 20),
                              ( x + w + 70 + bar_x,y + 13 + (index + 1) * 20 + 5,),
                              (255, 255, 255),cv2.FILLED,)


     cv2.imshow("Frame", frame)
     k = cv2.waitKey(1) & 0xFF
     if k == 27:
          break
cap.release()
cv2.destroyAllWindows()