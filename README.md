# AI-Powered Text Extraction, Translation & Speech Synthesis Pipeline

This project is designed to scan PDF files and images, extract text using Optical Character Recognition (OCR), translate the extracted text into a specified language, and convert the translated text into speech.

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
├── src/
│   ├── main.py                         # Application entry point
│   ├── resources/
│   │   └── sample.pdf                  # Sample document for verification
│   └── utils/
│       ├── ocr.py                      # OCR extraction & preprocessing routines
│       ├── translator.py               # Multi-engine translation logic
│       ├── text_to_speech.py           # Speech synthesis & fallback engine
│       ├── language_codes.py           # Supported language code references
│       ├── argos_install.py            # Automated Argos model downloader & installer
│       └── ...
├── tests/
│   ├── argos_test.py                   # Argos translation smoke test
│   ├── marianmt_models.py              # MarianMT model download test
│   └── parler_test.py                  # Indic Parler TTS smoke test
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git exclusion rules
└── README.md                           # Main repository documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

Python 3.9 or later is recommended. This project requires two external system tools:

1. **Tesseract OCR**:
   - **Windows**: Install Tesseract OCR, commonly to `C:\Program Files\Tesseract-OCR`, and add that directory to `PATH`. Restart the terminal or VS Code after updating `PATH`.
   - Verify it with `tesseract --version`.
   - **Linux / Ubuntu**: `sudo apt install tesseract-ocr`
   - **macOS**: `brew install tesseract`

2. **Poppler** (required by `pdf2image` for rendering PDFs to images):
   - **Windows**: Download and extract Poppler for Windows, then add the extracted `poppler-\...\Library\bin` directory to `PATH`.
   - Verify it with `pdfinfo -v`.
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
   pip install -r requirements.txt
   ```

---

### 3. (Optional) Setup Offline Translation Models

If you plan to use **Argos Translate** offline:
Run the built-in installer script to download and register pre-trained packages:
```bash
python src/utils/argos_install.py --from en --to hi
```

Replace `hi` with another Argos-supported target code, such as `ml`, `ta`, `te`, or `es`, when installing a different language pair:
```bash
python src/utils/argos_install.py --from en --to ml
```

The installer updates the Argos package index and downloads the requested package. Local `.argosmodel` files can also be installed manually through Argos, but they are not required and are ignored by Git.

For **MarianMT**, language-pair models are downloaded automatically from Hugging Face on first use. For **Indic Parler TTS**, `ai4bharat/indic-parler-tts` is downloaded on first use. Internet access, memory, and disk space are required for these first-time downloads. A GPU is recommended for neural TTS and MarianMT, but CPU operation is also possible.

---

## 💻 Usage

To run the full interactive pipeline:

```bash
python src/main.py
```

You will be prompted to:
1. Provide the path to your input image or PDF (e.g., `resources/sample.pdf`).
2. Specify your target language code (e.g., `ml` for Malayalam, `ta` for Tamil, `hi` for Hindi, `es` for Spanish).
3. Select your desired translation engine (`google`, `argos`, or `marian`).
4. Select your preferred TTS voice engine (`gtts`, `indic`, or `coqui`).

The translated audio file will be saved in `output_files/`.

---

## 📦 Dependencies

- OCR: `pytesseract`, `pdf2image`, `pdfplumber`, `opencv-python`, and `Pillow`
- Translation: `googletrans`, `argostranslate`, and `transformers`
- Speech: `gtts`, `coqui-tts`, `parler_tts`, `torch`, and `soundfile`
- Model support: `indic-nlp-library`, `sentencepiece`, `safetensors`, and `accelerate`

---

## ⚠️ Known Limitations

- OCR quality depends on image resolution and document layout.
- Google Translate and gTTS require internet access.
- MarianMT and Indic Parler TTS download large models when first used.
- Neural TTS and MarianMT may be slow without a supported GPU.
- Argos, MarianMT, and Coqui support only their available languages or language pairs.

---

## Contributing

Contributions, bug reports, and feature suggestions are welcome. Please open an issue or submit a pull request with a clear description of the proposed change.

---

Copyright (c) 2026 Ashwin

