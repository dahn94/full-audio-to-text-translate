import speech_recognition as sr
from pydub import AudioSegment
import glob, os
# convert mp3 file to wav (se necessario)
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")

wave_files = glob.glob('*.wav')

for wave_file in wave_files:
    print(wave_file)


    # Dividir o audio
    sound = AudioSegment.from_file(wave_file)
    audio_files = sound[::60000]

    full_transcription = ""


    # Transformar as partes do audio em txt
    for index, audio_file in enumerate(audio_files):
        audio_file_name = f'audios_separados/audio_file_{index + 1}'
        audio_file.export(audio_file_name, format='wav')
        print(f'processando {audio_file_name}')
        r = sr.Recognizer()
        with sr.AudioFile(audio_file_name) as source:
            audio = r.record(source)
            transcription = f'Transcription {index + 1}: ' + r.recognize_google(audio, language='pt-BR')
            full_transcription = full_transcription + transcription + '\n' + '\n'
    
    size = len(wave_file)
    name_file = wave_file[:size - 4]        
    with open(f'textos/{name_file}.txt', 'w') as f:
        f.write(full_transcription)
    
    # remover audios separados 
    dir = 'audios_separados'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

