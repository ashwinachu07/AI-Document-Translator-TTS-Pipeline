# AI-Powered Text Extraction, Translation & Speech Synthesis Pipeline

An end-to-end multimodal pipeline designed to extract text from scanned documents and images using Optical Character Recognition (OCR), translate the extracted content across multiple languages using neural machine translation (NMT) engines, and synthesize natural spoken audio in the target language.

---

## 🌟 Key Features

- **Document Ingestion & Preprocessing**:
  - Direct digital text extraction from PDFs using `pdfplumber`.
  - Scanned PDF and image extraction with automated image preprocessing (grayscale binarization via Otsu thresholding in OpenCV) and `pytesseract` OCR.
  - Multi-page document rasterization via `pdf2image`.

- **Multi-Engine Translation**:
  - **Google Translate**: Online translation with wide language support.
  - **Argos Translate**: Fully offline, open-source neural machine translation.
  - **Helsinki-NLP MarianMT**: Hugging Face transformer models for localized sentence translation.

- **Multilingual Speech Synthesis (TTS)**:
  - **gTTS (Google Text-to-Speech)**: Fast, cloud-based audio generation for major languages.
  - **Indic Parler TTS**: High-quality expressive neural voice synthesis tailored for Indic languages.
  - **Coqui TTS**: Offline neural speech synthesis.
  - Automatic fallback mechanism if a primary TTS engine is unavailable.

---

## 📁 Repository Structure

```text
├── pdf-image-translator/
│   ├── src/
│   │   ├── main.py                     # Application entry point
│   │   ├── resources/
│   │   │   └── sample.pdf              # Sample document for verification
│   │   └── utils/
│   │       ├── ocr.py                  # OCR extraction & preprocessing routines
│   │       ├── translator.py           # Multi-engine translation logic
│   │       ├── text_to_speech.py       # Speech synthesis & fallback engine
│   │       ├── language_codes.py       # Supported language code references
│   │       ├── argos_install.py        # Automated Argos model downloader & installer
│   │       └── ...
│   ├── requirements.txt                # Python dependencies
│   └── README.md                       # Module documentation
├── t-t-v.py                            # Standalone quick text-to-voice utility
├── .gitignore                          # Git exclusion rules
└── README.md                           # Main repository documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

In addition to Python 3.9+, this project requires two external system tools:

1. **Tesseract OCR**:
   - **Windows**: Download the installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki) and add the install directory to your system `PATH`.
   - **Linux / Ubuntu**: `sudo apt install tesseract-ocr`
   - **macOS**: `brew install tesseract`

2. **Poppler** (required by `pdf2image` for rendering PDFs to images):
   - **Windows**: Download the latest release from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) and add its `bin` folder to your system `PATH`.
   - **Linux / Ubuntu**: `sudo apt install poppler-utils`
   - **macOS**: `brew install poppler`

---

### 2. Installation

1. **Clone the repository**:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <REPOSITORY_NAME>
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r pdf-image-translator/requirements.txt
   ```

---

### 3. (Optional) Setup Offline Translation Models

If you plan to use **Argos Translate** offline:
Run the built-in installer script to download and register pre-trained packages:
```bash
python pdf-image-translator/src/utils/argos_install.py
```

---

## 💻 Usage

To run the full interactive pipeline:

```bash
cd pdf-image-translator/src
python main.py
```

You will be prompted to:
1. Provide the path to your input image or PDF (e.g., `resources/sample.pdf`).
2. Specify your target language code (e.g., `ml` for Malayalam, `ta` for Tamil, `hi` for Hindi, `es` for Spanish).
3. Select your desired translation engine (`google`, `argos`, or `marian`).
4. Select your preferred TTS voice engine (`gtts`, `indic`, or `coqui`).

The translated audio file will be saved in `output_files/`.

---

## 📄 License

This project is licensed under the MIT License.
