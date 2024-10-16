# image-pdf-to-text

This project provides tools to convert HEIC images to a combined PDF and then extract text from the PDF using OCR.

## Components

1. `image_combiner.py`: Converts HEIC files in the directory to a single combined PDF.
2. `pdf_scanner.py`: Performs OCR on PDF files to extract text.

## Requirements

- Python 3.x
- Pillow
- pillow_heif
- reportlab
- pdf2image
- pytesseract

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/image-pdf-to-text.git
   cd image-pdf-to-text
   ```

2. Install the required packages:
   ```
   pip install Pillow pillow_heif reportlab pdf2image pytesseract
   ```

3. Ensure you have Poppler and Tesseract installed on your system.

## Usage
Scan an image PDF. 
1. Run the PDF scanner:
   ```
   python pdf_scanner.py
   ```
   This will process all PDF files in the directory and output text files in the `output` folder.

Have iPhone screenshots that you want to scan? 
1. Place your HEIC files in the project directory.

2. Run the image combiner:
   ```
   python image_combiner.py
   ```
   This will create a `combined_images.pdf` file.

3. Run the PDF scanner:
   ```
   python pdf_scanner.py
   ```
   This will process all PDF files in the directory and output text files in the `output` folder.

## License

[MIT License](LICENSE)
