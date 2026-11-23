from googletrans import LANGUAGES
from argostranslate import translate
from indicnlp.tokenize import sentence_tokenize

def list_supported_languages(engine):
    """List supported languages for the specified translation engine."""
    if engine == "google":
        print("\nSupported languages for Google Translate:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language}")
    elif engine == "argos":
        print("\nSupported languages for Argos Translate:")
        installed_languages = translate.get_installed_languages()
        if not installed_languages:
            print("No Argos Translate language models are installed. Please install models first.")
        else:
            for lang in installed_languages:
                print(f"Language: {lang.name}, Code: {lang.code}")
    elif engine == "indic_tts":
        print("\nSupported languages for Indic TTS:")
        print("Tamil (ta), Malayalam (ml), Hindi (hi), Telugu (te), Kannada (kn), Bengali (bn)")
    else:
        print(f"Unsupported engine: {engine}")

def preprocess_text_with_indic(text, language):
    """Preprocess text using Indic NLP."""
    try:
        sentences = sentence_tokenize.sentence_split(text, lang=language)
        print("\nTokenized Sentences:")
        for sentence in sentences:
            print(sentence)
    except Exception as e:
        print(f"Error during text preprocessing: {e}")

def main():
    """Main function to list supported languages for the chosen engine."""
    print("Choose a translation or TTS engine:")
    print("1. Google Translate")
    print("2. Argos Translate")
    print("3. Indic TTS")
    print("4. Indic NLP (Preprocessing)")
    choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

    if choice == "1":
        list_supported_languages("google")
    elif choice == "2":
        list_supported_languages("argos")
    elif choice == "3":
        list_supported_languages("indic_tts")
    elif choice == "4":
        text = input("Enter text to preprocess: ").strip()
        language = input("Enter language code (e.g., 'ml' for Malayalam, 'ta' for Tamil): ").strip()
        preprocess_text_with_indic(text, language)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
