from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

def convert_pdf_to_images(pdf_path, output_folder):
    # use pdf2image to convert pdf into usable images
    images = convert_from_path(pdf_path, output_folder)
    image_paths = []

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        image.save(image_path)
        image_paths.append(image_path)

    return image_paths

def custom_preprocess(image):
    pytesseract

def ocr_on_image(image):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)
    return text
