import pytesseract
from PIL import Image

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image_path = './pic.png'  # Replace with the path to your image
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)