def translate_text(text, dest_language, engine="google", source_language="en"):
    """
    Translate text to the target language.

    Parameters:
    - text: The text to translate.
    - dest_language: The target language code (e.g., 'ml' for Malayalam, 'ta' for Tamil).
    - engine: The translation engine to use ('google', 'argos', or 'marian').
    - source_language: The source language code (default is 'en' for English).

    Returns:
    - Translated text.
    """
    if engine == "google":
        # Use Google Translate (online)
        try:
            from googletrans import Translator

            translator = Translator()
            translation = translator.translate(text, src=source_language, dest=dest_language)
            return translation.text
        except Exception as e:
            print(f"Error during Google translation: {e}")
            return None
    elif engine == "argos":
        # Use Argos Translate (offline)
        try:
            from argostranslate import translate

            installed_languages = translate.get_installed_languages()
            from_lang = next(lang for lang in installed_languages if lang.code == source_language)  # Source language
            to_lang = next(lang for lang in installed_languages if lang.code == dest_language)  # Target language
            translation = from_lang.get_translation(to_lang).translate(text)
            return translation
        except Exception as e:
            print(f"Error during Argos translation: {e}")
            return None
    elif engine == "marian":
        # Use MarianMT (Hugging Face) for translation
        try:
            from transformers import MarianMTModel, MarianTokenizer

            model_name = f"Helsinki-NLP/opus-mt-{source_language}-{dest_language}"
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)

            # Split the text into smaller chunks (e.g., by lines)
            lines = text.split("\n")  # Split by newline characters
            translated_lines = []

            for line in lines:
                if line.strip():  # Skip empty lines
                    # Tokenize the input text
                    inputs = tokenizer(line, return_tensors="pt", padding=True)

                    # Generate translation
                    translated = model.generate(**inputs)
                    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
                    translated_lines.append(translated_text)

            # Combine the translated lines into a single output
            return "\n".join(translated_lines)

        except Exception as e:
            print(f"Error during MarianMT translation: {e}")
            return None
    else:
        print(f"Unsupported translation engine: {engine}")
        return None