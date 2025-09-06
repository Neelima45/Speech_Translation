import speech_recognition as sr

def speech_to_text_from_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Error with the speech recognition service")

speech_to_text_from_file("sample.wav")
