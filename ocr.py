import pytesseract
import sys
import pyperclip

if len(sys.argv) != 2:
    sys.exit("Usage: python ocr.py image.png/jpg/bmp")

extracted_text = pytesseract.image_to_string(sys.argv[1])
print(extracted_text)
pyperclip.copy(extracted_text)
