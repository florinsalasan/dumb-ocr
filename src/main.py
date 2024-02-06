from ocr_module import convert_pdf_to_images, ocr_on_all, custom_preprocess 

def main(pdf_path):
    # Step 1: Convert PDF to images
    output_folder = 'output_images/'
    image_paths = convert_pdf_to_images(pdf_path, output_folder)

    # Step 2: Perform preprocessing on images
    preprocessed_images = custom_preprocess(image_paths)

    # Step 3: Perform OCR
    extracted_texts = ocr_on_all(preprocessed_images)

    # Step 4: Print or process the extracted texts
    for i, text in enumerate(extracted_texts):
        print(f"Text from page {i + 1}:\n{text}\n")


if __name__ == "__main__":
    # Provide the path to the PDF file as a command-line argument
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_pdf>")
    else:
        pdf_path = sys.argv[1]
        main(pdf_path)

