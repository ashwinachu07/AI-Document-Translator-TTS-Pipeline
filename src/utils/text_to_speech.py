from gtts import gTTS
import os
from datetime import datetime

def text_to_audio_with_indic_parler(prompt, description, output_file):
    """
    Convert text to speech using Indic Parler TTS.

    Parameters:
    - prompt: The text to convert to speech.
    - description: A detailed description of how the speech should sound.
    - output_file: The path to save the audio file.
    """
    try:
        from parler_tts import ParlerTTSForConditionalGeneration
        from transformers import AutoTokenizer
        import torch
        import soundfile as sf

        # Set device (use GPU if available)
        device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # Load the model and tokenizers
        model_name = "ai4bharat/indic-parler-tts"
        model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        description_tokenizer = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)

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
        sf.write(output_file, audio_arr, model.config.sampling_rate)
        print(f"Audio saved to: {output_file}")

    except Exception as e:
        print(f"Error during Indic Parler TTS call: {e}")

def text_to_audio(text, language, output_file, engine="gtts", description=None):
    """
    Convert text to speech and save it as an audio file.

    Parameters:
    - text: The text to convert to speech.
    - language: The language code (e.g., 'ml' for Malayalam, 'ta' for Tamil, 'en' for English).
    - output_file: The path to save the audio file.
    - engine: The TTS engine to use ('gtts', 'coqui', or 'indic').
    - description: A detailed description of how the speech should sound (used for Indic Parler TTS).
    """
    try:
        # Validate inputs
        if not text:
            raise ValueError("Text for TTS cannot be empty.")
        if not language:
            raise ValueError("Language code cannot be empty.")
        if engine not in ["gtts", "coqui", "indic"]:
            print(f"Unsupported TTS engine: {engine}")
            return  # Exit the function early

        # Determine the correct file extension
        file_extension = ".mp3" if engine == "gtts" else ".wav"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.splitext(output_file)[0] + f"_{timestamp}{file_extension}"

        if engine == "gtts":
            print(f"Using Google TTS for language: {language}")
            tts_file = gTTS(text=text, lang=language, slow=False)
            tts_file.save(output_file)
        elif engine == "coqui":
            print("Using Coqui TTS for natural-sounding speech")
            from TTS.api import TTS

            tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
            print(f"Using Coqui TTS model: {tts.model_name}")
            tts.tts_to_file(text=text, file_path=output_file)
        elif engine == "indic":
            print(f"Using Indic Parler TTS for language: {language}")
            if not description:
                description = "A neutral speaker delivers the speech with a moderate speed and pitch."
            text_to_audio_with_indic_parler(text, description, output_file)
        else:
            print(f"Unsupported TTS engine: {engine}")
            return

        # Log success only if the file was created
        if os.path.exists(output_file):
            print(f"Audio saved to: {output_file}")
        else:
            print(f"Error: Audio file was not created. Please check the TTS engine configuration.")

    except Exception as e:
        print(f"Error during text-to-speech conversion with engine '{engine}': {e}")
        print("Please check the input parameters and ensure the required dependencies are installed.")

def text_to_audio_with_fallback(text, language, output_file, selected_engine="gtts", description=None):
    """
    Convert text to speech using the selected engine, with a fallback mechanism.

    Parameters:
    - text: The text to convert to speech.
    - language: The language code (e.g., 'ml' for Malayalam, 'ta' for Tamil, 'en' for English).
    - output_file: The path to save the audio file.
    - selected_engine: The primary TTS engine to use.
    - description: A detailed description of how the speech should sound (used for Indic Parler TTS).
    """
    try:
        # Attempt to use the selected engine
        text_to_audio(text, language, output_file, engine=selected_engine, description=description)
    except Exception as e:
        print(f"Error with engine '{selected_engine}': {e}")
        fallback_engine = "gtts" if selected_engine != "gtts" else "indic"
        print(f"Falling back to engine: {fallback_engine}")
        text_to_audio(text, language, output_file, engine=fallback_engine, description=description)