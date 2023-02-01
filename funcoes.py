import speech_recognition as sr
from pydub import AudioSegment
import glob, os

def convert_audio_to_flac(audio_files):
    for audio_file in audio_files:
        sound = AudioSegment.from_file(audio_file)
        sound.export(audio_file[:len(audio_file) - 4] + '.flac', format='flac')


def split_audio_and_return_file_path(wave_file, split_time):
    audios_file_path_dict = []
    sound = AudioSegment.from_file(wave_file)
    audio_files = sound[::split_time]
    for index, audio_file in enumerate(audio_files):
        audio_file_name = f'audios_separados/audio_file_{index + 1}'
        audios_file_path_dict.append(audio_file_name)
        audio_file.export(audio_file_name, format='flac')
    return audios_file_path_dict

def transcribe_each_audio_files_on_recognize_google(audios_file_path_dict):
    full_transcription = ""
    for audio_file_name in audios_file_path_dict:
        print(f'processando {audio_file_name}')
        r = sr.Recognizer()
        with sr.AudioFile(audio_file_name) as source:
                audio = r.record(source)
                transcription = r.recognize_google(audio, language='pt')
                full_transcription = full_transcription + transcription + '\n' + '\n'
    
    return full_transcription

def transform_to_txt_file(full_transcription_str, name_file):
    with open(f'textos/{name_file}.txt', 'w') as f:
        f.write(full_transcription_str)
    
def remove_audios_separados():
    dir = 'audios_separados'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

def remove_audios_transcritos(name_file):
    dir = 'audios'
    # deletar arquivo que comeca com o nome do arquivo
    filelist = glob.glob(os.path.join(dir, f'{name_file}*'))
    for f in filelist:
        os.remove(f)
