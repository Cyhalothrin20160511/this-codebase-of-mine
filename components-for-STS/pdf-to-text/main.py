from pdf2image import convert_from_path
import pytesseract
import os

# Get the current directory (i.e., the path of the subfolder)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configure the path for Tesseract (Windows users need to specify the path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to Poppler (used to convert PDF to images)
poppler_path = os.path.join(current_dir, r'poppler-24.08.0\Library\bin')

def extract_text_from_image_pdf(pdf_path, output_file, lang):
    try:
        # Step 1: Convert the PDF into images
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
        # Step 2: Use OCR to process each image
        text = ""
        for i, image in enumerate(images):
            print(f"Processing page {i + 1}...")
            text += pytesseract.image_to_string(image, lang=lang) + "\n"
        
        # Step 3: Save the extracted text into a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        
        print(f"Extracted text has been saved to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Get user input for PDF file name and language
pdf_filename = input("Please enter the PDF file name (including extension): ")
lang_choice = input("Please enter the language ('rus' for Russian, 'ell' for Greek): ")

# Ensure the entered language is valid
if lang_choice not in ['rus', 'ell']:
    print("Invalid language choice. Please choose 'rus' (Russian) or 'ell' (Greek).")
else:
    # Ensure the file path is correct
    pdf_path = os.path.join(current_dir, pdf_filename)
    
    if not os.path.isfile(pdf_path):
        print(f"File {pdf_filename} not found. Please ensure the file path is correct.")
    else:
        # Generate the output file name
        output_file = os.path.splitext(pdf_filename)[0] + ".txt"
        
        # Call the function to process the file, passing the chosen language
        extract_text_from_image_pdf(pdf_path, output_file, lang_choice)
