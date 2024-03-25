#Import Pakcage
import cv2 as cv

#Import Your QrCode Pictures
qrCode = cv.imread("images/qrcode1.png")

#Create Class detector
detector = cv.QRCodeDetector()

#Read value from Qrcode
value,box,_ = detector.detectAndDecode(qrCode)

#Font putText
font = cv.FONT_HERSHEY_COMPLEX

#Show Value from QrCode
print(f"Value in qrCode=>{value}")

#Show Text on QrCode
cv.putText(qrCode,value,(int(box[0][0][0]),int(box[0][0][1])-10),font,.5,(255,255,0),1,cv.LINE_AA)

#Draw a rectangle around the qrcode
cv.line(qrCode,(int(box[0][0][0]),int(box[0][0][1])),(int(box[0][1][0]),int(box[0][1][1])),(255,255,0),3)
cv.line(qrCode,(int(box[0][0][0]),int(box[0][0][1])),(int(box[0][3][0]),int(box[0][3][1])),(255,255,0),3)
cv.line(qrCode,(int(box[0][3][0]),int(box[0][3][1])),(int(box[0][2][0]),int(box[0][2][1])),(255,255,0),3)
cv.line(qrCode,(int(box[0][2][0]),int(box[0][2][1])),(int(box[0][1][0]),int(box[0][1][1])),(255,255,0),3)


#Show Image
cv.imshow("qrCode",qrCode)
cv.waitKey(0)
cv.destroyAllWindows()