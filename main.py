import glob
import os
from funcoes import convert_audio_to_flac, remove_audios_separados, remove_audios_transcritos, split_audio_and_return_file_path, transcribe_each_audio_files_on_recognize_google, transform_to_txt_file

split_time = 50000 # milisegundos

# criar pasta para audios separados (se nao existir) 
if not os.path.exists('audios_separados'):
    os.makedirs('audios_separados')

# criar pasta para textos (se nao existir)
if not os.path.exists('textos'):
    os.makedirs('textos')

# Finds all audio files in the audios directory
audio_files = glob.glob('audios/*.mp3')
audio_files.extend(glob.glob('audios/*.wav'))
audio_files.extend(glob.glob('audios/*.m4a'))
convert_audio_to_flac(audio_files)
flac_files = glob.glob('audios/*.flac')

for flac_file in flac_files:
    try:
        name_file = flac_file.split('/')[-1].split('.')[0]
        audios_file_path_dict = split_audio_and_return_file_path(flac_file, split_time)
        full_transcription_str = transcribe_each_audio_files_on_recognize_google(audios_file_path_dict)
        transform_to_txt_file(full_transcription_str, name_file)
        remove_audios_separados()
        remove_audios_transcritos(name_file)     
    except Exception as e:
        print(f'Erro ao processar {flac_file}')
        print(e)
        with open('audios_que_nao_foram_convertidos_com_sucesso.txt', 'a') as f:
            f.write(flac_file + '\n')


        
