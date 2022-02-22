import speech_recognition as sr
from pydub import AudioSegment

# convert mp3 file to wav (se necessario)
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")

# Dividir o audio
sound = AudioSegment.from_file('audio_example.wav')
audio_files = sound[::60000]

# Transformar as partes do audio em txt
for index, audio_file in enumerate(audio_files):
    audio_file_name = f'audios_separados/audio_file_{index + 1}'
    audio_file.export(audio_file_name, format='wav')
    print(f'processando {audio_file_name}')
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_name) as source:
        audio = r.record(source)
        transcription = f'Transcription {index + 1}: ' + r.recognize_google(audio,
                                                               language='pt-BR')
        with open(f'textos_separados/audio_example[{index + 1}].txt', 'w') as f:
            f.write(transcription)

