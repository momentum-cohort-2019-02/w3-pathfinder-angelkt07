#! python3
# resizeAndAddLogo.py - resizes all images in  current working direction to fit in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import images

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'