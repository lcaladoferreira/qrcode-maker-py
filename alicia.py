import qrcode

data = "Meu QR code criado no Python"

img = qrcode.make(data)

img.save("/Users/leandrocalado/Desktop/QRCodePy/myQrCodes/aliciaqrcode.png")


