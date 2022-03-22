import qrcode 
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = "Testing..."
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
