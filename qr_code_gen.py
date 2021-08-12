import pyqrcode 
from pyqrcode import QRCode 
url = "https://www.youtube.com/channel/UCHzrn2GHTDHNtOGjYFu7bLQ"
make = pyqrcode.create(url) 
make.svg("my_youtube_channel.svg", scale = 8, background="white")
