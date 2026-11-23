import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf


def test_parler_tts_model():
    try:
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        model_name = "ai4bharat/indic-parler-tts"
        model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        description_tokenizer = AutoTokenizer.from_pretrained(
            model.config.text_encoder._name_or_path
        )

        prompt = "Hello, how are you doing today? I am good"
        description = (
            "A female speaker delivers a slightly expressive and animated speech "
            "with a moderate speed and pitch."
        )

        description_input_ids = description_tokenizer(
            description,
            return_tensors="pt",
        ).to(device)
        prompt_input_ids = tokenizer(prompt, return_tensors="pt").to(device)

        generation = model.generate(
            input_ids=description_input_ids.input_ids,
            attention_mask=description_input_ids.attention_mask,
            prompt_input_ids=prompt_input_ids.input_ids,
            prompt_attention_mask=prompt_input_ids.attention_mask,
        )

        audio_arr = generation.cpu().numpy().squeeze()
        sf.write("indic_tts_out.wav", audio_arr, model.config.sampling_rate)
        print("Audio saved to indic_tts_out.wav")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_parler_tts_model()
