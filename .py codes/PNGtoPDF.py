from PIL import Image
from fpdf import FPDF
import os

def convert_images_to_pdf(folder_path, output_path):
    # Get a list of all PNG files in the folder
    image_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

    if not image_files:
        print("No PNG files found in the folder.")
        return

    # Create a new PDF object
    pdf = FPDF()

    # Iterate over the PNG files and add each image to the PDF
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        pdf.add_page()
        pdf.image(image_path, 0, 0, pdf.w, pdf.h)

    # Save the PDF file
    pdf.output(output_path)

    print(f"PDF file saved at: {output_path}")

# Provide the folder path containing PNG files and the output PDF file path
folder_path = "D:/MiniListic/GraphicDesigns/NatElec"
output_path = "D:/MiniListic/GraphicDesigns/NatElec"

# Call the function to convert images to PDF
convert_images_to_pdf(folder_path, output_path)
