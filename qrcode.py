import pyqrcode
import png
from pyqrcode import QRCode
  
  
raj = "rajcv.pythonanywhere.com"
  
# Generate QR code
url = pyqrcode.create(raj)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)