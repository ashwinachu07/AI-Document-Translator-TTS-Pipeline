# PDF Image Translator

This project is designed to scan PDF files and images, extract text using Optical Character Recognition (OCR), translate the extracted text into a specified language, and convert the translated text into speech.

## Project Structure

```
pdf-image-translator
├── src
│   ├── main.py               # Entry point of the application
│   ├── utils
│   │   ├── ocr.py           # Functions for Optical Character Recognition
│   │   ├── translator.py     # Functions for translating text
│   │   └── text_to_speech.py # Functions for converting text to speech
│   └── resources
│       └── sample.pdf       # Sample PDF file for testing
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in version control
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd pdf-image-translator
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, install the required libraries using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF or image files in the `src/resources` directory.
2. Run the application:
   ```
   python src/main.py
   ```
3. Follow the prompts to select the file and specify the target language for translation.

## Dependencies

This project requires the following Python libraries:

- `pytesseract` for OCR
- `googletrans` for translation
- `gtts` for text-to-speech conversion
- `Pillow` for image processing
- `PyPDF2` for PDF handling

Make sure to check the `requirements.txt` file for the exact versions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.