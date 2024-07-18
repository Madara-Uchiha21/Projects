import qrcode as qr

img = qr.make("https://github.com/Madara-Uchiha21")
img.save("Hashirama.png")
print(type(img))

print()

