import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(gray,frame):
	face=face_cascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		gray_eye=gray[y:y+h,x:x+w]
		color_eye=frame[y:y+h,x:x+w]
		eye=eye_cascade.detectMultiScale(gray_eye,1.3,5)
		for (ex,ey,ew,eh) in eye:
			cv2.rectangle(color_eye,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
	return cv2.flip(frame,1)



cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 24.0, (680,480),True)


while (cap.isOpened()):
	ret,frames=cap.read()
	if ret==True:
		grays=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
		output=detect(grays,frames)
		print(type(frames))
		
		cv2.imshow('Face_Det',output)
		
		if cv2.waitKey(1) & 0XFF==ord('q'):
			break
		else:
			print(out.write(frames))
cap.release()
out.release()
cv2.destroyAllWindows()