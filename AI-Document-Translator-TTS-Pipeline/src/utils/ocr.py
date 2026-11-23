from pdf2image import convert_from_path
import pdfplumber
import pytesseract
import cv2
import numpy as np
import os

def preprocess_image(image):
    """Preprocess the image to improve OCR accuracy."""
    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    # Apply thresholding to binarize the image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return binary

def extract_text_from_pdf_direct(pdf_path):
    """Extract text directly from a PDF file if it contains embedded text."""
    try:
        text = ''
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error during direct PDF text extraction: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using OCR."""
    try:
        images = convert_from_path(pdf_path, dpi=300)
        text = ''
        for image in images:
            # Preprocess the image
            processed_image = preprocess_image(image)

            # Perform OCR on the preprocessed image
            text += pytesseract.image_to_string(processed_image, config='--psm 6')
        return text
    except Exception as e:
        print(f"Error during PDF text extraction: {e}")
        return None

def extract_text_from_image(image_path):
    """Extract text from an image file using OCR."""
    try:
        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Perform OCR on the preprocessed image
        text = pytesseract.image_to_string(processed_image, config='--psm 6')
        return text
    except Exception as e:
        print(f"Error during image text extraction: {e}")
        return None

def clean_extracted_text(text):
    """Clean up extracted text to remove unwanted characters or formatting."""
    # Remove extra spaces and newlines
    cleaned_text = ' '.join(text.split())

    # Optional: Replace common misinterpretations (e.g., 'ﬁ' -> 'fi')
    replacements = {
        'ﬁ': 'fi',
        'ﬂ': 'fl',
    }
    for old, new in replacements.items():
        cleaned_text = cleaned_text.replace(old, new)

    return cleaned_text

def extract_text(file_path):
    """Extract text from a PDF or image file."""
    if file_path.lower().endswith('.pdf'):
        # Try direct text extraction first
        text = extract_text_from_pdf_direct(file_path)
        if text:
            return clean_extracted_text(text)

        # Fallback to OCR if direct extraction fails
        text = extract_text_from_pdf(file_path)
        return clean_extracted_text(text) if text else None
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        text = extract_text_from_image(file_path)
        return clean_extracted_text(text) if text else None
    else:
        print("Unsupported file format.")
        return None