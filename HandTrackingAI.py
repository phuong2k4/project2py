import cv2
import mediapipe as mp
import time

from statsmodels.stats.libqsturng.make_tbls import success
capture = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(False)
mpDraw = mp.solutions.drawing.utils

pTime = 0
cTime = 0

while True:
    success, img = capture.read()

    imgRBG = cv2.cvtColor(img, cv2.COLOR_BRG2RGB)
    result = hands.process(imgRBG)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, ln in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(ln.x*w), int(ln.y*h)
                print(id,cx,cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img.str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255),3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()