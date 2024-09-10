import os
import tempfile
import shutil
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Set paths for Poppler and Tesseract
poppler_path = "/opt/homebrew/bin"
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

print("Script started")

def pdf_to_images(pdf_path, temp_dir):
    print(f"Converting PDF: {pdf_path}")
    try:
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        print(f"Converted {len(images)} pages")
    except Exception as e:
        print(f"Error converting PDF: {str(e)}")
        raise
    
    image_paths = []
    for i, image in enumerate(images):
        file_name = f'page_{i+1}.tiff'
        file_path = os.path.join(temp_dir, file_name)
        image.save(file_path, 'TIFF')
        image_paths.append(file_path)
    
    return image_paths

def perform_ocr(image_path):
    print(f"Performing OCR on: {image_path}")
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        print("OCR completed successfully")
    except Exception as e:
        print(f"Error performing OCR: {str(e)}")
        raise
    return text

def process_pdf(pdf_path, output_folder):
    with tempfile.TemporaryDirectory() as temp_dir:
        image_paths = pdf_to_images(pdf_path, temp_dir)
        
        all_text = ""
        for image_path in image_paths:
            text = perform_ocr(image_path)
            all_text += text + "\n\n--- Page Break ---\n\n"
        
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        text_file_path = os.path.join(output_folder, f'{base_name}_extracted_text.txt')
        os.makedirs(output_folder, exist_ok=True)
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(all_text)
        
        print(f"OCR complete. Text saved to {text_file_path}")
        
if __name__ == "__main__":
    # Usage
    output_folder = 'output'

    print("Starting PDF processing")
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf_path = filename
            print(f"Processing {pdf_path}...")
            try:
                process_pdf(pdf_path, output_folder)
            except Exception as e:
                print(f"Error processing {pdf_path}: {str(e)}")

    print("All PDFs processed.")