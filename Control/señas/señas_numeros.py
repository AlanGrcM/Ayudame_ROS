import cv2
#import time
#import os
import handTrackingModule as htm
import paho.mqtt.client as mqtt


broker_address = "173.31.2.100"
client = mqtt.Client('laei') # Creación del cliente 
client.connect(broker_address)
topic = "prueba"



cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4, 480)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
        k= lmlist[8][2] > lmlist[6][2]
        if not k and not lmlist[20][2] < lmlist[18][2]:
            n=1
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "Adelante")
        if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]    and not lmlist[4][1] > lmlist[8][1]: 
            n=2
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "Atras")
        if lmlist[4][1]  >lmlist[12][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]   and lmlist[16][2] > lmlist[14][2]: 
            n=3
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "Derecha")
        if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[20][2] < lmlist[18][2]: 
            n=4
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "Izquierda")
        if  lmlist[4][1] > lmlist[12][1] and    lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[20][2] < lmlist[18][2]: 
            n=5
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "D1A")
        if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] < lmlist[12][1] and lmlist[20][2] > lmlist[18][2]: 
            n=6
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "D1B")
        if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
            n=7
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "D2A")
        if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
            n=8
            #cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "D2B")
        if lmlist[8][2] > lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
            n=9
            cv2.rectangle(img,(0,0),(80,80),(0,0,255),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "GDerecha")
        if lmlist[8][2] > lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] > lmlist[18][2]: 
            n=10
            cv2.rectangle(img,(0,0),(160,80),(0,0,255),cv2.FILLED)
            #cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),2)1
            cv2.putText(img,str(n),(15,65), 1, 6, (255, 255, 255), 3)
            client.publish(topic, "Alto")
    cv2.imshow("image",img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
