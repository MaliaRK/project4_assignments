import qrcode

data = "This is my first QR code."

img = qrcode.make(data)

img.save("my qr code 1.png")
