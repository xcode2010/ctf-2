import sys
from PIL import Image

height = 150
width = 200

image = Image.frombytes('RGB', (width, height), open(sys.argv[1], 'rb').read()).transpose(Image.FLIP_TOP_BOTTOM)
image.show()