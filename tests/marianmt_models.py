from transformers import MarianMTModel, MarianTokenizer


def preload_marian_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    print(f"Preloading MarianMT model: {model_name}")
    MarianTokenizer.from_pretrained(model_name)
    MarianMTModel.from_pretrained(model_name)
    print("Model preloaded successfully.")


if __name__ == "__main__":
    preload_marian_model("en", "ml")
    preload_marian_model("en", "ta")
