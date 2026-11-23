from gtts import gTTS
from googletrans import Translator
import os

def translate_text(text, dest_language):
    """Translate text to the target language."""
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

def text_to_audio(text, language, output_file):
    """Convert text to speech and save it as an audio file."""
    try:
        tts_file = gTTS(text=text, lang=language, slow=False)
        tts_file.save(output_file)
        print(f"Audio saved to {output_file}")
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")

def main():
    """Translate text and convert it to speech."""
    english_text = input("Enter text to translate: ").strip()
    if not english_text:
        print("Error: No text provided.")
        return

    target_language = input("Enter target language code (e.g., 'es' for Spanish): ").strip()
    if not target_language:
        print("Error: No language code provided.")
        return

    translated_text = translate_text(english_text, target_language)
    if translated_text:
        print(f"English Text: {english_text}")
        print(f"Translated Text: {translated_text}")
        output_file = f"{target_language}_output_{len(english_text)}.mp3"
        text_to_audio(translated_text, target_language, output_file)

if __name__ == "__main__":
    main()
