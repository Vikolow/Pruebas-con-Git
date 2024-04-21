import qrcode  
from PIL import Image
import os

link_web = 'http://www.example.com'
qr = qrcode.QRCode(version = 2, box_size = 7, border = 7)
#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
#The box_size parameter controls how many pixels each box of the QR code is.
#The border parameter controls how many boxes thick the border should be.

qr.add_data(link_web)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('image_as_qr.png')



###### To change the directory where the QR code is located#######

# import os required

## Specify the directory where you want to save the image
#save_dir = '/path/to/your/directory/'

# Save the image with the full path
#img.save(os.path.join(save_dir, 'your_image.png')
