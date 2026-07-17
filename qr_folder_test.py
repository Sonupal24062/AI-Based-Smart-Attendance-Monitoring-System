import os
import pyqrcode

folder = "QRDB"

# Create the folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

data = "TNSO9820"

qr = pyqrcode.create(data)

qr.png(os.path.join(folder, "TNSO9820.png"), scale=8)

print("QR Code Saved in QRDB Folder!")