#Import Pakcage
import cv2 as cv

#Read Image From a WebCam
cap = cv.VideoCapture(0)

#Create Class detector
detector = cv.QRCodeDetector()

#Font putText
font = cv.FONT_HERSHEY_COMPLEX

#Read Frame from webcam
while True:
    _,frame = cap.read()
    #Read value from Qrcode
    value,box,_ = detector.detectAndDecode(frame)
    #Draw a rectangle around the qrcode
    if value != "":
        #Show Value from QrCode
        print(f"Value in qrCode=>{value}")
        #Show Text on QrCode
        cv.putText(frame,value,(int(box[0][0][0]),int(box[0][0][1])-10),font,.5,(255,255,0),1,cv.LINE_AA)
        cv.line(frame,(int(box[0][0][0]),int(box[0][0][1])),(int(box[0][1][0]),int(box[0][1][1])),(255,255,0),3)
        cv.line(frame,(int(box[0][0][0]),int(box[0][0][1])),(int(box[0][3][0]),int(box[0][3][1])),(255,255,0),3)
        cv.line(frame,(int(box[0][3][0]),int(box[0][3][1])),(int(box[0][2][0]),int(box[0][2][1])),(255,255,0),3)
        cv.line(frame,(int(box[0][2][0]),int(box[0][2][1])),(int(box[0][1][0]),int(box[0][1][1])),(255,255,0),3)

    #Show Frame
    cv.imshow("Frame",frame)
    
    #Exit Whit esc
    keys=cv.waitKey(5) & 0xff
    if(keys == 27):
        break
cv.destroyWindow()
cap.release()


