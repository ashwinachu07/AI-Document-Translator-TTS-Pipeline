from transformers import MarianMTModel, MarianTokenizer

def preload_marian_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    print(f"Preloading MarianMT model: {model_name}")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    print("Model preloaded successfully.")

# Example: Preload English to Malayalam model
preload_marian_model("en", "ml")
preload_marian_model("en", "ta")