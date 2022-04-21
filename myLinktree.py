import qrcode

data = "linktr.ee/lcaladoferreira"

img = qrcode.make(data)

img.save("/Users/leandrocalado/Desktop/QRCodePy/myQrCodes/myqrcode.png")

