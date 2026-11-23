import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import soundfile as sf

def test_parler_tts_model():
    try:
        # Set device (use GPU if available)
        device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # Load the model and tokenizers
        model_name = "ai4bharat/indic-parler-tts"
        model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        description_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

        # Define the prompt and description
        prompt = "Hello, how are you doing today? I am good"
        description = "A female speaker delivers a slightly expressive and animated speech with a moderate speed and pitch. The recording is of very high quality, with the speaker's voice sounding clear and very close up."

        # Tokenize the inputs
        description_input_ids = description_tokenizer(description, return_tensors="pt").to(device)
        prompt_input_ids = tokenizer(prompt, return_tensors="pt").to(device)

        # Generate the audio
        generation = model.generate(
            input_ids=description_input_ids.input_ids,
            attention_mask=description_input_ids.attention_mask,
            prompt_input_ids=prompt_input_ids.input_ids,
            prompt_attention_mask=prompt_input_ids.attention_mask
        )

        # Convert the generated audio to a NumPy array
        audio_arr = generation.cpu().numpy().squeeze()

        # Save the audio to a .wav file
        output_file = "indic_tts_out.wav"
        sf.write(output_file, audio_arr, model.config.sampling_rate)
        print(f"Audio saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

test_parler_tts_model()