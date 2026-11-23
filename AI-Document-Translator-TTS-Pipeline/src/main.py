import os
from datetime import datetime
from utils.ocr import extract_text_from_pdf, extract_text_from_image
from utils.translator import translate_text
from utils.text_to_speech import text_to_audio_with_fallback

def main():
    """
    Main function to orchestrate the PDF/image translation and speech conversion.
    """
    # Input file path
    file_path = input("Enter the path of the PDF or image file: ").strip()
    if not file_path:
        print("Error: No file path provided.")
        return

    # Extract text from the file
    if file_path.lower().endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)
    else:
        extracted_text = extract_text_from_image(file_path)

    if not extracted_text:
        print("Error: No text extracted from the file.")
        return

    print(f"Extracted Text: {extracted_text}")

    # Input target language
    target_language = input("Enter the target language code (e.g., 'ml' for Malayalam, 'ta' for Tamil): ").strip()
    if not target_language:
        print("Error: No target language provided.")
        return

    # Choose translation engine
    translation_engine = input("Choose translation engine ('google', 'argos', or 'marian'): ").strip().lower()
    if translation_engine not in ["google", "argos", "marian"]:
        print("Error: Invalid translation engine selected.")
        return

    # Translate the text
    translated_text = translate_text(extracted_text, target_language, engine=translation_engine)
    if not translated_text:
        print("Error: Translation failed.")
        return

    print(f"Translated Text: {translated_text}")

    # Choose TTS engine
    tts_engine = input("Choose TTS engine ('gtts', 'coqui', or 'indic'): ").strip().lower()
    if tts_engine not in ["gtts", "coqui", "indic"]:
        print("Error: Invalid TTS engine selected.")
        return

    # Optional description for Indic Parler TTS
    description = None
    if tts_engine == "indic":
        description = input("Enter a description for the speech (e.g., 'A female speaker with a cheerful tone'): ").strip()
        if not description:
            description = "A neutral speaker delivers the speech with a moderate speed and pitch."

    # Generate a unique output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(os.getcwd(), "output_files")
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    output_file = os.path.join(output_dir, f"{target_language}_output_{timestamp}.wav" if tts_engine == "indic" else f"{target_language}_output_{timestamp}.mp3")

    # Call the TTS function with fallback
    text_to_audio_with_fallback(translated_text, target_language, output_file, selected_engine=tts_engine, description=description)

    print(f"Process completed. Audio saved to: {output_file}")

if __name__ == "__main__":
    main()