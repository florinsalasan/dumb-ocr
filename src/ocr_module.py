from pdf2image import convert_from_path
import pytesseract
from PIL import Image, ImageEnhance
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

def custom_preprocess(image_path):
    image = Image.open(image_path)
    contrasted_image = enhance_contrast(image)

    preprocessed_path =os.path.splitext(image_path)[0] + "_preprocessed.png"
    contrasted_image.save(preprocessed_path)
    return preprocessed_path

def enhance_contrast(image, factor=1.5):
    # use PIL's ImageEnhance to increase the contrast
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(factor)
    return enhanced_image


def ocr_on_all(image_paths):
    # call ocr_on_image for all images in the path
    extracted_texts = []

    for image_path in image_paths:
        text = ocr_on_image(image_path)
        extracted_texts.append(text)

    return extracted_texts

def ocr_on_image(image_path):
    # Use pytesseract to extract text from the image
    image  = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
