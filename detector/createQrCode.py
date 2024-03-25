#Import Package
import os
import segno

qqrcode = segno.make_qr("Hello, World")


#Text for Make QRCode
text = "Hello!!"
QrCode = segno.make_qr(text)

#Save
file_name ="images/qrcode1.png"
i = 1
def SaveImage():
    global i
    file_name =f"images/qrcode{i}.png"
    if os.path.isfile(file_name):
        i+=1
        SaveImage()
    else:
        QrCode.save(f"images/qrcode{i}.png",
                    scale=5,
                    border=0)
SaveImage()