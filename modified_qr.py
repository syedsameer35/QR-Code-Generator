import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://www.youtube.com/shorts/iyAvtb_zpYQ")
qr.make(fit=True)
img = qr.make_image(fill_color="brown",back_color="grey")
img.save("short_video.png")