"""
    Hello and thanks because you taked a look at this script
    You asked you how other peoples sees you? This script is for you, now you can discover the answer! Only run this script and click "q" when you want to close the window
    Follow me on GitHub and TikTok(@robert_de_romania) if you want to support me :)
"""

import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    frame = cv.flip(frame, 1)
    cv.imshow("Camera POV", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()