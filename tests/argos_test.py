from argostranslate import translate


def translate_text_with_argos(text, source_language, target_language):
    """Translate text using Argos Translate."""
    try:
        installed_languages = translate.get_installed_languages()
        from_lang = next(lang for lang in installed_languages if lang.code == source_language)
        to_lang = next(lang for lang in installed_languages if lang.code == target_language)
        return from_lang.get_translation(to_lang).translate(text)
    except Exception as e:
        print(f"Error during Argos translation: {e}")
        return None


if __name__ == "__main__":
    translated_text = translate_text_with_argos(
        "Hello, how are you?",
        "en",
        "hi",
    )
    print(f"Translated Text: {translated_text}")
