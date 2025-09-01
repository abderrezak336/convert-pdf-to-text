

API_KEY = "YOUR API KEY"
USER_ID = "YOUR USER ID"

# import the playht SDK
from pyht import Client, TTSOptions, Format

# Initialize PlayHT API with your credentials
client = Client(USER_ID, API_KEY)

def convert_text_to_audio(voice, pdf_text, saved_location):
    # configure your stream
    options = TTSOptions(
        voice=voice,
        sample_rate=44_100,
        format=Format.FORMAT_MP3,
        speed=1,
    )

    # text to synthesize
    text = pdf_text

    # Open a file in binary write mode to save the MP3
    with open(f"{saved_location}/output.mp3", "wb") as audio_file:
        # Stream the TTS result and write each chunk to the file
        for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
            audio_file.write(chunk)









