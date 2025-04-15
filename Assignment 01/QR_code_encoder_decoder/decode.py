import qrcode

data1 = "This is my first QR code."

img = qrcode.make(data1)

img.save("D:/GIAIC_Q3_Python_Projects/project4_assignments/assignment_01/QR_code_encoder_decoder/myqrcode.png")



data2 = "This is my colorful QR code."

qr = qrcode.QRCode(version=1, border=5, box_size=10)

qr.add_data(data2)

qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("D:/GIAIC_Q3_Python_Projects/project4_assignments/assignment_01/QR_code_encoder_decoder/mycolorqrcode.png")