import cv2
import os

images_Path = os.path.join('images','input')
#images_Path = (r"C:\Users\juanb\Face_Recognition\FR_python_p\images\input")
print(images_Path)


if not os.path.exists("faces"):
    os.makedirs("faces")
    print ("Nueva carpeta creada: faces")


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count=0
for imageName in os.listdir(images_Path):
    print (imageName)
    img = cv2.imread(images_Path + "/" + imageName)
    faces = faceClassif.detectMultiScale(img, 1.1, 5)

    for (x, y, w, h) in faces:
          #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
          face = img[y:y + h, x:x + w]
          face = cv2.resize(face, (150, 150))
          cv2.imwrite("faces/" + imageName, face)
          count += 1

    cv2.imshow("Image", img)
    cv2.waitKey(0)
cv2.destroyAllWindows()