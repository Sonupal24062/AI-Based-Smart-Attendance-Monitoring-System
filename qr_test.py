import pyqrcode

data = "Hello Sonu"

qr = pyqrcode.create(data)

qr.png("hello.png", scale=8)

print("QR Code Created Successfully!")