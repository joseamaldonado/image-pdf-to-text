import os
from PIL import Image
import pillow_heif
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_heic_to_jpg(heic_path, jpg_path):
    heif_file = pillow_heif.read_heif(heic_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(jpg_path, "JPEG")

def combine_images_to_pdf(image_paths, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    for image_path in image_paths:
        img = Image.open(image_path)
        width, height = letter
        c.setPageSize((width, height))
        c.drawImage(image_path, 0, 0, width, height)
        c.showPage()
    c.save()

def main():
    current_dir = os.getcwd()
    temp_dir = os.path.join(current_dir, "temp_jpg")
    os.makedirs(temp_dir, exist_ok=True)

    heic_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.heic')]
    jpg_files = []

    for heic_file in heic_files:
        heic_path = os.path.join(current_dir, heic_file)
        jpg_file = os.path.splitext(heic_file)[0] + ".jpg"
        jpg_path = os.path.join(temp_dir, jpg_file)
        convert_heic_to_jpg(heic_path, jpg_path)
        jpg_files.append(jpg_path)

    output_pdf = os.path.join(current_dir, "combined_images.pdf")
    combine_images_to_pdf(jpg_files, output_pdf)

    # Clean up temporary JPG files
    for jpg_file in jpg_files:
        os.remove(jpg_file)
    os.rmdir(temp_dir)

    print(f"Combined PDF created: {output_pdf}")

if __name__ == "__main__":
    main()
