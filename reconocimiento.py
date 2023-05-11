#Elaborado por Juan Andres Bueno

import cv2
import os
import face_recognition

# Crear encoders para cada rostro en la carpeta faces, si la carpeta no existe corra extractor_rostros.py, 
# este se encuentra en imagenes

#Codificar cada rostro
imageFacesPath = "faces"
facesEncodings = []
facesNames = []
for file_name in os.listdir(imageFacesPath):
     image = cv2.imread(imageFacesPath + "/" + file_name)
     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
     f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
     facesEncodings.append(f_coding)
     facesNames.append(file_name.split(".")[0])

# Capturar video
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
     ret, frame = cap.read()
     if ret == False:
          break
     frame = cv2.flip(frame, 1)
     detected_names=[]
     principal_person=''
     area=0
     area_mayor=0
     orig = frame.copy()

     #Definir detector
     face_locations = face_recognition.face_locations(frame, model="cnn")
     if face_locations != []:
        
        for face_location in face_locations:
            actual_face_encoding = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
            result = face_recognition.compare_faces(facesEncodings, actual_face_encoding)
            #print(result)
            if True in result:
               index = result.index(True)
               name = facesNames[index]
               detected_names.append(name)
               color = (125, 220, 0)

               #Calcular el area de cada rostro
               area= (face_location[3]-face_location[1])*(face_location[0]-face_location[2])
               
               #Definir el rostro mas grande en la imagen
               if area >area_mayor:
                    area_mayor=area
                    principal_person=name
               
               
            else:
               name = "Desconocido"
               color = (50, 50, 255)
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
            cv2.putText(frame, name, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
            #cv2.line(frame, (face_location[3]+20, face_location[0]), (face_location[1], face_location[2]), color, 2)  
     
     #Imprimir el usuario principal
     if face_locations != []:
          #print('Se ha detectado a:', detected_names)  
          print('El usuario principal es:',principal_person, 'con Area:', area)
      
     #Mostrar la imagen
     cv2.imshow("Frame", frame)

     #Salir con esc
     k = cv2.waitKey(1) & 0xFF
     if k == 27:
          break
cap.release()
cv2.destroyAllWindows()