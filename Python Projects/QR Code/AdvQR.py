# some advance qr code

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('Uchiha')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="yellow")
img.save("qra.png")

print(type(img))

