import qrcode
data=""#Type what the output of the QR code will be. 
qr=qrcode.QRCode(version=1,box_size=10,border=8) #Version:QR code version, box_size:size of the QR code, border:the size of the scanned portion.
error_correction=qrcode.constants.ERROR_CORRECT_L
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")#You can choose the colors of the QR code.
img.save("QRcode.png")#Enter the name and type of the saved file.